from smoke import *

class Smoker:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.smoking = True
        self.smokes = []

        self.color = [255, 255, 255]
        self.width = 60
        self.height = 60

    def create_smoke(self, direction: list, change = [0, 0]):
        smk = Smoke(self.x + change[0], self.y + change[1], self.color)
        smk.vel = direction

        smk.width = self.width
        smk.height = self.height

        self.smokes.append(smk)

    def update(self):
        if self.smoking:
            for s in self.smokes:
                s.update()

                if s.opacity <= 0:
                    self.smokes.remove(s)