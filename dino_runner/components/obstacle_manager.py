
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
            if (game.player.dino_rect.colliderect(obstacle.rect)):
                if not game.player.has_lives and not game.player.shield:
                    game.player_heart_manager.reduce_heart_count()
                    if game.player_heart_manager.heart_count > 0:
                        game.player.has_lives = True
                        self.obstacles.pop(0)
                        start_transition_times = pygame.time.get_ticks()
                        game.player.lives_transition_time = start_transition_times + 1000
                    else:
                        #self.obstacles.remove(obstacle)
                        if not game.player.shield:
                            pygame.time.delay(500)
                            game.playing = False
                            game.death_count +=1
                            break
                        else:
                            self.obstacles.remove(obstacle)
                elif game.player.shield:
                    self.obstacles.pop(0)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
