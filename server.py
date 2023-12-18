from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from bot import chat
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/")
def read_root():
    response =chat()
    return response


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}