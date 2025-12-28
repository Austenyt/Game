import random

from . import player
from .alien import Alien
from .player import Player
from .settings import *


class Game:

    def __init__(self):
        self.player = Player(375, 500)
        self.aliens = []
        for x in range(40, WIDTH - 50, 40):
            for y in range(100, HEIGHT - 300, 50):
                alien = Alien(x, y)
                self.aliens.append(alien)
        self.bullets_player = []
        self.bullets_alien = []

    def run(self) -> None:
        """
        Запуск игрового процесса
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.update()
            self.draw()

    def update(self) -> None:
        """
        Обновляет свойства объектов
        """
        self.player.update()
        for alien in self.aliens:
            alien.update()
        if self.player.can_shoot():
            self.bullets_player.append(self.player.shoot())
        selected_alien = random.choice(self.aliens)
        if selected_alien.can_shoot():
            self.bullets_alien.append(selected_alien.shoot())
        for bullet in self.bullets_player:
            bullet.update()
            for alien in self.aliens:
                if alien.colliderect(bullet):
                    self.aliens.remove(alien)
                    self.bullets_player.remove(bullet)
        for bullet in self.bullets_alien:
            bullet.update()
            if self.player.colliderect(bullet):
                self.bullets_alien.remove(bullet)
                self.player.hp -= 1
                if self.player.hp < 1:
                    Game().run()
                    del self

    def draw(self) -> None:
        """
        Отрисовка
        """
        SCREEN.fill((0, 0, 0))
        self.player.draw()
        for alien in self.aliens:
            alien.draw()
        for bullet in self.bullets_player:
            bullet.draw()
        for bullet in self.bullets_alien:
            bullet.draw()
        pygame.display.flip()
