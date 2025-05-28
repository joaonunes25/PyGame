import pygame  # biblioteca principal para jogos em Python
from tela_instrucoes import tela_instrucoes  # função para exibir a tela de instruções

# Diretório absoluto onde estão armazenados os quadros da animação
IMGS_DIR = r"C:\PYGAME\PyGame-2\assets\img\tela_inicial"


def tela_inicial(window, WIDTH, HEIGHT):
    """
    Exibe a tela inicial animada usando quadros pré-carregados.

    Args:
        window (pygame.Surface): superfície principal onde será desenhada a animação.
        WIDTH (int): largura da janela para escalonamento dos quadros.
        HEIGHT (int): altura da janela para escalonamento dos quadros.
    """
    # Número total de quadros extraídos do GIF original
    TOTAL_FRAMES = 155

    # Lista para armazenar todos os Surfaces dos quadros animados
    frames = []
    for i in range(TOTAL_FRAMES):
        # Monta o caminho do arquivo de imagem do quadro 'i'
        path = f"{IMGS_DIR}/tela inicial-{i:04d}.jpg"
        # Carrega a imagem e converte para Surface com suporte a transparência
        img = pygame.image.load(path).convert_alpha()
        # Escalona a imagem para preencher toda a janela
        img = pygame.transform.scale(img, (WIDTH, HEIGHT))
        # Adiciona o Surface à lista de quadros
        frames.append(img)

    # Cria um relógio para controlar o frame rate da animação
    clock = pygame.time.Clock()
    # Define quantos quadros por segundo a animação deve exibir
    fps_anim = 60
    # Índice do quadro que será desenhado a cada iteração
    indice = 0

    # Loop principal da tela inicial
    while True:
        # Processa eventos de teclado e janela
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Fecha o Pygame e encerra o programa imediatamente
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Sai da tela inicial e retorna para iniciar o jogo
                    return
                elif event.key == pygame.K_SPACE:
                    # Exibe a tela de instruções antes de retornar
                    tela_instrucoes(window, WIDTH, HEIGHT)
                elif event.key == pygame.K_ESCAPE:
                    # Encerra o jogo se ESC for pressionado
                    pygame.quit()
                    exit()

        # Desenha o quadro atual da animação na posição (0,0)
        window.blit(frames[indice], (0, 0))
        # Avança para o próximo quadro, reiniciando após o último
        indice = (indice + 1) % TOTAL_FRAMES

        # Atualiza o display com o conteúdo desenhado
        pygame.display.update()
        # Controla a velocidade do loop para fps_anim quadros por segundo
        clock.tick(fps_anim)