import pygame
from assets import fundo_vitoria_suprema
from tela_instrucoes import *
from tela_inicial import *

def tela_vitoria_suprema (window, WIDTH, HEIGHT):
    fonte_pequena = pygame.font.Font(fonte, 20)

    texto_reiniciar = fonte_pequena.render("Aperte R para reiniciar", True, (255,255,255))

    inicial = pygame.image.load(fundo_vitoria_suprema).convert_alpha()
    fundo = pygame.transform.scale(inicial, (WIDTH, HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

    # Desenhando tela
        window.blit(fundo, (0,0))
        window.blit(texto_reiniciar, (WIDTH//2 - texto_reiniciar.get_width()//2, HEIGHT - 60))
        pygame.display.update()