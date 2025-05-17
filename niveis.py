import pygame
from inimigo import *
from player import *

# nivel teste: We will rock you

batida = 750   # 80 BPM -> 1 batida a cada 750 ms
tempo_musica = 134000 #ms
lista_tempo = []

for i in range (tempo_musica):
    lista_tempo.append(i+750)
    
# for tempo in range (len(lista_tempo)):
#     inimigo = Inimigo(inimigo_img)
#     gp_inimigo.add(inimigo)