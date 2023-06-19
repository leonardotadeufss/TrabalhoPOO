class Player(Image):
    def __init__(self, file):
        self.tiros = []
        self.file = file

    def update(self):
        if keyboard.is_key_just_down("space"):
            self.dispara()
        if keyboard.is_key_down("w"):
            if self.y > 40:
                self.y -= 10
        if keyboard.is_key_down("s"):
            if self.y < 450:
                self.y += 10
        if self.tiros is not None:
            for tiro in self.tiros:
                tiro.update()
                if tiro.y < -10:
                    tiro.destroy()
                    tiro = None

    def dispara(self):
        tiro = Tiro()
        tiro.x = self.x
        tiro.y = self.y
        self.tiros.append(tiro)
