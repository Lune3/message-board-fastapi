from typing import Union, List
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi import Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from datetime import date

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

class Message(BaseModel):
    name: str
    text: str
    added: date = Field(default_factory=date.today)

today = date.today()

messages: List[Message] = [
    Message(text="Hi There!", name="John", added=today),
    Message(text="Hello World", name="Jane", added=today)
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
async def formPagePost(request: Request,message : Message = Form(...)):
    messages.append(message)
    return RedirectResponse('/',status_code=303)
    
    

