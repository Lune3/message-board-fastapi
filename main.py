from typing import Union
from fastapi import FastAPI
from datetime import date

app = FastAPI()
today = date.today()

message = [{'text':"Hi There!",'user':"John",'added':today},{'text':"Hello World",'user':"Jane",'added':today}]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}