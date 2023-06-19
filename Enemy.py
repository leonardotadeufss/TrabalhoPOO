from tupy import *

count = 0


class Enemy(Image):
    def __init__(self, file, x, y):
        self.file = file
        self.x = x
        self.y = y

    def update(self):
        global count
        if count < 5000:
            count += 1
        else:
            count = 0
            for enemy in enemies:
                enemy.x -= 50
