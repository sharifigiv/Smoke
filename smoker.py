from smoke import *

class Smoker:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.smoking = True
        self.smokes = []

    def create_smoke(self, direction: list, change = [0, 0]):
        smk = Smoke(self.x + change[0], self.y + change[1])
        smk.vel = direction

        self.smokes.append(smk)

    def update(self):
        if self.smoking:
            for s in self.smokes:
                s.update()

                if s.opacity <= 0:
                    self.smokes.remove(s)
                    
