from dataclasses import dataclass 
from typing import Optional

@dataclass
class ModuleExtraction: 
    """ Class for machine that extraction resource example Miner, wather, oli """
    outputs: int
    item_minute_outputs: int

@dataclass 
class ModuleCrafter:
    """ Module for all machine that crafter """
    inputs: int
    item_minute_inputs: int
    outputs: int
    item_minute_outputs: int

@dataclass
class ModuleEnergy:
    """ Module for all machine that usage energy """
    power_usage: int

@dataclass
class ModuleInventory:
    """ Module for machine that they have inventory """
    inventory_size: int
    inputs: int
    outputs: int


@dataclass
class ModuleOverclock:
    """ Module of machine that has it enabled the overclock """
    overclock_able: bool
    porcent_boost: float


@dataclass 
class ModuleTransport:
    """ Module the machine of transport of item """
    item_minute: int

@dataclass
class Conection():
    source_id: int
    target_id: int 

    # This variable is optional
    transport: Optional[ModuleTransport]


@dataclass
class MachineCore:
    """ The all machine of system contain the core"""
    id_machine: str
    name: str 
    length: int
    width: int
    heigth: int
    area: int
    ingredients: str

    # The modules these optinal the base machine

    extraction: Optional[ModuleExtraction]
    crafter: Optional[ModuleCrafter]
    energy: Optional[ModuleEnergy]
    inventory: Optional[ModuleInventory]
    overclock: Optional[ModuleOverclock]
