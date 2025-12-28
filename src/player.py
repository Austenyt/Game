import time

import pygame

from src.bullet import Bullet
from src.settings import SCREEN, WIDTH


class Player(pygame.rect.Rect):
    def __init__(self, x, y):
        self.width = 50
        self.height = 50
        super().__init__(x, y, self.width, self.height)
        self.frequency = 1
        self.displacement = 1
        self.hp = 3
        self.color = (150, 100, 100)
        self.last_shoot_time = time.time()

    def update(self):
        keys = pygame.key.get_pressed()  # Получение состояния клавиш

        # Проверка нажатия клавиш и обновление направления
        if keys[pygame.K_LEFT] and self.x > 0:  # Если нажата клавиша "влево"
            self.x -= self.displacement
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:  # Если нажата клавиша "вправо"
            self.x += self.displacement
        # if keys[pygame.K_UP]:  # Если нажата клавиша "вверх"
        #     self.direction[1] = -self.velocity
        # if keys[pygame.K_DOWN]:  # Если нажата клавиша "вниз"
        #     self.direction[1] = self.velocity

    def can_shoot(self):
        return self.last_shoot_time + self.frequency < time.time()

    def shoot(self):
        self.last_shoot_time = time.time()
        return Bullet(self.x + self.width / 2, self.y, 5, 10, -1)

    def draw(self):
        pygame.draw.rect(SCREEN, self.color, self)
