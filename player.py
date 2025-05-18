import pygame
from config import * 

class Player(pygame.sprite.Sprite):

    def __init__(self, sprites_parado, sprites_pulando, sprites_atacando):
        super().__init__()
        self.sprites_por_estado = {
            'PARADO': sprites_parado,
            'PULANDO': sprites_pulando,
            'ATACANDO': sprites_atacando
        }

        self.estado = 'PARADO'
        self.sprites = self.sprites_por_estado[self.estado]
        self.index = 0
        self.image = self.sprites[self.index]

        self.y = pygame.display.get_surface().get_height() - 300
        self.rect = pygame.Rect(100, self.y, 32, 48)
        self.velocidade_y = 0
        self.v_pulo = -15
        self.pulo = False
        self.no_chao = True

        self.duracao_pulo = 500
        self.vida_max = 100
        self.vida = self.vida_max
        self.vivo = True

        self.tempo_animacao = 70
        self.ultimo_update = pygame.time.get_ticks()

        for estado, sprites in self.sprites_por_estado.items():
            for i, img in enumerate(sprites):
                if img.get_width() == 0 or img.get_height() == 0:
                    print(f" Imagem vazia em {estado} - índice {i}")
                else:
                    print(f" Sprite {estado}[{i}] OK: {img.get_width()}x{img.get_height()}")

    def animar(self):
        nova_spritesheet = self.sprites_por_estado[self.estado]
        if nova_spritesheet != self.sprites:
            self.sprites = nova_spritesheet
            self.index = 0

        agora = pygame.time.get_ticks()
        if agora - self.ultimo_update > self.tempo_animacao:
            self.ultimo_update = agora
            self.index += 1
            if self.index >= len(self.sprites):
                if self.estado == "ATACANDO":
                    self.estado = "PULANDO" if self.pulo else "PARADO"
                self.index = 0
            self.image = self.sprites[self.index]

    def update(self):
        self.animar()

        # Aumenta a gravidade para cair mais rápido
        self.gravidade = 1.2 if self.velocidade_y >= 0 else 0.5
        self.velocidade_y += self.gravidade
        self.y += self.velocidade_y

        if self.y >= pygame.display.get_surface().get_height() - 300:
            self.y = pygame.display.get_surface().get_height() - 300
            self.velocidade_y = 0
            self.pulo = False
            self.no_chao = True
            if self.estado != "ATACANDO":
                self.estado = "PARADO"
        else:
            self.no_chao = False

        if self.pulo:
            tempo_decorrido = pygame.time.get_ticks() - self.tempo_pulo
            if tempo_decorrido >= self.duracao_pulo and self.estado != "ATACANDO":
                self.estado = "PARADO"
                self.pulo = False

        offset_x = 100 + (self.image.get_width() // 2) - (self.rect.width // 2)
        offset_y = self.y + (self.image.get_height() // 2) - (self.rect.height // 2)
        self.rect.topleft = (offset_x, offset_y)

        if not self.vivo:
            print('morreu')

    def draw(self, window):
        if self.vivo:
            window.blit(self.image, (100, self.y))
            self.desenhar_barra_de_vida(window)

    def jump(self):
        if self.no_chao:  # só permite pular se estiver no chão
            self.velocidade_y = self.v_pulo
            self.pulo = True
            self.no_chao = False
            self.tempo_pulo = pygame.time.get_ticks()
            self.estado = "PULANDO"

    def ataque(self, indice_inicio=0):
        if self.estado != 'ATACANDO':
            self.estado = 'ATACANDO'
            self.sprites = self.sprites_por_estado['ATACANDO']
        self.index = indice_inicio
        self.ultimo_update = pygame.time.get_ticks()

    def desenhar_barra_de_vida(self, window):
        if self.vivo:
            l_barra = 400
            h_barra = 50
            x = 420
            y = HEIGHT

            pygame.draw.rect(window, RED, (x, y, l_barra, h_barra))
            proporcao = self.vida / self.vida_max
            l_vida = l_barra * proporcao
            pygame.draw.rect(window, GREEN, (x, y, l_vida, h_barra))