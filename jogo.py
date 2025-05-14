# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from player import *

pygame.init()

# ----- Gera tela principal
WIDTH = 1280
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

player = Player()
game = True

while game:

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    
    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    player.draw(window)
    # Desenhando meteoro
    

    
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
