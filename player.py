import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.rect = pygame.Rect(0, pygame.display.get_surface().get_height()- 300, 100, 100)
        self.color = (0,0,0)   # branco
        self.velocidade_y = 0

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)