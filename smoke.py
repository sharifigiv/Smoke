class Smoke:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y

        self.width = 50
        self.height = 50

        self.vel = [0, 0]

        self.color = color
        self.opacity = 100

    def update(self):
        self.x += self.vel[0]
        self.y += self.vel[1]

        self.opacity -= 0.4