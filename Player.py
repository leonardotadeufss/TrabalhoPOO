from tupy import *
from Tiro import Tiro
from Enemy import Enemy


class Player(Image):
    def __init__(self, file: str, enemies: Enemy) -> None:
        self.tiros = []
        self.file = file
        self.enemies = enemies

    def update(self) -> None:
        if keyboard.is_key_just_down("space"):
            self.dispara()
        if keyboard.is_key_down("w") or keyboard.is_key_down("Up"):
            if self.y > 40:
                self.y -= 10
        if keyboard.is_key_down("s") or keyboard.is_key_down("Down"):
            if self.y < 450:
                self.y += 10
        if self.tiros is not None:
            for tiro in self.tiros:
                tiro.update()
                if tiro.y < -10:
                    tiro.destroy()
                    tiro = None

    def dispara(self) -> None:
        tiro = Tiro(enemies=self.enemies)
        tiro.x = self.x
        tiro.y = self.y
        self.tiros.append(tiro)
