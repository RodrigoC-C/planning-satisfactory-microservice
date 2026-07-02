from fastapi import FastAPI
from create_class import read_json

app = FastAPI()

@app.get("/")
async def root():
    read = read_json()

    return read