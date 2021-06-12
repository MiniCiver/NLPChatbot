from fastapi import FastAPI, Request
from typing import Optional
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn
import numpy as np
import json

from aibot import mainchatbot

app = FastAPI()

app.mount("/static", StaticFiles(directory="../barber_shop"), name="static")
templates = Jinja2Templates(directory="../barber_shop")

class Data(BaseModel):
    chatInput: str

@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})

@app.get('/about')
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request":request})

@app.get('/blog')
async def blog(request: Request):
    return templates.TemplateResponse("blog.html", {"request":request})

@app.get('/contact')
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request":request})

@app.get('/portfolio')
async def portfolio(request: Request):
    return templates.TemplateResponse("portfolio.html", {"request":request})

@app.get('/price')
async def price(request: Request):
    return templates.TemplateResponse("price.html", {"request":request})

@app.get('/service')
async def service(request: Request):
    return templates.TemplateResponse("service.html", {"request":request})

@app.get('/single')
async def single(request: Request):
    return templates.TemplateResponse("single.html", {"request":request})

@app.get('/team')
async def team(request: Request):
    return templates.TemplateResponse("team.html", {"request":request})

@app.post('/chat')
def startchat(data: Data):
    dict_chat = mainchatbot.chat(data.chatInput)
    return dict_chat

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)