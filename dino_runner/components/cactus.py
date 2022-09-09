from dino_runner.components.obstacle import Obstacle
import random

from dino_runner.utils.constants import CACTUS_MODEL


class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        self.model = CACTUS_MODEL
        super().__init__(image, self.type)
        self.rect.y = 320

    def fly(self):
        pass
