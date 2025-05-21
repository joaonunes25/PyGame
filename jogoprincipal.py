import pygame
import random
import numpy as np
from player import *
from inimigo import *
from tela_game_over import *
from assets import *

def iniciar_jogo():
    pygame.init()

    pygame.mixer.music.load(snd1)
    pygame.mixer.music.play()

    inicio_jogo = pygame.time.get_ticks()

    WIDTH = 1280
    HEIGHT = 720
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ghost Dash")

    # Posições iniciais
    x1 = x3 = 0
    x_lua = WIDTH - 200

    sprites_parado = carregar_sprites(fantasma_voando, 4, tamanho=(250, 250))
    sprites_pulando = carregar_sprites(fantasma_pulo, 4, tamanho=(250, 250))
    sprites_atacando = carregar_sprites(fantasma_ataque, 5, tamanho=(250, 250))

    player = Player(sprites_parado, sprites_pulando, sprites_atacando)

    clock = pygame.time.Clock()
    FPS = 60

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
            inimigo = Inimigo(inimigo_abobora)
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
            if player.estado == "PULANDO":
                player.ataque(indice_inicio=2)

            if player.estado != "ATACANDO":
                player.vida -= 5
                if player.vida <= 0:
                    player.vivo = False
            
        if not player.vivo:
            pygame.mixer.music.stop()
            tela_game_over(window, WIDTH, HEIGHT)
            iniciar_jogo()

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