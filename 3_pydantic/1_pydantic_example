from pydantic import BaseModel , EmailStr, AnyUrl,Field
from typing import List ,Dict ,Optional ,Annotated

class Patient(BaseModel):
    
    name:Annotated[str,Field(max_length=50,title="name of the patient",description="Give the name of the patient in less than 50 chars",examples=['Hanu','Aravind'])]
    email: EmailStr
    linkedin_url:AnyUrl
    age:int=Field(gt=10,lt=100)
    weight:Annotated[float,Field(gt=0,strict=True)]
    married:Annotated[bool,Field(default=None,description="Is the patient married or not ")]
    allergies:Annotated[Optional[List[str]],Field(default=None,max_length=5)]
    contact_details:Dict[str,str]
    
def updated_patient_data(patient:Patient):
    
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')
    
patient_info={'name':'Nikhil', 'email':'abc@gmail.com', 'linkedin_url':'http://linkedin.com/1322', 'age': '21', 'weight': 57,'contact_details':{'phone':'2353462'}}


patient1=Patient(**patient_info)
updated_patient_data(patient1)
print(patient1)