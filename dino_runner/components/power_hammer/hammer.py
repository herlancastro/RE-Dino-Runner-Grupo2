
from dino_runner.components.power_hammer.power_hammer import PowerHammer
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE

class Hammer(PowerHammer):
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super(Hammer,self).__init__(self.image, self.type)
