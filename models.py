class MachineBase: 
    """ Class father for all it machine in this sistem """
    def __init__(
        self,
        name,
        length,
        width,
        height,
        area,
        ingredients
    ) -> None:

        self.name = name
        self.lenght = length
        self.width = width
        self.heigth = heigth
        self.area = area
        self.ingredients = ingredients


class MachineProduction(MachineBase):
    """ Machine Production base on factory """
    def __init__(
        self,
        power_usage,
        inputs,
        outputs,
        overclocker_able
    ) -> None:

        super().__init__(
            name,
            length,
            width,
            heigth,
            area,
            ingredients
        )

        self.power_usage = power_usage
        self.inputs = inputs
        self.outputs = outputs
        self.overclocker_able = overclocker_able

class MachineLogistic(MachineBase):
    """ This class is indispensable? """
    def __init__(
        self,
        item_min
    ) -> None:

        super().__init__(
            name
        )
        self.item_min = item_min


