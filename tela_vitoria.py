import pygame
from assets import *
from tela_instrucoes import *

def tela_vitoria (window, WIDTH, HEIGHT):
    fonte_grande = pygame.font.Font(fonte, 50)
    fonte_pequena = pygame.font.Font(fonte, 20)

    # texto_jogo = fonte_grande.render("Você venceu!", True, (255, 255, 255))
    texto_iniciar = fonte_pequena.render("Aperte SPACE para entrar na próxima fase", True, (255,255,255))

    inicial = pygame.image.load(fundo_vitoria).convert_alpha()
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
        # window.blit(texto_jogo, (WIDTH//2 - texto_jogo.get_width()//2, 70))
        window.blit(texto_iniciar, (WIDTH//2 - texto_iniciar.get_width()//2, HEIGHT - 60))

        pygame.display.update()