# FastAPI CRUD Testing Guide (POST, PUT, DELETE using /docs)

This guide explains how to test your FastAPI endpoints (POST, PUT, DELETE) using the built-in Swagger UI.

---

# Step 1: Run the Server

Start your FastAPI application:

```bash
uvicorn main:app --reload
```

Now open your browser and go to:

```
http://127.0.0.1:8000/docs
```

---

# Step 2: Understanding Swagger UI

Swagger UI (`/docs`) provides:

* Interactive API testing
* Input forms for requests
* Live responses

All your endpoints will be grouped using **tags** (e.g., Patients, General).

---

# Step 3: Create Data (POST)

## Endpoint:

```
POST /create
```

## Steps:

1. Click **POST /create**
2. Click **Try it out**
3. Enter JSON:

```json
{
  "id": "P001",
  "name": "Thanuja",
  "city": "Nuzvid",
  "age": 22,
  "gender": "female",
  "height": 1.6,
  "weight": 50
}
```

4. Click **Execute**

## Expected Output:

```json
{
  "message": "Patient created successfully"
}
```

---

# Step 4: View Data (GET)

## Endpoint:

```
GET /view
```

Click **Execute**

You should see:

```json
{
  "P001": {
    "name": "Thanuja",
    "city": "Nuzvid",
    "age": 22,
    "gender": "female",
    "height": 1.6,
    "weight": 50
  }
}
```

---

# Step 5: Update Data (PUT)

## Endpoint:

```
PUT /edit/{patient_id}
```

## Steps:

1. Click **PUT /edit/{patient_id}**
2. Click **Try it out**
3. Enter:

   * patient_id → `P001`
4. Enter JSON:

```json
{
  "weight": 55
}
```

5. Click **Execute**

## Expected Output:

```json
{
  "message": "Patient updated successfully"
}
```

---

# Step 6: Delete Data (DELETE)

## Endpoint:

```
DELETE /delete/{patient_id}
```

## Steps:

1. Click **DELETE /delete/{patient_id}**
2. Click **Try it out**
3. Enter:

   * patient_id → `P001`
4. Click **Execute**

## Expected Output:

```json
{
  "message": "Patient deleted successfully"
}
```

---

# Step 7: Verify Changes

After each operation:

* Use `GET /view` to check updated data

---

# Important Notes

* POST → Creates new data

* PUT → Updates existing data

* DELETE → Removes data

* GET → Retrieves data

* Always create data before updating or deleting

* Ensure correct data types (e.g., height in meters like 1.6, not 160)

---

# Summary

Swagger UI (`/docs`) allows you to:

* Test all API endpoints easily
* Send requests without writing frontend code
* Debug and verify API behavior

This is the easiest way to interact with FastAPI during development.

---
