import random
import time

import pygame

from src.bullet import Bullet
from src.settings import SCREEN


class Alien(pygame.rect.Rect):
    def __init__(self, x, y):
        self.width = 30
        self.height = 30
        super().__init__(x, y, self.width, self.height)
        self.frequency = random.randint(300, 100000) / 1000
        self.velocity = 0.5
        self.direction = [0, 0]
        self.hp = 1
        self.color = (0, 150, 150)
        self.last_shoot_time = time.time()

    def update(self):
        # TODO: Управление с помощью pygame.key.get_pressed().
        pass

    def can_shoot(self):
        return self.last_shoot_time + self.frequency < time.time()

    def shoot(self):
        self.last_shoot_time = time.time()
        return Bullet(self.x + self.width / 2, self.y, 5, 10, 1)

    def draw(self):
        pygame.draw.rect(SCREEN, self.color, self)
