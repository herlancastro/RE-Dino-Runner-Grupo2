
from dino_runner.components.obstacle import Obstacle
from pygame.sprite import Sprite
from dino_runner.utils.constants import BIRD, BIRD_MODEL, DEFAULT_TYPE


class Pajaro(Obstacle, Sprite):

    def __init__(self, image):
        self.fly_img = {DEFAULT_TYPE: BIRD}
        self.type = 0
        self.model = BIRD_MODEL
        super().__init__(image, self.type)
        self.rect.y = 250
        self.rect.x = 1500
        self.step_index = 0
        # self.fly()

    def fly(self):
        self.step_index += 1
        if self.step_index == 15:
            self.type = 1
        elif self.step_index == 30:
            self.type = 0
            self.step_index = 0
