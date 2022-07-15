from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello Invoice User"}

@app.get("/customers")
async def customers():
    return {"customer": "Sebastian Ramirez"}

@app.get("/products")
async def products():
    return {"product": "Hammer"}

@app.get("/invoices")
async def invoices():
    return {"invoice": "1000"}

@app.get("/pdf_invoice")
async def pdf_invoice():
    return {"pdf_invoice": "1000"}
