# FastAPI HTTP Methods POST PUT DELETE GET Complete Guide

---

# What are POST PUT DELETE GET in FastAPI

POST PUT DELETE and GET are HTTP methods used to perform operations on data in an API.

They define what kind of action the client wants to perform.

---

# Why We Need Them

In real applications we do not just read data we also need to

* Create new data
* Read data
* Update existing data
* Delete data

These operations are handled using different HTTP methods.

---

# Overview of Methods

| Method | Purpose              |
| ------ | -------------------- |
| GET    | Read data            |
| POST   | Create new data      |
| PUT    | Update existing data |
| DELETE | Remove data          |

---

# GET Method

## What it does

GET is used to retrieve data from the system.

---

## Why we use it

* To fetch data like users, patients, products
* Does not modify data

---

## Example

```python id="nq6lg4"
@app.get("/patients")
def get_patients():
    return patients
```

---

## How it works

1. Client sends request
2. Server fetches data
3. Data is returned as response

---

# POST Method

## What it does

POST is used to create new data in the system.

---

## Why we use it

* To add new users, patients, products
* Sends data in request body

---

## Example

```python id="0v4u0b"
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Patient(BaseModel):
    name: str
    age: int

patients = []

@app.post("/patients")
def create_patient(patient: Patient):
    patients.append(patient)
    return {"message": "Patient added", "data": patient}
```

---

## How it works

1. Client sends JSON data
2. FastAPI validates using Pydantic
3. Data is stored
4. Response is returned

---

# PUT Method

## What it does

PUT is used to update existing data completely.

---

## Why we use it

* To modify existing records
* Replaces old data with new data

---

## Example

```python id="rhtj8l"
@app.put("/patients/{index}")
def update_patient(index: int, patient: Patient):
    if index >= len(patients):
        return {"error": "Patient not found"}
    
    patients[index] = patient
    return {"message": "Patient updated", "data": patient}
```

---

## How it works

1. Client sends updated data
2. FastAPI validates it
3. Existing data is replaced
4. Updated result is returned

---

# DELETE Method

## What it does

DELETE is used to remove data from the system.

---

## Why we use it

* To delete users, records, entries

---

## Example

```python id="qdlqnj"
@app.delete("/patients/{index}")
def delete_patient(index: int):
    if index >= len(patients):
        return {"error": "Patient not found"}
    
    removed = patients.pop(index)
    return {"message": "Patient deleted", "data": removed}
```

---

## How it works

1. Client sends identifier
2. FastAPI finds the data
3. Data is removed
4. Confirmation response is returned

---

# How They Are Used in FastAPI

FastAPI uses decorators to define HTTP methods

```python id="w3t4r0"
@app.get("/path")
@app.post("/path")
@app.put("/path")
@app.delete("/path")
```

Each decorator maps a function to a specific HTTP action.

---

# How They Affect the System

| Method | Effect                |
| ------ | --------------------- |
| GET    | Reads data            |
| POST   | Adds new data         |
| PUT    | Updates existing data |
| DELETE | Removes data          |

---

# Real World Flow

* GET → Fetch patients
* POST → Add new patient
* PUT → Update patient details
* DELETE → Remove patient

---

# Key Takeaways

* GET is for reading data
* POST is for creation
* PUT is for updating
* DELETE is for removal
* FastAPI uses decorators to map them
* Pydantic ensures data validation

---

# Summary

GET POST PUT and DELETE are essential HTTP methods used to manage data in FastAPI applications. GET retrieves data, POST creates new data, PUT updates existing data, and DELETE removes data. Together they provide complete control over data operations and form the foundation of REST APIs.

---
