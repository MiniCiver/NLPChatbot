from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data':{'name':'You'}}

@app.get('/about')
def about():
    return {'data':{'name':'Me'}}