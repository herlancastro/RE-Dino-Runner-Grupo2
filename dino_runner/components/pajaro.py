
from dino_runner.components.obstacle import Obstacle
import random

from dino_runner.utils.constants import BIRD


class Pajaro(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 250
        self.rect.x = 1500
        self.bird_fly = True
        self.step_index = 0

    def move(self):
        if self.bird_fly:
            self.fly()
        if self.step_index >= 10:
            self.step_index = 0

    def fly(self):
        self.image =BIRD[0] if self.step_index < 5 else BIRD[1]
        self.bird_fly = self.image.get_rect()
        self.step_index +=1