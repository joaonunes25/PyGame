import pygame
pygame.init()

WIDTH, HEIGHT = 1280, 720

# Carrega camadas do fundo
fundo_estrela = "assets\img\_fundo1.png"  
fundo_lua = "assets\img\_fundo2.png"  
fundo_nuvens = "assets\img\_fundo3.png"  

fundo_gameover = 'assets\img\_fundogameover.png'
fundo_inicial = "assets\img\_fundoiniicial.png"
fundo_instrucoes = "assets\img\_telainstrucoes.png"
fundo_vitoria_suprema = "assets\img\_tela_vitoria_suprema (2).png"
fundo_vitoria = "assets\img\_telavitoria.png"

fantasma_voando = "assets\img\_fantasma\parado\VOANDO"
fantasma_pulo = "assets\img\_fantasma\parado\VOANDO"
fantasma_ataque = "assets\img\_fantasma\_atacando\_atacando"


def carregar_sprites(caminho_base, quantidade, tamanho=(150, 150)): 
        return [
            pygame.transform.scale(
                pygame.image.load(f"{caminho_base}{i}.png").convert_alpha(), 
                tamanho
            ) for i in range(1, quantidade + 1)
        ]

        """
        Percorre um caminho base e carrega uma sequência de imagens para animação, redimensionando-as.
        Parâmetros:
            caminho_base (str): Caminho base das imagens (ex: "sprites/correr_").
            quantidade (int): Quantidade de sprites a serem carregadas.
            tamanho (tuple, opcional): Tamanho (largura, altura) para redimensionar cada imagem. 
                                    Valor padrão é (150, 150).

        Retorna:
            list: Lista de superfícies do Pygame com as imagens carregadas e redimensionadas.
        """

inimigo_abobora = "assets\img\inimigos\_abobora.png"

snd1 = "assets\snd\music1.mp3"
snd2 = "assets\snd\Ghost Dash (1).mp3"

fonte = "assets\_font\PressStart2P-Regular.ttf"