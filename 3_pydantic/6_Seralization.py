from pydantic import BaseModel
class Address(BaseModel):
    city:str
    state:str
    pin :str
    
class Patient(BaseModel):
    name:str
    gennder:str='Male'
    age:int
    address:Address
    
    
address_dict ={'city':'haryana','state':'thamil nadu','pin':'122001'}

address1 = Address(**address_dict)
patient_dict = {'name': 'nitish', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

temp1 = patient1.model_dump(exclude_unset=True) 
temp2 = patient1.model_dump_json()
print(temp1)
print("type of temp1 is ",type(temp1))
print(temp2)
print("type(temp2) is ",type(temp2))