import pygame
from config import * 
from player import *

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, inimigo_img):
        pos_inicial = (pygame.display.get_surface().get_width() - 100, pygame.display.get_surface().get_height() - 100)
        self.inimigo_img = inimigo_img
        self.rect = self.inimigo_img.get_rect(center = pos_inicial)
        self.velocidade_x = 5    # se move apenas em x
        self.x = 5
    
    def update(self):
        self.x += self.velocidade_x

        if self.x >= pygame.display.get_surface().get_width() + 100:
            self.x = pygame.display.get_surface().get_width() + 100
            self.x = 0
            self.estado = 'PARADO'

    def mover_em_direcao(self, player,velocidade_x):
        # Posições como vetores
        self.pos = pygame.math.Vector2(self.rect.center)
        pos_player = pygame.math.Vector2(player.rect.center)

        # Calcula direção
        direcao = pos_player - self.pos
        if direcao.length() != 0:                 # Verifica se a distância entre inimigo e player é diferente de zero
            direcao = direcao.normalize()         # Normaliza para manter velocidade constante
            movimento = direcao * velocidade_x
            self.pos.rect.centerx += movimento.x
         

    def draw(self, window):
        window.blit(self.inimigo_img, (self.x, pygame.display.get_surface().get_height() - 240))
