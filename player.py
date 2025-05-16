import pygame
from config import * 

class Player(pygame.sprite.Sprite):
    def __init__(self, player_img):
        self.player_img = player_img 
        self.velocidade_y = 0
        self.gravidade = 1
        self.pulo = - 15
        self.estado = 'PARADO'
        self.y = 0

        self.tempo_ataque = 0
        self.duracao_ataque = 1000

        self.rect = self.player_img.get_rect()

    def update(self):
        self.velocidade_y += self.gravidade
        self.y += self.velocidade_y

        if self.y >= pygame.display.get_surface().get_height() - 300:
            self.y = pygame.display.get_surface().get_height() - 300
            self.velocidade_y = 0
            self.estado = 'PARADO'

    def draw(self, window):
        window.blit(self.player_img, (100, self.y))

    def jump(self):
        if self.estado == 'PARADO':
            self.velocidade_y = self.pulo
            self.estado = 'PULANDO'

    def ataque(self):
        if self.estado != 'ATACANDO':
            self.estado = 'ATACANDO'
            self.tempo_ataque = pygame.time.get_ticks
