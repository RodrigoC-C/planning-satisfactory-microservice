from dataclasses import dataclass 

@dataclass
class MachineCore:
    """ The all machine of system contain the core"""
    def base(
        name: str ,
        length: int,
        width: int,
        heigth: int,
        area: int,
        ingredients: str
    ) -> None:
        
        name = name
        length = length
        width = width
        heigth = heigth 
        area = area 
        ingredients = ingredients

@dataclass
class ModuleExtracion: 
    """ Class for machine that extraction resource example Miner, wather, oli """
    def extract(
        outputs: int,
        item_minute_outputs: int
    ) -> None: 
        
        outputs = outputs
        item_minute_outputs = item_minute_outputs

@dataclass 
class ModuleCrafter:
    """ Module for all machine that crafter """
    def crafter(
        inputs: int,
        item_minute_inputs: int,
        outputs: int,
        item_minute_outputs: int
    ) -> None:
        
        inputs = inputs
        item_minute_inputs = item_minute_inputs
        outputs = outputs
        item_minute_outputs = item_minute_outputs

@dataclass
class ModuleEnergy:
    """ Module for all machine that usage energy """
    def energy(
        power_usage: int,
    ) -> None:
        
        power_usage = power_usage

@dataclass
class ModuleInventory:
    """ Module for machine that they have inventory """
    def inventory(
        inventory_size: int,
        inputs: int,
        outputs: int,
    ) -> None:
        
        inventory_size = inventory_size
        inputs = inputs
        outputs = outputs

@dataclass
class ModuleOverclock:
    """ Module of machine that has it enabled the overclock """
    def overclock(
        overclock_able: bool,
        porcent_boost: float
    ) -> None:
        
        overclock_able = overclock_able
        porcent_boost = porcent_boost

@dataclass 
class ModuleTransport:
    """ Module the machine of transport of item """
    def transport(
        item_minute = int,
    ) -> None:
        
        item_minute = item_minute