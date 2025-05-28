import pygame
from assets import fonte

class ZonaPontuacao:
    def __init__ (self, centro_baixo, centro_alto, raio_interno, raio_externo):
        self.centro_baixo = centro_baixo
        self.centro_alto = centro_alto
        self.raio_interno = raio_interno
        self.raio_externo = raio_externo

    def desenhar(self, tela):
        # código sugerido pelo Chat GPT
        pygame.draw.circle(tela, (255, 255, 255), self.centro_baixo, self.raio_externo, 2)
        pygame.draw.circle(tela, (255, 255, 255), self.centro_baixo, self.raio_interno, 2)
        pygame.draw.circle(tela, (255, 255, 255), self.centro_alto, self.raio_externo, 2)
        pygame.draw.circle(tela, (255, 255, 255), self.centro_alto, self.raio_interno, 2)

    def calcular_pontuacao(self, inimigo_rect, tipo_acao, pontuacao_base=100):
        ix, iy = inimigo_rect.center

        if tipo_acao in ['d', 'f']:
            cx, cy = self.centro_baixo
        elif tipo_acao in ['j', 'k']:
            cx, cy = self.centro_alto
        else:
            return 0

        distancia = ((cx - ix)**2 + (cy - iy)**2)**0.5

        if distancia <= self.raio_interno:
            return pontuacao_base
        elif distancia <= self.raio_externo:
            return pontuacao_base // 2
        else:
            return 0


def desenhar_pontuacao(tela, pontuacao, posicao=(50, 50)):
    fonte_pixel = pygame.font.Font(fonte, 20)
    texto = fonte_pixel.render(f"PONTOS: {pontuacao}", True, (255, 255, 255))
    tela.blit(texto, posicao)