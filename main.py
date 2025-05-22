from typing import Union, List
from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from datetime import date

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class message(BaseModel):
    name: str
    text: str
    added: date

today = date.today()

messages: List[message] = [
    message(text="Hi There!", name="John", added=today),
    message(text="Hello World", name="Jane", added=today)
]


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        request=request,name="index.html",context={'messages':messages}
    )


@app.get("/new")
def formPage(request: Request):
    return templates.TemplateResponse(
        request=request, name="form.html"
    )

@app.post("/new")
def formPagePost(request: Request, response: Response,message: message):
    messages.append(message)
    

