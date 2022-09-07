import pygame

from dino_runner.components.cactus import Cactus
from dino_runner.components.pajaro import Pajaro
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import BIRD


class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
            self.obstacles.append(Pajaro(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if (game.player.dino_rec.colliderect(obstacle.rect)):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
