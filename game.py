from tupy import *


count = 0
game = 'play'


class Enemy(Image):
    def __init__(self, file: str , x: int , y: int) -> None:
        self._file = file
        self._x = x
        self._y = y

    def destroy_self(self)->None:
        self._destroy()
    


class Tiro(Image):
    def __init__(self, enemies: list[Enemy]) -> None:
        self.file = "./assets/Shoot.png"
        self.enemies = enemies

    def update(self) -> None:
        self.x += 15
        for enemy in self.enemies.objects:
            if self._collides_with(enemy):
                self.x = 1000
                self.enemies.remove(enemy)
                enemy.destroy_self()


class Player(BaseImage):
    def __init__(self, enemies: list[Enemy]) -> None:
        self.tiros = []
        self._file = "./assets/Chewbacca.png"
        self.enemies = enemies
        self._x = 50
        self._y = 250

    def update(self) -> None:
        if keyboard.is_key_just_down("space"):
            self.shoot()
        if keyboard.is_key_down("w") or keyboard.is_key_down("Up"):
            self.move('Up')
        if keyboard.is_key_down("s") or keyboard.is_key_down("Down"):
            self.move('Down')
        if self.tiros is not None:
            for tiro in self.tiros:
                tiro.update()
                if tiro.y < -10:
                    tiro.destroy()
                    
    def move(self, direction)->None:
        if direction == 'Up' and self._y > 40:
            self._y -= 10
        elif direction == 'Down' and self._y < 450:
            self._y += 10

    def shoot(self) -> None:
        tiro = Tiro(enemies=self.enemies)
        tiro.x = self._x
        tiro.y = self._y
        self.tiros.append(tiro)

def update():
    global count
    global game 
    #Jogo rodando
    if game == 'play':
        if len(enemies1.objects) == 1:
            game = 'game over'
        player.update()
        if count < 100:
            count += 1
        else:
            count = 0
            enemies1.x -= 50
            if enemies1._collides_with(player):
                print('Game Over')
                game = 'game over'
            
    #Game over
    elif game == 'game over':
        toast("Game over! Enter = jogar novamente; Esc = Sair")
        if keyboard.is_key_just_down("Return"):
            game = 'play'
            print(game)
        if keyboard.is_key_down("Esc"):
            exit()

background = BaseImage("./assets/background.png", 450, 250)
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
enemyController = Enemy("./assets/enemy_1.png", 0, 0)
enemyController._hide()

enemies1 = Group([e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, enemyController])


player = Player( enemies=enemies1)


run(globals())
