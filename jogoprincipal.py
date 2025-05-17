# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import numpy as np
from player import *
from inimigo import *
# from niveis import *

def iniciar_jogo():
    pygame.init()

    pygame.mixer.music.load("assets\snd\we will rock you.mp3")
    pygame.mixer.music.play(start= 4.0)

    inicio_jogo = pygame.time.get_ticks()

    # ----- Gera tela principal
    WIDTH = 1280
    HEIGHT = 720
    window = pygame.display.set_mode((WIDTH, HEIGHT)) 
    pygame.display.set_caption("Ghost Dash")

    fundo_img = pygame.image.load("assets\img\moon_background.jpeg").convert_alpha()
    fundo_img = pygame.transform.scale(fundo_img, (WIDTH,HEIGHT))

    player_img = pygame.image.load('assets\img\_fantasma1.png').convert_alpha()
    inimigo_img = pygame.image.load('assets\img\meteorBrown_med1.png').convert_alpha()   

    player = Player(player_img)
    # inimigo = Inimigo(inimigo_img)

    clock = pygame.time.Clock()
    FPS = 60

    gp_inimigo = pygame.sprite.Group()

    # nivel teste: We will rock you ----------------------------------------------------------------------------

    batida = 1000   # 80 BPM -> 1 batida a cada 750 ms
    # atraso = 4000  
    v_inimigo = 300
    tempo_viagem = 500    # viagem até o player

    tempo_musica = np.arange(0, 134000 , batida) # ms
    lista_tempo = []

    for i in (tempo_musica):
        t = i - tempo_viagem               # cria o inimigo antes para que ele chegue no tempo correto ao player
        if t >= 0:
            lista_tempo.append(t)    

    indice_spawn = 0
    #--------------------------------------------------------------------------

    game = True

    while game:
        clock.tick(FPS)

        tempo_atual = pygame.time.get_ticks() - inicio_jogo

        # Sugerido pelo Chat GPT -> Verificação se o momento de spawnar um inimigo está correto

        while indice_spawn< len(lista_tempo) and tempo_atual >= lista_tempo[indice_spawn]:
            inimigo = Inimigo(inimigo_img)

            # Cálculo da distância para ele chegar no player exatamente em tempo_viagem
            distancia = int(v_inimigo * (tempo_viagem / 1000))
            inimigo.rect.x = WIDTH + distancia

            # Posições verticais possíveis
            inimigo.rect.y = random.choice([HEIGHT - 230, HEIGHT - 400])
        
            gp_inimigo.add(inimigo)
            indice_spawn += 1
        # -------------------------------------------------------------------------------------

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k or event.key == pygame.K_j:
                    player.jump()
                if event.key == pygame.K_f or event.key == pygame.K_d:
                    player.ataque()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_k or event.key == pygame.K_j or event.key == pygame.K_f or event.key == pygame.K_d:
                    player.estado = "PARADO"

        colisao = pygame.sprite.spritecollide(player, gp_inimigo, False)

        player.update()
        gp_inimigo.update()

        # Verifica se houve colisão com o player e atualiza a barra de vida
        if colisao:
            if player.estado == "ATACANDO":
                player.vida = player.vida
            else:                      
                player.vida -= 10
            if player.vida <= 0:
                player.vivo = False

        # Verfica se o player está vivo para continuar ou não o jogo
        if not player.vivo:              
            game = False

        for inimigo in colisao:
            if player.estado == "ATACANDO":
                print("Acertou")
                print(player.estado)
            else:
                pass
                print("Errou")
                print(player.estado)
            
            inimigo.kill()

        # Mata os inimigos que não são atingidos e passam do limite da tela
        for inimigo in gp_inimigo:     
            if inimigo.rect.x <= 0:
                inimigo.kill()

        # ----- Gera saídas
        window.blit(fundo_img, (0,0))  # Substitui imagem de fundo 

        # desenhando os personagens do jogo
        player.draw(window)
        gp_inimigo.draw(window)

        player.update()
        gp_inimigo.update()
        
        pygame.display.update()  # Mostra o novo frame para o jogador

    # ===== Finalização =====
    pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

