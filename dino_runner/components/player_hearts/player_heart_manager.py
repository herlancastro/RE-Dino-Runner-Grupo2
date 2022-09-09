import pygame
from dino_runner.components.player_hearts.heart import Heart

class PlayerHeartManager:
    def __init__(self):
        self.heart_count = 5

    def reduce_heart_count(self):
        self.heart_count -= 1
        if self.heart_count == 1:
            pygame.mixer.pause()
            sonido_muerte = pygame.mixer.Sound("dino_runner/Sound/dark.mp3")
            pygame.mixer.Sound.play(sonido_muerte)
        if self.heart_count == 0:
            pygame.mixer.pause()
            sonido_muerte = pygame.mixer.Sound("dino_runner/Sound/muerte.mp3")
            pygame.mixer.Sound.play(sonido_muerte)

            

    def draw(self, screen):
        x_position = 10
        y_position = 20

        for counter in range(self.heart_count):
            heart = Heart(x_position,y_position)
            heart.draw(screen)
            x_position += 30