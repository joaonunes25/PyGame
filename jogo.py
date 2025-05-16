# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from player import *
from inimigo import *


pygame.init()

# ----- Gera tela principal
WIDTH = 1280
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

player_img = pygame.image.load('assets\img\_fantasma1.png').convert_alpha()
inimigo_img = pygame.image.load('assets\img\meteorBrown_med1.png').convert_alpha()  

player = Player(player_img)
inimigo = Inimigo(inimigo_img)
game = True
clock = pygame.time.Clock()
FPS = 60

while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    inimigo.draw(window)
    player.draw(window)
    player.update()
    inimigo.update()
    
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
