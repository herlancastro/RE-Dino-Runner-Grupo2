import pygame
import random


from dino_runner.components.power_hammer.hammer import Hammer

class PowerHammerManager:
    def __init__(self):
        self.power_hammer=[] 
        self.when_appears = 0
        self.points = 0
        self.option_number = list(range(1,10)) 

    def reset_power_hammer(self, points):
        self.power_hammer=[]   
        self.points = points
        self.when_appears = random.randint(200,300)+self.points
    def generate_power_hammer(self, points):
        self.points = points
        if len(self.power_hammer) ==0:
            if self.when_appears == self.points:
                print("generating  powerHammer")
                self.when_appears = random.randint(self.when_appears +200 , 500 + self.when_appears)
                self.power_hammer.append(Hammer())
        return self.power_hammer


    def update(self, points, game_speed, player):
        self.generate_power_hammer(points)
        for power_hammer in self.power_hammer:
            power_hammer.update(game_speed, self.power_hammer)
            if(player.dino_rect.colliderect(power_hammer.rect)):
                escudo = pygame.mixer.Sound("dino_runner/Sound/estrella.mp3")
                pygame.mixer.Sound.play(escudo)
                power_hammer.start_time = pygame.time.get_ticks()
                player.hammer = True
                player.show_text = True 
                player.type = power_hammer.type
                power_hammer.start_time = pygame.time.get_ticks()
                time_random = random.randrange(6,9)
                player.hammer_time_hammer = power_hammer.start_time + (time_random * 1000)
                self.power_hammer.remove(power_hammer)

    def draw(self, screen):
        for power_hammer in self.power_hammer:
            power_hammer.draw(screen)  