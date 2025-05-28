import pygame
from assets import fundo_vitoria_suprema
from tela_instrucoes import *

def tela_vitoria_suprema (window, WIDTH, HEIGHT):

    inicial = pygame.image.load(fundo_vitoria_suprema).convert_alpha()
    fundo = pygame.transform.scale(inicial, (WIDTH, HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

    # Desenhando tela
        window.blit(fundo, (0,0))
        pygame.display.update()