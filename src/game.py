import pygame
from src.settings import *


class Game:

    def __init__(self):
        self.player = pygame.rect.Rect(100, 100, 50, 50)
        self.direction = [0, 0]

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP6:
                        self.direction[0] = 1
                    elif event.key == pygame.K_KP4:
                        self.direction[0] = -1
                    elif event.key == pygame.K_KP8:
                        self.direction[0] = 1
                    elif event.key == pygame.K_KP2:
                        self.direction[0] = -1
                elif event.type == pygame.KEYUP:
                    if event.key in [pygame.K_KP6, pygame.K_KP4]:
                        self.direction[0] = 0
            self.player.x += self.direction[0] * 1
            SCREEN.fill((0, 0, 0))
            pygame.draw.rect(SCREEN, (255, 0, 0), self.player)
            pygame.display.flip()
