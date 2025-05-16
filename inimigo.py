import pygame
from config import * 
from player import Player

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, inimigo_img):
        self.inimigo_img = inimigo_img
        self.velocidade_y = 0
        # self.gravidade = 2
        # self.pulo = - 15

    def mover_em_direcao(inimigo, player, 2):
    # Posições como vetores
    pos_inimigo = pygame.math.Vector2(inimigo.rect.center)
    pos_jogador = pygame.math.Vector2(jogador.rect.center)

    # Calcula direção
    direcao = pos_jogador - pos_inimigo
    if direcao.length() != 0:
        direcao = direcao.normalize()  # Normaliza para manter velocidade constante
        movimento = direcao * velocidade
        inimigo.rect.centerx += movimento.x
        inimigo.rect.centery += movimento.y

    def draw(self, window):
        largura_tela = (pygame.display.get_surface().get_width()) - 100
        window.blit(self.inimigo_img, (largura_tela, pygame.display.get_surface().get_height() - 300))
    # def jump(self):