from fastapi import FastAPI ,Request ,Path ,HTTPException,Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json 
import uvicorn

""" 
| Import          | Use                       |
| --------------- | ------------------------- |
| FastAPI         | Create app                |
| Request         | Needed for templates      |
| Path            | Validate path parameters  |
| Query           | Validate query parameters |
| HTTPException   | Raise errors              |
| HTMLResponse    | Return HTML               |
| Jinja2Templates | Render templates          |
| json            | Read JSON file            |
| uvicorn         | Run server                |

"""

app =FastAPI()

#Load Data from File 
def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
        
    return data

# basic from page of the web 
@app.get('/')
def hello():
    return {'message':'hello world'}

templates = Jinja2Templates(directory="templates")

# HTTML end point 
@app.get("/about",response_class=HTMLResponse)
async def about(request:Request):
    context={"request":request,"name":"Thanuja"}
    return templates.TemplateResponse("index.html",context)

#view all data 

@app.get('/view')
def view():
    return load_data()
"""Return the all data """

#Path parameter example 8 
""" here the patient_id is the dynamic URL input """
@app.get('/patients/{patient_id}')
def view_patient(patient_id:str=Path(...,desription='Id of the patient in the DB',examples='P001')):
    data=load_data()
    
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="patient not found")

#query parameter example 
@app.get('/sort')
def sort_patients(
    sort_by:str=Query(...,description="sort on the basis of height,weight and bmi"),
    sort_order:str=Query('asc',description='sort in asc or dsc order')
    ):
    """ here sort_by is the required query param, 
             sort_order: optional (default=asc)"""
    valid_fields=['height','weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f'Invalid field ,select from {valid_fields}')
    
    if sort_order not in ['asc', 'desc']:
        raise HTTPException(status_code=400,detail=f'Invalid sort order select btween asc or desc')
    
    data=load_data()
    
    order=True if sort_order=="desc" else False 
    
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=order)
    """If 'age' doesnot exist ,use 0 as the default 
     So 0 here prevents errors like KeyError if 'age' is missing, and ensures those entries are treated as having age 0."""
    return sorted_data

if __name__=="__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )    
        
    
    
