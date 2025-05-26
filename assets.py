import pygame
from jogoprincipal import WIDTH, HEIGHT 

# Carrega camadas do fundo
fundo_estrela = "assets\img\_fundo1.png"  
fundo_lua = "assets\img\_fundo2.png"  
fundo_nuvens = "assets\img\_fundo3.png"  

fundo_gameover = 'assets\img\gameover.png'

fantasma_voando = "assets\img\_fantasma\parado\VOANDO"
fantasma_pulo = "assets\img\_fantasma\parado\VOANDO"
fantasma_ataque = "assets\img\_fantasma\_atacando\_atacando"

# função que percorre e o caminho base e carrega as sprites para fazer a animação
def carregar_sprites(caminho_base, quantidade, tamanho=(150, 150)): 
        return [
            pygame.transform.scale(
                pygame.image.load(f"{caminho_base}{i}.png").convert_alpha(), 
                tamanho
            ) for i in range(1, quantidade + 1)
        ]

inimigo_abobora = "assets\img\inimigos\_abobora.png"

snd1 = "assets\snd\music\music1.mp3"

fonte = "assets\_font\PressStart2P-Regular.ttf"