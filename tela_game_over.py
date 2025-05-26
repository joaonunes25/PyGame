import pygame
from assets import *

WIDTH = 1280
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

def tela_game_over(window, WIDTH, HEIGHT):
    fonte_grande = pygame.font.Font(fonte, 50)
    fonte_pequena = pygame.font.Font(fonte, 20)

    texto_gameover = fonte_grande.render("Você morreu!", True, (255, 255, 255))
    texto_reiniciar = fonte_pequena.render("Pressione R para reiniciar ou ESC para sair", True, (255,255,255))

    gameover = pygame.image.load(fundo_gameover).convert_alpha()
    fundo = pygame.transform.scale(gameover, (WIDTH, HEIGHT))

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

        window.blit(fundo, (0,0))
        window.blit(texto_gameover, (WIDTH//2 - texto_gameover.get_width()//2, 70))
        window.blit(texto_reiniciar, (WIDTH//2 - texto_reiniciar.get_width()//2, HEIGHT - 60))

        pygame.display.update()