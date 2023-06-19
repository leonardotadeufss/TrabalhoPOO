from tupy import *
from Enemy import Enemy
from Tiro import Tiro
from Player import Player


background = Image("./assets/background.png", 450, 250)
e1 = Enemy("./assets/enemy_1.png", 740, 50)
e2 = Enemy("./assets/enemy_1.png", 740, 120)
e3 = Enemy("./assets/enemy_1.png", 740, 190)
e4 = Enemy("./assets/enemy_1.png", 740, 260)
e5 = Enemy("./assets/enemy_1.png", 740, 330)
e6 = Enemy("./assets/enemy_1.png", 740, 400)
e7 = Enemy("./assets/enemy_1.png", 640, 50)
e8 = Enemy("./assets/enemy_1.png", 640, 120)
e9 = Enemy("./assets/enemy_1.png", 640, 190)
e10 = Enemy("./assets/enemy_1.png", 640, 260)
e11 = Enemy("./assets/enemy_1.png", 640, 330)
e12 = Enemy("./assets/enemy_1.png", 640, 400)

enemies = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12]


player = Player("./assets/Chewbacca.png")
player.x = 50
player.y = 250

run(globals())
