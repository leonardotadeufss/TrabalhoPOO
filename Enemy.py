from tupy import *


class Enemy(Image):
    def __init__(self, file, x, y):
        self.file = file
        self.x = x
        self.y = y

    def destroy_self(self):
        self._destroy()
