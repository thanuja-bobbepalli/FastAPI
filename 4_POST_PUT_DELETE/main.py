"""
FastAPI Patient Management API
--------------------------------
A simple CRUD API for managing patient records.

Features:
- Create, view, edit, delete patients
- Sort patients by height, weight, or BMI
- Computed BMI and verdict fields
- JSON file used as data storage
"""
#=====imports===================
from fastapi import FastAPI, Request, Path, HTTPException, Query
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json
import uvicorn

app=FastAPI(
    
    title="Patient Mangement API",
    version="1.0.0",
    description="A simple application fro managing patient data"
 )

templates = Jinja2Templates(directory="templates")
class Patient(BaseModel):
    """
    Represents a patient record.
    Includes automatically computed fields for BMI and health verdict.
    """
    id: Annotated[str, Field(..., description="Unique ID of the patient", examples=['P001'])]
    name: Annotated[str, Field(..., description="Full name of the patient")]
    city: Annotated[str, Field(..., description="City where the patient lives")]
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the patient")]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description="Gender of the patient")]
    height: Annotated[float, Field(..., gt=0, description="Height of the patient (in meters)")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the patient (in kilograms)")]

    # Computed field for BMI
    @computed_field
    @property
    def bmi(self) -> float:
        """Calculate Body Mass Index."""
        return round(self.weight / (self.height ** 2), 2)

    # Computed field for BMI verdict
    @computed_field
    @property
    def verdict(self) -> str:
        """Return health verdict based on BMI."""
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 30:
            return "Normal"
        return "Obese"

class PatientUpdate(BaseModel):
    """
    Partial update model for patient data.
    All fields are optional for flexible updates.
    """
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female', 'others']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]

# -----------------------------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------------------------
def load_data() -> dict:
    """Load all patient data from the JSON file."""
    with open('patients.json', 'r') as f:
        return json.load(f)
    
def save_data(data: dict) -> None:
    """Save all patient data back to the JSON file."""
    with open('patients.json', 'w') as f:
        json.dump(data, f, indent=4)
        
# -----------------------------------------------------------------------------
# Routes: General
# -----------------------------------------------------------------------------
@app.get("/", tags=["General"])
def hello():
    """Root route - returns a welcome message."""
    return {"message": "Hello, world! Welcome to the Patient API."}


@app.get("/about", response_class=HTMLResponse, tags=["General"])
async def about(request: Request):
    """
    Render a simple HTML page using Jinja2 template.
    Example use-case: displaying basic app info.
    """
    context = {"request": request, "name": "Thanuja"}
    return templates.TemplateResponse("index.html", context)

@app.get("/view", tags=["Patients"])
def view_patients():
    """Return all patient records."""
    return load_data()


@app.get("/patient/{patient_id}", tags=["Patients"])
def view_patient(
    patient_id: str = Path(..., description="Patient ID to retrieve", examples="P001")
):
    """Fetch a single patient's data by ID."""
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    return data[patient_id]



@app.get("/sort", tags=["Patients"])
def sort_patients(
    sort_by: str = Query(..., description="Sort field: height, weight, or bmi"),
    sort_order: str = Query('asc', description="Sort order: 'asc' or 'desc'")
):
    """
    Sort patients by a specific field (height, weight, or BMI).
    """
    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field. Choose from {valid_fields}")
    if sort_order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Sort order must be 'asc' or 'desc'")

    data = load_data()
    reverse_order = sort_order == 'desc'

    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=reverse_order
    )
    return sorted_data

# -----------------------------------------------------------------------------
# Routes: Create / Update / Delete
# -----------------------------------------------------------------------------

@app.post("/create",tags=["Patients"])
def create_patients(patient:Patient):
    """ creat a new patient record .Raises error if patient id is alrady exist ."""
    data=load_data()
    
    if patient.id in data:
        raise HTTPException(status_code=400,detail="Patient alrady exists")
    data[patient.id]=patient.model_dump(exclude=['id'])
    """This line:

Takes patient data

Converts it to dictionary

Stores it using ID as key"""
    save_data(data)
    
    return JSONResponse(status_code=201,content={"message":"Ptient created sucessfully"})
   
@app.put('/edit/{patient_id}',tags=["Ptients"])
def update_patient(patient_id:str,patient_update:PatientUpdate) :
    
    existing_patient_info=view_patient(patient_id=patient_id)
    
    update_fields=patient_update.model_dump(exclude_unset=True)
    for key,value in update_fields.items(): 
        existing_patient_info[key]=value
    # Rebuild with Pydantic model to auto-update computed fields
    existing_patient_info['id'] = patient_id
    patient_obj = Patient(**existing_patient_info)

    # Save updated record
    data = load_data()
    data[patient_id] = patient_obj.model_dump(exclude=['id'])
    save_data(data)

    return JSONResponse(status_code=201, content={"message": "Patient updated successfully"})        
"""  
Receive update request

Fetch existing patient

Extract only updated fields

Update dictionary

Recreate Pydantic model

Replace old data

Save file

Return response
"""
@app.delete("/delete/{patient_id}", tags=["Patients"])
def delete_patient(patient_id: str):
    """
    Delete a patient record by ID.
    Returns a success message if deleted.
    """
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    del data[patient_id]
    save_data(data)

    return JSONResponse(status_code=201, content={"message": "Patient deleted successfully"})


# -----------------------------------------------------------------------------
# Run App
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )

    
    

        
 