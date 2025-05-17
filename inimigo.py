import pygame
from config import * 
from player import *

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, inimigo_img):
        super().__init__()
        pos_inicial = (pygame.display.get_surface().get_width() - 100, pygame.display.get_surface().get_height() - 210)
        self.image = inimigo_img
        self.rect = self.image.get_rect(center = pos_inicial)
        self.velocidade_x = 5               # se move apenas em x
    
    def update(self):
        self.rect.x -= self.velocidade_x
        if self.rect.x < 0:
            self.rect.x = pygame.display.get_surface().get_width() + 100

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
         