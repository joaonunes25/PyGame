import pygame
import random
import numpy as np
from player import *
from inimigo import *
from tela_inicial import tela_inicial
from tela_game_over import tela_game_over
from assets import *
from pontuação import *
from tela_vitoria import tela_vitoria
from tela_vitoria_suprema import tela_vitoria_suprema


# -----------------------------------------------------------Dicionário com variáveis de cada fase----------------------------------------------------------------
FASES = {
    1: {
        "fundo": (fundo_estrela, fundo_lua, fundo_nuvens),
        "inimigo_sprite": {
            "caminho": inimigo_abobora,
            "quantidade": 4,
            "spritesheet": True
        },
        "bpm": 56.5,
        "duracao": 94,
        "velocidade_inimigo": 60,
        "musica": snd1
    },
    2: {
        "fundo": (
            fundo_ceu,
            fundo_nuvem1,
            fundo_nuvem2
        ),
        "inimigo_sprite": {
            "caminho": inimigo_bat_,
            "quantidade": 4,
            "spritesheet": False
        },
        "bpm": 68.5,
        "duracao": 166,
        "velocidade_inimigo": 85,
        "musica": snd2
    },
}

#  Função que roda a fase
def iniciar_fase(numero_fase):
    pygame.init()
   
    config = FASES[numero_fase]

    WIDTH, HEIGHT = 1280, 720
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(f"Ghost Dash - Fase {numero_fase}")

    if numero_fase == 1:
        tela_inicial(window, WIDTH, HEIGHT)

    # Fundos
    fundo1 = pygame.image.load(config["fundo"][0]).convert_alpha()
    fundo2 = pygame.image.load(config["fundo"][1]).convert_alpha()
    fundo3 = pygame.image.load(config["fundo"][2]).convert_alpha()
    fundo1 = pygame.transform.scale(fundo1, (WIDTH, HEIGHT))
    fundo2 = pygame.transform.scale(fundo2, (1152, 648))
    fundo3 = pygame.transform.scale(fundo3, (WIDTH, HEIGHT))
    # Posições iniciais
    x1 = x3 = 0
    x_lua = WIDTH - 200

    sprites_parado = carregar_sprites(fantasma_voando, 4, tamanho=(250, 250))
    sprites_pulando = carregar_sprites(fantasma_pulo, 4, tamanho=(250, 250))
    sprites_atacando = carregar_sprites(fantasma_ataque, 5, tamanho=(250, 250))

    player = Player(sprites_parado, sprites_pulando, sprites_atacando)
    x_zona = player.rect.centerx + 200
    zona = ZonaPontuacao(
        centro_baixo= (x_zona, HEIGHT - 190),
        centro_alto= (x_zona, HEIGHT - 360),
        raio_interno= 25,
        raio_externo= 50
    )

    pontuacao_total = 0
    x_spawn = WIDTH
    BPM = config["bpm"]
    v_inimigo = config["velocidade_inimigo"]
    duracao = config["duracao"]
    inimigo_sprite = config["inimigo_sprite"]

    tempo_viagem = (x_spawn - x_zona) / v_inimigo  # segundos

    batida_intervalo = 60 / BPM
    batidas = np.arange(0, duracao + tempo_viagem, batida_intervalo)
    instantes_spawn = batidas - tempo_viagem

    # Guarda numa lista os tempos positivos
    lista = []
    for instante in instantes_spawn:
        if instante >= 0:
            lista.append(instante)
    instantes_spawn = lista

    gp_inimigo = pygame.sprite.Group()

    indice_batida = 0

    # Relógio para limitar o FPS
    clock = pygame.time.Clock()
    FPS = 60
    inicio_jogo = pygame.time.get_ticks()

    # Música
    pygame.mixer.music.load(config["musica"])
    som_soco = pygame.mixer.Sound(snd_soco)
    pygame.mixer.music.play()

    game = True
    tipo_acao = 'd'
    while game:
        
        clock.tick(FPS)
        tempo_atual = (pygame.time.get_ticks() - inicio_jogo)/ 1000

        while indice_batida < len(instantes_spawn) and tempo_atual >= instantes_spawn[indice_batida]:
            if config['inimigo_sprite']['spritesheet'] == False:

                """
                Criação dos inimigos no jogo, considerando dois formatos diferentes de animação:

                - Se `spritesheet` for False: carrega os sprites individuais de uma pasta (por exemplo, 'Bat1.png', 'Bat2.png', etc.)
                usando a função `carregar_sprites`. Esse método é necessário quando os quadros de animação estão salvos como
                arquivos separados e não em um único arquivo .png.

                - Se `spritesheet` for True: o inimigo será criado com base em um spritesheet, onde os quadros de animação
                estão todos em um único arquivo de imagem. Nesse caso, a classe `Inimigo` utilizará o método
                `carregar_spritesheet_em_lista` para extrair os quadros da imagem.

                OBS: O sistema original do jogo aceitava apenas spritesheets (um único arquivo contendo todos os quadros de animação).
                Esta verificação foi adicionada para permitir maior flexibilidade e aceitar também sprites em arquivos separados,
                como no caso do inimigo "morcego", cujas animações são fornecidas como imagens individuais.
                """

                inimigo_bat = carregar_sprites(inimigo_bat_, 4)
            sprite_cfg = config['inimigo_sprite']
            inimigo = Inimigo(
                spritesource=sprite_cfg['caminho'],
                num_sprites=sprite_cfg['quantidade'],
                usar_spritesheet=sprite_cfg['spritesheet']
)
            inimigo.rect.x = x_spawn

            if sprite_cfg['spritesheet'] == True:
                inimigo.rect.y = random.choice([HEIGHT - 230, HEIGHT - 400])
            else:
                inimigo.rect.y = random.choice([HEIGHT - 430, HEIGHT - 280])
                

            gp_inimigo.add(inimigo)

            indice_batida += 1

        # --------------------------------Tratando eventos-----------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_k, pygame.K_j]:
                    tipo_acao = 'j' if event.key == pygame.K_j else 'k'
                    player.jump()
                    player.ataque(indice_inicio=2)  # manter sprite de ataque mesmo no pulo
                    som_soco.play()

                elif event.key in [pygame.K_f, pygame.K_d]:
                    tipo_acao = 'd' if event.key == pygame.K_d else 'f'
                    player.ataque(indice_inicio=2)
                    som_soco.play()

                # verifica pontuação
                for inimigo in gp_inimigo:
                    pontos = zona.calcular_pontuacao(inimigo.rect, tipo_acao, 100)
                    if pontos > 0:
                        pontuacao_total += pontos
                        inimigo.kill()

        colisao = pygame.sprite.spritecollide(player, gp_inimigo, False)
        player.update()
        gp_inimigo.update()

        if colisao:
            interagiu_com_player = True
            if player.estado == "PULANDO":
                player.ataque(indice_inicio=2)

            if player.estado != "ATACANDO" and not inimigo.interagiu_com_player:
                player.vida -= 5
                inimigo.interagiu_com_player = True
                if player.vida <= 0:
                    player.vivo = False
            
        if not player.vivo:
            pygame.mixer.music.stop()
            # atualizar_ranking(nome_jogador, pontuacao_total)  # atualiza o ranking com o nome passado
            tela_game_over(window, WIDTH, HEIGHT)
            # from ranking import tela_ranking  # importe a função do ranking se necessário
            # tela_ranking(window, WIDTH, HEIGHT)  # exibe o ranking
            return  # sai da função para evitar reinício imediato
            
            inimigo.kill() # Se o inimigo colide com o jogador e ele está atacando, o inimido é removido

        for inimigo in gp_inimigo: # Se o inimigo sai da tela, ele é removido
            if inimigo.rect.x <= 0:
                if player.vida <= 0:
                    player.vivo = False
                inimigo.kill()

        if tempo_atual >= duracao and player.vivo:
            pygame.mixer.music.stop()
            if numero_fase + 1 in FASES:
                tela_vitoria(window, WIDTH, HEIGHT)
                iniciar_fase(numero_fase + 1)
            else:
                tela_vitoria_suprema(window, WIDTH, HEIGHT)
                
        # Movimento dos fundos
        x1 -= 0.2
        x3 -= 1.2
        x_lua -= 0.3
        if x1 <= -WIDTH:
            x1 = 0
        if x3 <= -WIDTH:
            x3 = 0
        if x_lua < -fundo2.get_width():
            x_lua = WIDTH

        # Desenhando o jogo
        window.blit(fundo1, (x1, 0))
        window.blit(fundo1, (x1 + WIDTH, 0))
        window.blit(fundo2, (x_lua, 80))
        window.blit(fundo3, (x3, 0))
        window.blit(fundo3, (x3 + WIDTH, 0))
        player.draw(window)
        gp_inimigo.draw(window)
        zona.desenhar(window)
        desenhar_pontuacao(window, pontuacao_total)

        pygame.display.update()

    pygame.quit()


# Garante que o jogo seja executado quando na main.py
if __name__ == "__main__":
    iniciar_fase(1)