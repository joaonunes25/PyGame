# inimigo.py
import pygame
from player import *


class Inimigo(pygame.sprite.Sprite):
    def __init__(self, spritesource, num_sprites=4, tamanho_sprite=None, usar_spritesheet=True):
        super().__init__()
        self.interagiu_com_player = False
        
        if usar_spritesheet:
            self.sprites = self.carregar_spritesheet_em_lista(spritesource, num_sprites)
        else:
            self.sprites = self.carregar_sprites_de_pasta(spritesource, num_sprites, tamanho_sprite or (150, 150))

        self.index = 0
        self.image = self.sprites[self.index]
        self.rect = self.image.get_rect(center=(
            pygame.display.get_surface().get_width() - 100,
            pygame.display.get_surface().get_height() - 210
        ))

        self.velocidade_x = 5
        self.tempo_animacao = 100  # milissegundos entre frames
        self.ultimo_update = pygame.time.get_ticks()


    def carregar_spritesheet_em_lista(self, caminho, num_sprites):
        imagem = pygame.image.load(caminho).convert_alpha()
        largura_total = imagem.get_width()
        altura = imagem.get_height()
        largura_sprite = largura_total // num_sprites

        sprites = []
        for i in range(num_sprites):
            frame = imagem.subsurface((i * largura_sprite, 0, largura_sprite, altura))
            sprites.append(frame)
        return sprites
    
    """
    Carrega uma spritesheet e divide em uma lista de sprites individuais.

    Parâmetros:
        caminho (str): Caminho para a imagem da spritesheet.
        num_sprites (int): Número total de sprites na spritesheet.

    Retorna:
        list: Lista de superfícies do Pygame contendo os sprites individuais.
    """

    def carregar_sprites_de_pasta(self, caminho_base, quantidade, tamanho):
        return [
            pygame.transform.scale(
                pygame.image.load(f"{caminho_base}{i}.png").convert_alpha(),
                tamanho
            ) for i in range(1, quantidade + 1)
        ]
    
    """
    Carrega uma sequência de imagens individuais de uma pasta e redimensiona cada uma.

    Parâmetros:
        caminho_base (str): Caminho base para as imagens (ex: "sprites/img_").
        quantidade (int): Quantidade de imagens a carregar.
        tamanho (tuple): Tamanho (largura, altura) desejado para as imagens.

    Retorna:
        list: Lista de superfícies do Pygame contendo as imagens carregadas e redimensionadas.
    """

    def update(self):
        agora = pygame.time.get_ticks()
        if agora - self.ultimo_update > self.tempo_animacao:
            self.ultimo_update = agora
            self.index = (self.index + 1) % len(self.sprites)
            self.image = self.sprites[self.index]

        self.rect.x -= self.velocidade_x
        if self.rect.x < 0:
            self.rect.x = pygame.display.get_surface().get_width() + 100


    def mover_em_direcao(self, player, velocidade_x):
        self.pos = pygame.math.Vector2(self.rect.center)
        pos_player = pygame.math.Vector2(player.rect.center)
        direcao = pos_player - self.pos
        if direcao.length() != 0:
            direcao = direcao.normalize()
            movimento = direcao * velocidade_x
            self.rect.centerx += movimento.x
