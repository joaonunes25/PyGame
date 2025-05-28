import pygame
from assets import *

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
        self.v_pulo = -18
        self.pulo = False
        self.no_chao = True

        self.duracao_pulo = 500
        self.vida_max = 100
        self.vida = self.vida_max
        self.vivo = True

        self.tempo_animacao = 70
        self.ultimo_update = pygame.time.get_ticks()


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
    """
    Atualiza a animação do objeto com base no estado atual.

    Esta função gerencia a troca de sprites de animação com base no tempo e no estado do personagem,
    como "PARADO", "PULANDO" ou "ATACANDO".

    Funcionamento:
    1. Verifica se o estado (`self.estado`) mudou e, se sim, carrega a nova spritesheet correspondente,
       reiniciando o índice de animação (`self.index`).
    2. Verifica se já se passou tempo suficiente desde a última atualização com base em `self.tempo_animacao`.
    3. Se sim, avança para o próximo frame da animação.
    4. Quando chega ao fim da sequência de sprites:
       - Se o estado atual for "ATACANDO", muda para "PULANDO" (caso esteja no ar) ou "PARADO".
       - Reinicia o índice da animação.
    5. Atualiza a imagem atual do objeto (`self.image`) com o frame correspondente da lista `self.sprites`.

    Requisitos:
    - `self.sprites_por_estado`: dicionário com listas de sprites para cada estado.
    - `self.estado`: estado atual do personagem.
    - `self.tempo_animacao`: intervalo entre atualizações de frames.
    - `self.pulo`: booleano indicando se o personagem está no ar.
    """

    def update(self):
        self.animar()
        # Aumenta a gravidade para cair mais rápido
        if self.velocidade_y >= 0:
            self.gravidade = 1
        else:
            self.gravidade = 0.8
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

        # Centralizando o rect no player para detectar a colisão corretamente (código sugerido pelo Chat GPT)
        offset_x = 100 + (self.image.get_width() // 2) - (self.rect.width // 2)
        offset_y = self.y + (self.image.get_height() // 2) - (self.rect.height // 2)
        self.rect.topleft = (offset_x, offset_y)


        if not self.vivo:
            print('morreu')
    ''' Atualiza o estado do player no loop principal'''
    

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
            y = HEIGHT - 100
            # Desenha a barra de vida total
            pygame.draw.rect(window, (255,0,0), (x, y, l_barra, h_barra))
            # Calcula a proporção vida/vida total
            proporcao = self.vida / self.vida_max
            l_vida = l_barra * proporcao
            # Desenha a vida atual do player
            pygame.draw.rect(window, (0,255,0), (x, y, l_vida, h_barra))