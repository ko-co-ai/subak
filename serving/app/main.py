from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from app.model import Model

class Message(BaseModel):
    problem: str

app = FastAPI()
model = Model()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/generate")
async def generate(message: Message):
    generated = model.generate(message.problem)
    return generated
