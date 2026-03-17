from pydantic import BaseModel ,EmailStr,AnyUrl,Field ,field_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]
    
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        
        valid_domains =['hdfc.com','icici.com']
        
        domain_name=value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
      
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode='after') # this mode = after makes sure that age value got here after type conversion
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')

def updated_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')
    
patient_info={'name':'Nikhil', 'email':'abc@icici.com',  'age': '21', 'weight': 57,'married':False,'allergies': ['pollen', 'dust'],'contact_details':{'phone':'2353462'}}


patient1=Patient(**patient_info)
updated_patient_data(patient1)
print(patient1)      
   
    