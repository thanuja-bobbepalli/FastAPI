# 🚀 FastAPI Path & Query Parameters (With Correct Understanding)

---

# 📌 What are Parameters in FastAPI?

In FastAPI, **parameters are used to send input from the URL to the backend function**.

There are two main types:

* 🔹 **Path Parameters** → part of URL path
* 🔹 **Query Parameters** → after `?` in URL

---

# 🔥 Important Understanding (VERY IMPORTANT)

👉 Parameters **DO NOT directly fetch data from files or database**

They only:

* Take input from URL
* Pass it to your function

👉 Your function decides:

* Whether to read from file
* Fetch from database
* Filter data
* Or return static response

---

# 🧠 Correct Concept

| Component | Role        |
| --------- | ----------- |
| URL       | Input       |
| Parameter | Variable    |
| Function  | Logic       |
| File/DB   | Data Source |

---

# 🔹 1. Path Parameters

## 📌 Definition

Values embedded inside the URL path.

---

## ✅ Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

---

## 🌐 URL

```
/user/10
```

---

## 📤 Output

```json
{
  "user_id": 10
}
```

---

## 🧠 Key Points

* Required parameter
* Used to identify specific resource
* Type validation is automatic

---

# 🔥 Path Parameter with Data Source

```python
users = {
    1: "Hareesh",
    2: "Ravi"
}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"name": users.get(user_id, "Not found")}
```

👉 Here:

* Parameter is used to **select data**
* Not directly reading — logic does it

---

# 🔹 2. Query Parameters

## 📌 Definition

Values passed after `?` in URL.

---

## ✅ Example

```python
@app.get("/items/")
def get_items(limit: int = 2):
    return {"limit": limit}
```

---

## 🌐 URL

```
/items/?limit=5
```

---

## 📤 Output

```json
{
  "limit": 5
}
```

---

## 🧠 Key Points

* Optional (default values allowed)
* Used for filtering, pagination

---

# 🔥 Query Parameter with Data

```python
items = ["apple", "banana", "mango", "grapes"]

@app.get("/items/")
def get_items(limit: int = 2):
    return {"items": items[:limit]}
```

👉 Query parameter controls:

* How much data to return

---

# 🔹 Combined Example

```python
@app.get("/users/{user_id}")
def get_user_posts(user_id: int, limit: int = 2):
    return {
        "user_id": user_id,
        "limit": limit
    }
```

---

## 🌐 URL

```
/users/5?limit=3
```

---

# 🔹 Path vs Query Parameters

| Feature  | Path Parameter    | Query Parameter    |
| -------- | ----------------- | ------------------ |
| Location | URL path          | After `?`          |
| Example  | `/user/10`        | `/items?limit=5`   |
| Required | ✅ Yes             | ❌ Optional         |
| Use case | Identify resource | Filter/modify data |

---

# ⚙️ How to Run

## 🔹 Install Dependencies

```bash
pip install fastapi uvicorn
```

---

## 🔹 Run Server

```bash
uvicorn main:app --reload
```

---

# 🌐 How to Test

## 🔹 Browser

* `/user/10`
* `/items/?limit=5`

---

## 🔹 Swagger UI (Best)

```
http://127.0.0.1:8000/docs
```

---

# ❌ Common Mistakes

| Mistake                        | Fix                  |
| ------------------------------ | -------------------- |
| Thinking parameters fetch data | ❌ Wrong              |
| Parameters only pass values    | ✅ Correct            |
| Missing `{}` in path           | Use `/user/{id}`     |
| Forget `?` in query            | Use `/items?limit=5` |

---

# 🎯 Key Takeaways

* Parameters = input from URL
* They do NOT fetch data directly
* Your function uses them to:

  * Fetch data
  * Filter data
  * Process logic

---

# 🔥 Final Summary (Interview Ready)

👉
**Path and query parameters are used to pass values from the URL to the backend. They do not directly retrieve data, but help the backend logic decide what data to fetch or return from sources like files or databases.**

---
