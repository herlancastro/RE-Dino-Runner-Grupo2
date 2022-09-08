from dino_runner.components.player_hearts.heart import Heart
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.components.cactus import Cactus

class PlayerHeartManager:
    def __init__(self):
        self.heart_count = 5
    def reduce_heart_count(self):
        self.obstacles.append(Cactus(SMALL_CACTUS))

    def draw(self, screen):
        x_position = 10
        y_position = 20

        for counter in range(self.heart_count):
            heart = Heart(x_position,y_position)
            heart.draw(screen)
            x_position += 30