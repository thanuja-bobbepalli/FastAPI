# FastAPI Pydantic Complete Guide

---

# What is Pydantic

Pydantic is a Python library used for data validation, parsing, and type enforcement.
It ensures that the data coming into your API is correct, structured, and safe.

---

# Why Pydantic is Needed

Problem without Pydantic

* No validation leads to incorrect data entering the system
* Manual validation makes code complex and hard to maintain
* Type errors can cause runtime failures

Solution with Pydantic

* Automatic validation of input data
* Cleaner and structured code
* Built-in error handling
* Seamless integration with FastAPI

---

# Core Idea

Define a schema using a model and FastAPI will automatically validate incoming data based on that schema.

---

# Basic Example

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Patient(BaseModel):
    name: str
    age: int
    weight: float

@app.post("/patient")
def create_patient(patient: Patient):
    return patient
```

Input JSON

```json
{
  "name": "Thanuja",
  "age": 25,
  "weight": 70.5
}
```

Output

```json
{
  "name": "Thanuja",
  "age": 25,
  "weight": 70.5
}
```

Invalid Input Example

```json
{
  "name": "Thanuja",
  "age": "twenty"
}
```

FastAPI automatically returns a validation error.

---

# Field (Validation and Metadata)

Field is used to define validation rules and add extra information like descriptions.

```python
from pydantic import BaseModel, Field

class Patient(BaseModel):
    name: str = Field(..., min_length=3, description="Patient name")
    age: int = Field(..., gt=0, lt=120)
    weight: float = Field(..., gt=0)
```

---

# Field Validator

Field validator is used to validate or modify a single field.
It allows you to apply custom logic to one specific field.

```python
from pydantic import field_validator

class Patient(BaseModel):
    name: str

    @field_validator("name")
    def name_must_be_valid(cls, value):
        if not value.isalpha():
            raise ValueError("Name must contain only letters")
        return value
```

---

# Model Validator

Model validator is used to validate the entire model.
It is useful when validation depends on multiple fields.

```python
from pydantic import model_validator

class Patient(BaseModel):
    age: int
    weight: float

    @model_validator(mode="after")
    def check_health(cls, values):
        if values.weight < 30:
            raise ValueError("Weight too low")
        return values
```

---

# Computed Fields

Computed fields are values calculated from existing fields.
They are not provided by the user but generated automatically.

```python
from pydantic import computed_field

class Patient(BaseModel):
    weight: float
    height: float

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)
```

Output includes bmi automatically.

---

# Nested Models

Nested models allow one model to be used inside another model.
This helps represent complex structured data.

```python
class Address(BaseModel):
    city: str
    state: str

class Patient(BaseModel):
    name: str
    address: Address
```

Input JSON

```json
{
  "name": "Thanuja",
  "address": {
    "city": "Hyderabad",
    "state": "Telangana"
  }
}
```

---

# Serialization

Serialization means converting a Pydantic model into a dictionary or JSON format.

```python
patient = Patient(name="Thanuja", age=25, weight=70)
print(patient.model_dump())
```

Output

```python
{
  "name": "Thanuja",
  "age": 25,
  "weight": 70
}
```

You can also exclude fields

```python
patient.model_dump(exclude={"age"})
```

---

# FastAPI and Pydantic Flow

1. Request comes in JSON format
2. Pydantic validates the data
3. Data is converted into Python object
4. Your function processes the data
5. Response is returned

---

# Common Mistakes

* Using plain dictionary instead of Pydantic model
* Not defining validation rules
* Writing validation logic inside route instead of validators

---

# Key Takeaways

* Pydantic handles validation and parsing
* Reduces manual error checking
* Ensures type safety
* Supports nested models and computed fields
* Makes APIs clean and production ready

---
# Final Summary of Pydantic Features

Pydantic provides a structured and reliable way to handle data in FastAPI by combining validation, parsing, and type enforcement into a single system.

---

# Validators Overview Table

| Feature         | Type                          | What it Does                                        | When to Use                                                          |
| --------------- | ----------------------------- | --------------------------------------------------- | -------------------------------------------------------------------- |
| Field           | Built-in validation           | Adds constraints like min, max, length, description | When defining basic rules for a single field                         |
| field_validator | Custom field-level validation | Applies custom logic to one field                   | When one field needs special validation (for example only alphabets) |
| model_validator | Full model validation         | Validates multiple fields together                  | When validation depends on multiple fields                           |

---

# Other Important Pydantic Features

| Feature         | Purpose                        | Benefit                        |
| --------------- | ------------------------------ | ------------------------------ |
| Computed Fields | Automatically calculate values | Avoids storing redundant data  |
| Nested Models   | Embed models inside models     | Handle complex structured data |
| Serialization   | Convert model to dict or JSON  | Easy API response and storage  |

---

# Summary

Pydantic ensures that data in FastAPI applications is validated, structured, and consistent. Field handles basic validation, field_validator handles custom single field logic, and model_validator ensures correctness across multiple fields. Computed fields reduce redundancy, nested models manage complex data, and serialization enables easy data transfer. Together, these features make APIs reliable, clean, and production ready.
          
 ( or simply )


Pydantic is a data validation and parsing library used in FastAPI to enforce data types, validate inputs, and structure request and response data efficiently. It helps build reliable, clean, and scalable APIs by reducing manual validation and preventing invalid data from entering the system.

---
