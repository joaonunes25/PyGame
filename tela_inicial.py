import pygame
from assets import *
from tela_instrucoes import *

def tela_inicial(window, WIDTH, HEIGHT):
    # Carregando fontes
    fonte_grande = pygame.font.Font(fonte, 50)
    fonte_pequena = pygame.font.Font(fonte, 20)
    # fonte_input = pygame.font.Font(fonte, 20)

    # Textos
    texto_jogo = fonte_grande.render("Ghost Dash", True, (255, 255, 255))
    texto_iniciar = fonte_pequena.render("Aerte SPACE para instruções ou ENTER para jogar", True, (255,255,255))

    # Imagens
    inicial = pygame.image.load(fundo_inicial).convert_alpha()
    fundo = pygame.transform.scale(inicial, (WIDTH, HEIGHT))

    # Player
    ativo = True
    cor_input = (255,255,255)
    input_box = pygame.Rect(WIDTH//2 - 150, HEIGHT//2, 300, 40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if ativo:
                    if event.key == pygame.K_RETURN:
                        # return nome  # retorna o nome digitado
                        return
                    elif event.key == pygame.K_SPACE:
                        tela_instrucoes(window, WIDTH, HEIGHT)
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                    # elif event.key == pygame.K_BACKSPACE:
                    #     nome = nome[:-1]
                    # else:
                    #     if len(nome) < 20:  # limite de caracteres
                    #         nome += event.unicode

    # Desenhando tela
        window.blit(fundo, (0,0))
        window.blit(texto_jogo, (WIDTH//2 - texto_jogo.get_width()//2, 70))
        window.blit(texto_iniciar, (WIDTH//2 - texto_iniciar.get_width()//2, HEIGHT - 60))

        # pygame.draw.rect(window, cor_input, input_box, 2)
        # texto_nome = fonte_input.render(nome, True, (255, 255, 255))
        # window.blit(texto_nome, (input_box.x + 10, input_box.y + 5))

        pygame.display.update()
