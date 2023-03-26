class Smoke:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.width = 30
        self.height = 30

        self.opacity = 100

        self.vel = [0, 0]

    def update(self):
        self.x += self.vel[0]
        self.y += self.vel[1]

        self.opacity -= 0.4