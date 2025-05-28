import pygame
from assets import *

def tela_inicial (window, WIDTH, HEIGHT):
    tela_atual = 0 
    fonte_grande = pygame.font.Font(fonte, 50)
    fonte_pequena = pygame.font.Font(fonte, 20)

    texto_jogo = fonte_grande.render("Ghost Dash", True, (255, 255, 255))
    texto_iniciar = fonte_pequena.render("Aperte SPACE para jogar", True, (255,255,255))

    inicial = pygame.image.load(fundo_inicial).convert_alpha()
    fundo = pygame.transform.scale(inicial, (WIDTH, HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        window.blit(fundo, (0,0))
        window.blit(texto_jogo, (WIDTH//2 - texto_jogo.get_width()//2, 70))
        window.blit(texto_iniciar, (WIDTH//2 - texto_iniciar.get_width()//2, HEIGHT - 60))

        pygame.display.update()