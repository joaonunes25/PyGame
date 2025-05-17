import pygame
from config import * 

class Player(pygame.sprite.Sprite):
    def __init__(self, player_img):
        super().__init__()
        self.image = player_img
        self.y = pygame.display.get_surface().get_height() - 300
        self.rect = pygame.Rect(100, self.y, 32, 48)
        self.velocidade_y = 0
        self.v_pulo = - 15
        self.estado = 'PARADO'
        self.pulo = False
        # self.travado_no_ar = False

        # Limita a duração do tempo de pulo
        self.duracao_pulo = 500

        # vida do player
        self.vida_max = 100
        self.vida = self.vida_max
        self.vivo = True

    def update(self):
        if self.velocidade_y < 0:
            self.gravidade = 0.5
        else:
            self.gravidade = 0.2

        self.velocidade_y += self.gravidade
        self.y += self.velocidade_y

        # if not self.travado_no_ar:
        #     self.velocidade_y += self.gravidade
        #     self.y += self.velocidade_y
        # else:
        #     self.velocidade_y = 0

        if self.y >= pygame.display.get_surface().get_height() - 300:
            self.y = pygame.display.get_surface().get_height() - 300
            self.velocidade_y = 0

        duracao_ataque = 400

        # if self.travado_no_ar:
        #     if pygame.time.get_ticks() - self.tempo_ataque >= duracao_ataque:
        #         self.travado_no_ar = False
        #         self.estado = 'PARADO'
            
        # if self.estado != "ATACANDO":
        #     self.estado = 'PARADO'
        
        if not self.vivo:
            print('morreu')

        # Verifica se o tempo de pulo já ultrapassou o limite e se o estado do player é atacando para continuar ou não o pulo
        if self.pulo:
            tempo_decorrido = pygame.time.get_ticks() - self.tempo_pulo
            if tempo_decorrido >= self.duracao_pulo:
                if self.estado != "ATACANDO":
                    self.estado = "PARADO"
                    self.pulo = False
            
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
        if not self.pulo:
            self.velocidade_y = self.v_pulo
            self.pulo = True
            self.tempo_pulo = pygame.time.get_ticks()

    def ataque(self):
        if self.estado != 'ATACANDO':
            self.estado = 'ATACANDO'
            # if self.rect.bottom <= inimigo.rect.top:
            #     self.travado_no_ar = True
            #     self.tempo_ataque = pygame.time.get_ticks()

    def desenhar_barra_de_vida(self, window):
        if self.vivo:
            l_barra = 400
            h_barra = 50
            x = 420
            y = HEIGHT 

            pygame.draw.rect(window, RED, (x, y, l_barra, h_barra))    # Desenhando a barra de vida total
            
            # Calculando a proporção vida/vida maxima
            proporcao = self.vida / self.vida_max
            l_vida = l_barra * proporcao

            pygame.draw.rect(window, GREEN, (x, y, l_vida, h_barra))    # Desenhando a barra que representa avida que o personagem de fato possui

