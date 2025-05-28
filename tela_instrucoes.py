import pygame
import glob
from assets import *  # importa variáveis de caminho (sprites, fontes, sons etc.)

def tela_instrucoes(window, WIDTH, HEIGHT):
    """
    Exibe a tela de instruções animada a partir de uma sequência de imagens
    convertidas de um GIF. Aguarda SPACE para voltar ou ESC para sair.
    """

    # Carrega a fonte definida em assets.py no tamanho 20px
    fonte_pequena = pygame.font.Font(fonte, 20)
    # Renderiza o texto que indica como voltar
    texto_iniciar2 = fonte_pequena.render("SPACE para voltar", True, (255, 255, 255))

    # Define a posição do texto: 10px da esquerda e 30px de distância da base
    x_texto = 10
    y_texto = HEIGHT - 30

    # ------------------------------------------------------------------
    # Carregamento dos frames da animação (209 imagens convertidas do GIF)
    # ------------------------------------------------------------------
    # Consulta todos os arquivos dentro da pasta de instruções
    frame_paths = sorted(glob.glob(fundo_instrucoes))
    # Se nenhum arquivo for encontrado, interrompe com mensagem de erro clara
    if not frame_paths:
        raise FileNotFoundError("Nenhum frame encontrado em assets/img/tela_instrucoes")

    # Cria uma lista de superfícies (Surface) redimensionadas para a tela inteira
    frames = []
    for path in frame_paths:
        img = pygame.image.load(path).convert_alpha()               # carrega imagem com canal alpha
        img = pygame.transform.scale(img, (WIDTH, HEIGHT))         # redimensiona para WIDTH×HEIGHT
        frames.append(img)

    # Índice do frame atual na lista `frames`
    frame_index = 0
    # Clock para controlar FPS da animação
    clock = pygame.time.Clock()

    # ----------------------------------------------------------
    # Loop principal: trata eventos, atualiza animação e desenha
    # ----------------------------------------------------------
    while True:
        # --------- Tratamento de eventos ------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # encerra o módulo pygame
                exit()         # termina o programa completamente
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return    # sai da função e volta à tela anterior
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        # ----------------------
        # Desenha o próximo frame
        # ----------------------
        window.blit(frames[frame_index], (0, 0))                  # desenha na posição (0,0)
        frame_index = (frame_index + 1) % len(frames)             # avança circularmente
        clock.tick(60)                                            # fixa em 60 FPS

        # -------------------
        # Desenha o texto
        # -------------------
        window.blit(texto_iniciar2, (x_texto, y_texto))

        # Atualiza o display com tudo que foi desenhado
        pygame.display.update()