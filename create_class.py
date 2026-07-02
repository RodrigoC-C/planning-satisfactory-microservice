from models import MachineCore
import json 

# This fuction is for read and open json, the call of api
def read_json():
    with open('contract.json','r', encoding='utf-8') as archivo:
        datos = json.load(archivo)

    return datos

# This fuction is for create class whit data json and complement by class for graph
def create_class():
    read_json = read_json()
    machine = MachineCore()
# Create lecture of json whit class base and component
