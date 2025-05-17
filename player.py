import pygame
from config import * 

class Player(pygame.sprite.Sprite):
    def __init__(self, player_img):
        super().__init__()
        self.image = player_img
        self.y = pygame.display.get_surface().get_height() - 300
        self.rect = pygame.Rect(100, self.y, 32, 48)
        self.velocidade_y = 0
        self.gravidade = 2
        self.pulo = - 30
        self.estado = 'PARADO'

        self.tempo_ataque = 0
        self.duracao_ataque = 1000

        # vida do player
        self.vida_max = 100
        self.vida = self.vida_max
        self.vivo = True

    def update(self):
        self.velocidade_y += self.gravidade
        self.y += self.velocidade_y

        if self.y >= pygame.display.get_surface().get_height() - 300:
            self.y = pygame.display.get_surface().get_height() - 300
            self.velocidade_y = 0
            
        if self.estado != "ATACANDO":
            self.estado = 'PARADO'
        
        if not self.vivo:
            print('morreu')
            
        # Centralizando o rect no player para detectar a colisão corretamente (código sugerido pelo Chat GPT)
        offset_x = 100 + (self.image.get_width() // 2) - (self.rect.width // 2)
        offset_y = self.y + (self.image.get_height() // 2) - (self.rect.height // 2)
        self.rect.topleft = (offset_x, offset_y)
        # --------------------------------------------------------------------------------------------------

    def draw(self, window):
        if self.vivo:
            window.blit(self.image, (100, self.y))
        else:
            pass

        self.desenhar_barra_de_vida(window)

    def jump(self):
        if self.estado == 'PARADO':
            self.velocidade_y = self.pulo
            self.estado = 'PULANDO'

    def ataque(self):
        if self.estado != 'ATACANDO':
            self.estado = 'ATACANDO'
            self.tempo_ataque = pygame.time.get_ticks ()

    def desenhar_barra_de_vida(self, window):
        if self.vivo:
            l_barra = 200
            h_barra = 40
            x = 40
            y = HEIGHT 

            pygame.draw.rect(window, RED, (x, y, l_barra, h_barra))    # Desenhando a barra de vida total
            
            # calculando a proporção vida/vida maxima
            proporcao = self.vida / self.vida_max
            l_vida = l_barra * proporcao

            pygame.draw.rect(window, GREEN, (x, y, l_vida, h_barra))    # Desenhando a barra que representa avida que o personagem de fato possui

