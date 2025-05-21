import pygame
from jogoprincipal import WIDTH, HEIGHT 

# Carrega camadas do fundo
fundo1 = pygame.image.load("assets\img\_fundo1.png").convert_alpha()  # estrelas
fundo2 = pygame.image.load("assets\img\_fundo2.png").convert_alpha()  # lua
fundo3 = pygame.image.load("assets\img\_fundo3.png").convert_alpha()  # nuvens

fundo1 = pygame.transform.scale(fundo1, (WIDTH, HEIGHT))
fundo2 = pygame.transform.scale(fundo2, (1152, 648))  # lua maior
fundo3 = pygame.transform.scale(fundo3, (WIDTH, HEIGHT))


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