import pygame
from assets import *

def tela_instrucoes (window, WIDTH, HEIGHT):
    fonte_grande = pygame.font.Font(fonte, 50)
    fonte_pequena = pygame.font.Font(fonte, 20)

    texto_iniciar2 = fonte_pequena.render("Aperte SPACE para voltar", True, (255,255,255))

    inicial = pygame.image.load(fundo_instrucoes).convert_alpha()
    fundo = pygame.transform.scale(inicial, (WIDTH, HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        window.blit(fundo, (0,0))
        window.blit(texto_iniciar2, (WIDTH//2 - texto_iniciar2.get_width()//2, HEIGHT - 30))

        pygame.display.update()