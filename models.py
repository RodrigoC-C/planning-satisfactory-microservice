from dataclasses import dataclass, field 
from typing import Optional


@dataclass
class ModuleExtraction: 
    """ Class for machine that extraction resource example Miner, wather, oli """
    outputs: int
    item_minute_outputs: int

    # This method is base for create class for component
    @classmethod
    def from_dict(cls, data: dict) -> "ModuleExtraction":
        return cls(
            outputs = data["outputs"],
            item_minute_outputs = data["item_minute_outputs"]
        )

@dataclass 
class ModuleCrafter:
    """ Module for all machine that crafter """
    inputs: int
    item_minute_inputs: int
    outputs: int
    item_minute_outputs: int

    # This method is base for create class for component
    @classmethod
    def from_dict(cls, data: dict) -> "ModuleCrafter":
        return cls(
            inputs = data["inputs"],
            item_minute_inputs = data["item_minute_inputs"],
            outputs = data["outputs"],
            item_minute_outputs = data["item_minute_outputs"]
        )
    
@dataclass
class ModuleEnergy:
    """ Module for all machine that usage energy """
    power_usage: int

    # This method is base for create class for component
    @classmethod
    def from_dict(cls, data: dict) -> "ModuleEnergy":
        return cls(
            power_usage = data["power_usage"]
        )

@dataclass
class ModuleInventory:
    """ Module for machine that they have inventory """
    inventory_size: int
    inputs: int
    outputs: int

    # This method is base for create class for component
    @classmethod
    def from_dict(cls, data: dict) -> "ModuleInventory":
        return cls(
            inventory = data["inventory_size"],
            inputs = data["inputs"],
            outputs = data["outputs"]
        )

@dataclass
class ModuleOverclock:
    """ Module of machine that has it enabled the overclock """
    overclock_able: bool
    porcent_boost: float

    # This method is base for create class for component
    @classmethod
    def from_dict(cls, data: dict) -> "ModuleOverclock":
        return cls(
            overclock_able = data["overclock_able"],
            porcent_boost = data["porcent_boost"]
        )

@dataclass 
class ModuleTransport:
    """ Module the machine of transport of item """
    item_minute: int

    # This method is base for create class for component
    @classmethod
    def from_dict(cls, data: dict) -> "ModuleTransport":
        return cls(
            item_minute = data["item_minute"]
        )

@dataclass
class Conection:
    source_id: int
    target_id: int 

    # This variable is optional
    transport: Optional[ModuleTransport]

    # This method is base for create class for component
    @classmethod 
    def from_dict(cls, data: dict) -> "Conection":
        # get of json data transport
        json_transport = data.get('transport')
        # pass each one to function from_dict for create class module
        module_transport = ModuleTransport.from_dict(json_transport) if json_transport else None

        return cls(
            source_id = data["source_id"],
            target_id = data["target_id"],
            #Optional
            transport = module_transport
        )



@dataclass
class MachineCore:
    """ The all machine of system contain the core"""
    id_machine: str
    name: str 
    length: int
    width: int
    heigth: int
    area: int
    ingredients: list[str] = field(default_factory=list) # The field(default_factory=list) is for create one new list for each one class new 

    # The modules these optinal the base machine
    extraction: Optional[ModuleExtraction] = None 
    crafter: Optional[ModuleCrafter] = None
    energy: Optional[ModuleEnergy] = None
    inventory: Optional[ModuleInventory] = None
    overclock: Optional[ModuleOverclock] = None

    # This method is base for create class for component
    @classmethod
    def from_dict(cls, data: dict) -> "MachineCore":
        # search package exact on json, for each one module optional(Component)
        json_extraction = data.get('extraction')
        json_crafter = data.get('crafter')
        json_energy = data.get('energy')
        json_inventory = data.get('inventory')
        json_overclock = data.get('overclock')

        # Pass each one module optional to funtion of creation 
        module_extraction = ModuleExtraction.from_dict(json_extraction) if json_extraction else None 
        module_crafter = ModuleCrafter.from_dict(json_crafter) if json_crafter else None
        module_energy = ModuleEnergy.from_dict(json_energy) if json_energy else None
        module_inventory = ModuleInventory.from_dict(json_inventory) if json_inventory else None
        module_overclock = ModuleOverclock.from_dict(json_overclock) if json_overclock else None

        return cls(
            id_machine = data["id_machine"],
            name = data["name"],
            length = data["length"],
            width = data["width"],
            heigth = data["heigth"],
            area = data["area"],
            ingredients = data["ingredients"],
            # Optionals
            extraction = module_extraction,
            crafter = module_crafter,
            energy = module_energy,
            inventory = module_inventory,
            overclock = module_overclock
        )