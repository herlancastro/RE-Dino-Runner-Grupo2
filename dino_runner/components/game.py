import pygame

from dino_runner.components.obstacle_manager import ObstacleManager
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager
from dino_runner.components.power_up.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, JUMPING, DEFAULT_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components import text_utils
from dino_runner.components.text_utils import get_score_element


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        #self.old_position = 0
        #self.is_jumping = False
        self.player_heart_manager = PlayerHeartManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.death_count =0
        self.running = True

    def run(self):
        # self.saltar()
        # Game loop: events - update - draw
        sonido_fondo = pygame.mixer.Sound("dino_runner/Sound/principal.wav")
        pygame.mixer.Sound.play(sonido_fondo)
        self.create_comment()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        # pygame.quit()
    def create_comment(self):
        self.power_up_manager.reset_power_ups(self.points)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_UP:
        #             self.old_position = self.x_pos_bg
        #             self.player.Y_POS -= 90
        #             self.is_jumping = True
        # if self.x_pos_bg == (self.old_position - 260) and self.is_jumping == True:
        #     self.player.Y_POS += 90
        #     self.is_jumping = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.power_up_manager.update(self.points,self.game_speed,self.player)
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.player_heart_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.score()
        self.running = True
        self.player.check_lives()

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def score(self):
        self.points += 1
        score, score_rect = text_utils.get_score_element(self.points)
        self.screen.blit(score,score_rect)
        self.player.check_visibility(self.screen)

    def show_menu(self,death_count=0):
        self.running = True
        white_color = (255,255,255)
        self.screen.fill(white_color)
        self.print_menu_elements(death_count)
        pygame.display.update()
        self.headle_key_events_on_menu()
    
    def print_menu_elements(self,death_count=0):
        half_screen_hegth = SCREEN_HEIGHT//2
        if death_count == 0:
            text, text_rect = text_utils.get_centered_message("Press my Key to Start")
            self.screen.blit(text,text_rect)
        elif death_count > 0:
            text, text_rect = text_utils.get_centered_message("Press my Key to Start")
            score, score_rect = text_utils.get_centered_message("Your Score "+ str(self.points),height = half_screen_hegth +50)
            self.screen.blit(text,text_rect)
            self.screen.blit(score,score_rect)

    def headle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()

            if  event.type == pygame.KEYDOWN:
                self.run()

