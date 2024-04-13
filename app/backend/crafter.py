# -*- coding: utf-8 -*-

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Input(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

class Output(BaseModel):
    model_reponse: str

@app.get("/healthcheck")
def healthcheck():
    return {"status": "The service is healthy"}

@app.post("/generate/agent", response_model=Output)
def predict_agent(input: Input):
    # Your prediction logic goes here
    pass

