from fastapi import FastAPI
from create_class import create, read_json
from models import MachineCore
import json 

app = FastAPI()

@app.get("/")
async def root():
    machine1 = MachineCore.from_dict(read_json())
    return machine1
