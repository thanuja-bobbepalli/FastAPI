from fastapi import FastAPI ,Request 
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


"""
FastAPI → Creates the main app

Request → Represents incoming HTTP request (needed for templates)

HTMLResponse → Tells FastAPI to return HTML instead of JSON

Jinja2Templates → Used to render HTML templates (like dynamic web pages)

"""

app=FastAPI()

#first Endpoint 

@app.get('/')
def hello():
    return {'message':'Hello world'}

"""
-> @app.get('/') → This is a GET API endpoint

-> URL: http://localhost:8000/

 ``` def hello('/')  : Called when user visits / ```
 
 return {'message':'Hello world'} : 👉 FastAPI automatically converts this into JSON
"""

#Template setup 
templates=Jinja2Templates(directory="templates")

""" My HTML files are inside a folder named tmeplates """

# HTML Endpoin (Dynamic page)
@app.get("/about",response_class=HTMLResponse)
async def about(request:Request):
    context={"request":request,"name":"Thanuja"}
    
    return templates.TemplateResponse("index.html",context)

"""
/about → URL endpoint

response_class=HTMLResponse → Return HTML (not JSON)

async def → Asynchronous function (better performance)

context = {"request": request, "name": "Thanuja"}

👉 This data is passed to HTML template

⚠️ Important:

"request" is mandatory in FastAPI templates

"name" → Custom data you want to display
  
 return templates.TemplateResponse("index.html", context)

👉 What happens here:

Loads index.html

Injects context data

Returns rendered HTML page
 
"""
