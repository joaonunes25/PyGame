import pygame
from config import * 

class Player(pygame.sprite.Sprite):
    def __init__(self, player_img):
        # self.player_img = player_img 
        self.image = player_img
        self.y = pygame.display.get_surface().get_height() - 300
        self.rect = pygame.Rect(100, self.y, 32, 48)
        self.velocidade_y = 0
        self.gravidade = 2
        self.pulo = - 30
        self.estado = 'PARADO'

        self.tempo_ataque = 0
        self.duracao_ataque = 1000

    def update(self):
        self.velocidade_y += self.gravidade
        self.y += self.velocidade_y

        if self.y >= pygame.display.get_surface().get_height() - 300:
            self.y = pygame.display.get_surface().get_height() - 300
            self.velocidade_y = 0
            
        if self.estado != "ATACANDO":
            self.estado = 'PARADO'
            
        # Centralizando o rect no player para detectar a colisão corretamente (código sugerido pelo Chat GPT)
        offset_x = 100 + (self.image.get_width() // 2) - (self.rect.width // 2)
        offset_y = self.y + (self.image.get_height() // 2) - (self.rect.height // 2)
        self.rect.topleft = (offset_x, offset_y)
        # --------------------------------------------------------------------------------------------------

    def draw(self, window):
        window.blit(self.image, (100, self.y))

    def jump(self):
        if self.estado == 'PARADO':
            self.velocidade_y = self.pulo
            self.estado = 'PULANDO'

    def ataque(self):
        # if self.estado != 'ATACANDO':
        self.estado = 'ATACANDO'
            # self.tempo_ataque = pygame.time.get_ticks ()
