import pygame
from assets import fonte, historia_imgs

#CÓDIGO GERADO 100% POR INTELIGENCIA ARTIFICIAL (CHATGPT)

# Textos da história divididos em duas linhas manualmente
textos_historia = [
    ["Em um reino encantado, onde fantasmas", "viviam em perfeita harmonia musical..."],
    ["Terríveis monstros surgiram das sombras,", "aprisionando todos sem piedade!"],
    ["Restou apenas um fantasminha...", "dotado de um dom musical único, mas agora sozinho."],
    ["Ele entendeu: com coragem, ritmo e seus punhos,", "libertaria seus amigos do mal!"],
]

def tela_historia(window, WIDTH, HEIGHT):
    pygame.font.init()
    fonte_historia = pygame.font.Font(fonte, 22)

    largura_img = WIDTH // 2
    altura_img = HEIGHT // 2

    imagens = [
        pygame.transform.scale(pygame.image.load(path).convert_alpha(), (largura_img, altura_img))
        for path in historia_imgs
    ]

    index_imagem = 0
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if index_imagem < 3:
                        index_imagem += 1
                    else:
                        return
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        window.fill((0, 0, 0))

        posicoes = [
            (0, 0),
            (largura_img, 0),
            (0, altura_img),
            (largura_img, altura_img),
        ]

        for i in range(index_imagem + 1):
            window.blit(imagens[i], posicoes[i])

        # Renderiza duas linhas de texto, centralizadas
        linha1 = fonte_historia.render(textos_historia[index_imagem][0], True, (255, 255, 255))
        linha2 = fonte_historia.render(textos_historia[index_imagem][1], True, (255, 255, 255))

        linha1_rect = linha1.get_rect(center=(WIDTH // 2, HEIGHT - 60))
        linha2_rect = linha2.get_rect(center=(WIDTH // 2, HEIGHT - 30))

        window.blit(linha1, linha1_rect)
        window.blit(linha2, linha2_rect)

        pygame.display.update()
        clock.tick(60)