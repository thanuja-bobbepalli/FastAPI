# 🚀 FastAPI + Jinja2 Templates (Beginner Guide)

## 📌 What This Project Does

This is a simple **FastAPI application** that demonstrates:

* ✅ Creating a basic API endpoint (returns JSON)
* ✅ Rendering an HTML page using **Jinja2 templates**
* ✅ Passing dynamic data from backend → frontend

---

# 🧠 Code Explanation

## 🔹 1. Imports

```python
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
```

### Purpose:

* `FastAPI` → Create app
* `Request` → Required for templates
* `HTMLResponse` → Return HTML instead of JSON
* `Jinja2Templates` → Render HTML files

---

## 🔹 2. Initialize App

```python
app = FastAPI()
```

👉 Main FastAPI application instance

---

## 🔹 3. JSON API Endpoint

```python
@app.get('/')
def hello():
    return {'message':'hellow world'}
```

### What it does:

* URL → `/`
* Returns → JSON response

### Output:

```json
{
  "message": "hellow world"
}
```

---

## 🔹 4. Setup Templates

```python
templates = Jinja2Templates(directory="templates")
```

👉 Tells FastAPI:

* HTML files are inside **templates/** folder

---

## 🔹 5. HTML Endpoint

```python
@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    context = {"request": request, "name": "Hareesh"}
    return templates.TemplateResponse("index.html", context)
```

### What it does:

* URL → `/about`
* Sends data (`name`) to HTML
* Renders `index.html`

---

## 🔹 6. HTML Template (index.html)

```html
<html>
<body>
    <h1>Hello {{ name }}</h1>
</body>
</html>
```

### Output in browser:

```
Hello Hareesh
```

---

# 📁 Project Structure (VERY IMPORTANT)

```
1_Intro_to_Fastapi/
│
├── main.py
└── templates/
    └── index.html
```

### Rules:

* `templates/` must be same level as `main.py`
* File name must be exactly `index.html`

---

# ⚙️ How to Run This Project

## 🔹 Step 1: Create Virtual Environment

```bash
python -m venv venv
```

---

## 🔹 Step 2: Activate Environment

### Windows:

```bash
venv\Scripts\activate
```

---

## 🔹 Step 3: Install Dependencies

```bash
pip install fastapi uvicorn jinja2
```

---

## 🔹 Step 4: Run Server

```bash
uvicorn main:app --reload
```

👉 Important:

* `main` = filename (without `.py`)
* `app` = FastAPI instance

---

# 🌐 How to Check Output

## 🔹 1. API Response (JSON)

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🔹 2. HTML Page

```
http://127.0.0.1:8000/about
```

---

## 🔹 3. Swagger UI (Best for Testing)

```
http://127.0.0.1:8000/docs
```

👉 Click → Try it out → Execute

---

## 🔹 4. Logs in Terminal

You’ll see:

```
GET / 200 OK
```

---

# ❌ Common Errors & Fixes

## 🔸 Error: Could not import module

```bash
# ❌ Wrong
uvicorn main.py:app --reload

# ✅ Correct
uvicorn main:app --reload
```

---

## 🔸 Error: TemplateNotFound

```
jinja2.exceptions.TemplateNotFound
```

### Fix:

* Create `templates/` folder
* Add `index.html` inside it

---

## 🔸 Error: Server not stopping

Press:

```
CTRL + C
```

---

# 🎯 Key Takeaways

* FastAPI supports both **API + Web pages**
* JSON response → default behavior
* HTML response → use `HTMLResponse`
* Templates → handled by Jinja2
* Folder structure is **critical**
* Always run using:

  ```
  uvicorn main:app --reload
  ```

---

# 🔥 Summary (Interview Ready)

This project demonstrates:

* Building REST API using FastAPI
* Rendering dynamic HTML using Jinja2
* Passing backend data to frontend
* Running server using Uvicorn

👉 It combines **backend + frontend basics**, making it a strong beginner project.

---
