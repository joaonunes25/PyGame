import pygame
from config import * 


class Player(pygame.sprite.Sprite):
    def __init__(self, player_img):
        self.player_img = player_img #pygame.Rect(0, pygame.display.get_surface().get_height()- 300, 100, 100)
        self.velocidade_y = 0
        # self.gravidade = 2
        # self.pulo = - 15

    def draw(self, window):
        window.blit(self.player_img, (0, pygame.display.get_surface().get_height() - 300))

    # def jump(self):

