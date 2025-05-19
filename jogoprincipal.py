# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import numpy as np
from player import *
from inimigo import *

def iniciar_jogo():
    pygame.init()

    pygame.mixer.music.load("assets\snd\music\music1.mp3")
    pygame.mixer.music.play(start=4.0)

    inicio_jogo = pygame.time.get_ticks()

    WIDTH = 1280
    HEIGHT = 720
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ghost Dash")

    # Carrega camadas do fundo
    fundo1 = pygame.image.load("assets\img\_fundo1.png").convert_alpha()  # estrelas
    fundo2 = pygame.image.load("assets\img\_fundo2.png").convert_alpha()  # lua
    fundo3 = pygame.image.load("assets\img\_fundo3.png").convert_alpha()  # nuvens

    fundo1 = pygame.transform.scale(fundo1, (WIDTH, HEIGHT))
    fundo2 = pygame.transform.scale(fundo2, (1152, 648))  # lua maior
    fundo3 = pygame.transform.scale(fundo3, (WIDTH, HEIGHT))

    # Posições iniciais
    x1 = x3 = 0
    x_lua = WIDTH - 200

    def carregar_sprites(caminho_base, quantidade, tamanho=(150, 150)):  # tamanho novo
        return [
            pygame.transform.scale(
                pygame.image.load(f"{caminho_base}{i}.png").convert_alpha(), 
                tamanho
            ) for i in range(1, quantidade + 1)
        ]

    sprites_parado = carregar_sprites("assets\img\_fantasma\parado\VOANDO", 4, tamanho=(250, 250))
    sprites_pulando = carregar_sprites("assets\img\_fantasma\parado\VOANDO", 4, tamanho=(250, 250))
    sprites_atacando = carregar_sprites("assets\img\_fantasma\_atacando\_atacando", 5, tamanho=(250, 250))


    player = Player(sprites_parado, sprites_pulando, sprites_atacando)

    clock = pygame.time.Clock()
    FPS = 60000
    gp_inimigo = pygame.sprite.Group()

    batida = 1000
    v_inimigo = 300
    tempo_viagem = 500
    tempo_musica = np.arange(0, 134000 , batida)
    lista_tempo = [t - tempo_viagem for t in tempo_musica if t - tempo_viagem >= 0]
    indice_spawn = 0

    game = True
    while game:
        clock.tick(FPS)
        tempo_atual = pygame.time.get_ticks() - inicio_jogo

        while indice_spawn < len(lista_tempo) and tempo_atual >= lista_tempo[indice_spawn]:
            inimigo = Inimigo("assets\img\inimigos\_abobora.png")
            distancia = int(v_inimigo * (tempo_viagem / 1000))
            inimigo.rect.x = WIDTH + distancia
            inimigo.rect.y = random.choice([HEIGHT - 230, HEIGHT - 400])
            gp_inimigo.add(inimigo)
            indice_spawn += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_k, pygame.K_j]:
                    player.jump()
                elif event.key in [pygame.K_f, pygame.K_d]:
                    player.ataque(indice_inicio=2)

        colisao = pygame.sprite.spritecollide(player, gp_inimigo, False)
        player.update()
        gp_inimigo.update()

        if colisao:
            if player.estado != "ATACANDO":
                player.vida -= 5
                if player.vida <= 0:
                    player.vivo = False
            if player.estado == "PULANDO":
                player.ataque(indice_inicio=2)

        if not player.vivo:
            game = False

        for inimigo in colisao:
            if player.estado == "ATACANDO":
                print("Acertou")
            else:
                print("Errou")
            inimigo.kill()

        for inimigo in gp_inimigo:
            if inimigo.rect.x <= 0:
                inimigo.kill()

        # ----- Movimento dos fundos -----
        x1 -= 0.2
        x3 -= 1.2
        x_lua -= 0.3
        if x1 <= -WIDTH:
            x1 = 0
        if x3 <= -WIDTH:
            x3 = 0
        if x_lua < -fundo2.get_width():
            x_lua = WIDTH

        # ----- Desenho dos fundos -----
        window.blit(fundo1, (x1, 0))
        window.blit(fundo1, (x1 + WIDTH, 0))

        window.blit(fundo2, (x_lua, 80))

        window.blit(fundo3, (x3, 0))
        window.blit(fundo3, (x3 + WIDTH, 0))

        player.draw(window)
        gp_inimigo.draw(window)

        pygame.display.update()

    pygame.quit()