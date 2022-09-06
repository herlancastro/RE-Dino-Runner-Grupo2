
from mimetypes import init
from turtle import Screen
import pygame

from dino_runner.utils.constants import RUNNING

class Dinosaur():
    X_POS = 80
    Y_POS = 310
    pass

    def __init__(self) ->None:
        self.image = RUNNING[0]
        self.dino_rec =self.image.get_rect()

        #Definiendo la posicion del dino
        self.dino_rec.x =self.X_POS
        self.dino_rec.y =self.Y_POS


    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rec.x,self.dino_rec.y))
        

    def run(self):
        self.image =RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rec = self.image.get_rect()

        self.dino_rec.x  =self.X_POS
        self.dino_rec.y  =self.Y_POS
        
        self.stop_index +=1