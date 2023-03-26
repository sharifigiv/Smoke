class Smoke:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.opacity = 200

        self.vel = [0, 0]

    def update(self):
        self.x += self.vel[0]
        self.y += self.vel[1]

        self.opacity -= 0.2