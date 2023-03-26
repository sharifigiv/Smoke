from smoke import *

class Smoker:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.smoking = True
        self.smokes = []

    def create_smoke(self):
        self.smokes.append(Smoke(self.x, self.y))

    def update(self):
        if self.smoking:
            self.create_smoke()

        for s in self.smokes:
            if s.opacity <= 0:
                self.smokes.remove(s)
