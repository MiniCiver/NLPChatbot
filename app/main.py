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

@app.post('/chat')
def startchat(data: Data):
    dict_chat = mainchatbot.chat(data.chatInput)
    return dict_chat

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)