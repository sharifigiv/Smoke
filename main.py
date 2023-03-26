import pyray as pr
from random import choice

from smoke import Smoke
from smoker import Smoker

pr.init_window(1080, 720, "Smoker")

smk = Smoker(1080 // 2, 720 // 2)

pr.set_target_fps(60)

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)

    pr.draw_circle(smk.x + 15, smk.y + 15, 1, pr.RED)

    if pr.is_mouse_button_down(0):
        mouse_pos = [pr.get_mouse_x() + choice([5, -5, 10, -10, 25, -25, 15, -15, 20, -20, 30, -30, 35, -35]), pr.get_mouse_y() + choice([5, -5, 10, -10, 25, -25, 15, -15, 20, -20, 30, -30, 35, -35])]

        d = [mouse_pos[0] - smk.x, mouse_pos[1] - smk.y]
        mag = (d[0] ** 2 + d[1] ** 2) ** 0.5

        d[0] = (d[0] / mag) * 2
        d[1] = (d[1] / mag) * 2

        smk.create_smoke(d, change=[choice([5, -5, 2, -2, 4, -4]), choice([5, -5, 2, -2, 4, -4])])
 
    smk.update()

    for particle in smk.smokes:
        pr.draw_rectangle(int(particle.x), int(particle.y), particle.width, particle.height, pr.Color(255, 255, 255, int(particle.opacity)))


    pr.end_drawing()