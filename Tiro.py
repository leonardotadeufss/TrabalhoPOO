from tupy import *
from Enemy import Enemy


class Tiro(Image):
    def __init__(self, enemies: Enemy) -> None:
        self.file = "./assets/Shoot.png"
        self.enemies = enemies

    def update(self) -> None:
        self.x += 15
        for enemy in self.enemies:
            if self._collides_with(enemy):
                self.x = 1000
                enemy.x = 1000
