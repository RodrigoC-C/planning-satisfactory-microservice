from models import MachineCore
import json 

# This fuction is for read and open json, the call of api
def read_json() -> dict:
    with open('contract.json','r', encoding='utf-8') as archivo:
        datos = json.load(archivo)

    return datos

# This fuction is for create class whit data json and complement by class for graph
def create():
    read = read_json()
    
    machine = MachineCore.from_dict(read_json)
    return machine


