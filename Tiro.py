class Tiro(Image):
    def __init__(self):
        self.file = "./assets/Shoot.png"

    def update(self):
        self.x += 15
        for enemy in enemies:
            if self._collides_with(enemy):
                self.x = 1000
                enemy.destroy()
