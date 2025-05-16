from fastapi import FastAPI

app = FastAPI(
    title="FastAPI",
    version="0.0.1",
)

@app.get('/')
@app.get('/index')
@app.get('/index.html')
async def index():
    return {"message":"Hello World!"}
