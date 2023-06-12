from tupy import *


class Game(Image):
    def __init__(self):
        self.state = "menu"

    def update(self):
        if keyboard.is_key_just_down("q"):
            quit()
        if keyboard.is_key_just_down("r"):
            run_game()
        if keyboard.is_key_just_down("p"):
            pause_game()


class Background(Image):
    def __init__(self, file, x=0, y=0) -> None:
        self.file = file
        self.x = x
        self.y = y


class Master(Image):
    def __init__(self, file, riddles) -> None:
        self.file = file
        self.riddles = riddles


class Element(Image):
    def __init__(self, background: Background, master: Master, file, x, y) -> None:
        self.background = background
        self.master = master
        self.file = file
        self.x = x
        self.y = y


class Riddle:
    def __init__(self, answer, text, hint=None) -> None:
        self.hint = hint
        self.text = text
        self.answer = answer


def run_game():
    print("game on")
    start_game.destroy()
    quit_game.destroy()
    bg_menu.destroy()

    fire = Element(
        Background("./assets/firenation.webp", 350, 350),
        Master("./assets/tio_iroh.webp", []),
        "./assets/fogo.png",
        600,
        350,
    )
    earth = Element(
        Background("./assets/earth_kingdom.png", 350, 350),
        Master("./assets/toph.webp", []),
        "./assets/terra.png",
        600,
        150,
    )
    water = Element(
        Background("./assets/tribe_of_water.png", 350, 350),
        Master("./assets/katara.webp", []),
        "./assets/agua.png",
        300,
        150,
    )
    air = Element(
        Background("./assets/air_temple.jpg", 350, 350),
        Master("./assets/aang.webp", []),
        "./assets/ar.png",
        300,
        350,
    )
    fire.background._hide()
    air.background._hide()
    water.background._hide()
    earth.background._hide()

    fire.master._hide()
    air.master._hide()
    water.master._hide()
    earth.master._hide()

    element_choose = input(prompt="Escolha o elemento")
    print(element_choose)
    # if 100 <= mouse.x <= 400 and 50 <= mouse.y <= 200:
    #     print("water")
    if element_choose == "fogo":
        fire.background._show()
        fire.master._show()
    elif element_choose == "água":
        water.master._show()
        water.background._show()
    elif element_choose == "terra":
        earth.master._show()
        earth.background._show()
    elif element_choose == "ar":
        air.master._show()
        air.background._show()
    else:
        input(
            prompt="Elemento inválido, tente alguma das opções: Fogo, Água, Terra, Ar"
        )

    return


def pause_game():
    print("game paused")


bg_menu = Background("./assets/menu.png", 450, 250)
start_game = Label("Jogar (P)", 440, 400)
quit_game = Label("Sair (Q)", 450, 440)
game = Game()


if __name__ == "__main__":
    game._hide()
    # tio_iroh._hide()
    # katara._hide()
    # toph._hide()
    # aang._hide()
    # bg_air._hide()
    # bg_fire._hide()
    # bg_water._hide()
    # bg_earth._hide()

    run(globals())
