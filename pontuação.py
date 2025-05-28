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
    """
    Calcula a pontuação obtida com base na posição do inimigo e na tecla pressionada.

    Parâmetros:
    - inimigo_rect: o retângulo (pygame.Rect) do inimigo, usado para obter sua posição central.
    - tipo_acao: tecla pressionada pelo jogador, representando o tipo de ataque:
        - 'd' ou 'f': ataque na zona inferior (centro_baixo).
        - 'j' ou 'k': ataque na zona superior (centro_alto).
    - pontuacao_base (opcional): valor máximo de pontos possíveis (padrão = 100).

    Funcionamento:
    1. Identifica o centro de referência (alto ou baixo) com base no tipo de ação.
    2. Calcula a distância entre o centro do inimigo e o centro da zona correspondente.
    3. Define a pontuação com base nessa distância:
        - Se estiver dentro do raio interno → pontuação máxima.
        - Se estiver dentro do raio externo → metade da pontuação.
        - Fora dos dois raios → pontuação zero.

    Retorno:
    - Um inteiro representando os pontos ganhos com o ataque.
    """

def desenhar_pontuacao(tela, pontuacao, posicao=(50, 50)):
    fonte_pixel = pygame.font.Font(fonte, 20)
    texto = fonte_pixel.render(f"PONTOS: {pontuacao}", True, (255, 255, 255))
    tela.blit(texto, posicao)