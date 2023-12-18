from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI ,Request
from bot import chat
from pydantic import BaseModel
import json
from fastapi.encoders import jsonable_encoder

class Item(BaseModel):
    query: str
    # description: str | None = None
    # price: float
    # tax: float | None = None


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/")
def read_root(query:Item):
    
    response =chat(query.query)

    return response


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}