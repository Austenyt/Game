import pygame

from src.settings import SCREEN


class Bullet(pygame.rect.Rect):
    def __init__(self, x, y, width, height, direction):
        self.width = width
        self.height = height
        self.direction = direction
        super().__init__(x, y, self.width, self.height)
        self.velocity = 2
        self.hp = 1
        self.color = (0, 150, 0)

    def update(self):
        self.y += self.velocity * self.direction

    def draw(self):
        pygame.draw.rect(SCREEN, self.color, self)
