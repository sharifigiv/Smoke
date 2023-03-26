import pyray as pr
from random import choice

from smoke import Smoke
from smoker import Smoker

pr.init_window(1080, 720, "Smoker")

smk = Smoker(1080 // 2 - 30, 720 // 2 - 30)

smk_img = pr.load_image("assets/smoke.png")
pr.image_resize(smk_img, smk.width, smk.height)

smk_tx = pr.load_texture_from_image(smk_img)

pr.unload_image(smk_img)

pr.set_target_fps(60)

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)

    if pr.is_mouse_button_down(0):
        mouse_pos = [pr.get_mouse_x() + choice([5, -5, 10, -10, 25, -25, 15, -15, 20, -20, 30, -30, 35, -35]), pr.get_mouse_y() + choice([5, -5, 10, -10, 25, -25, 15, -15, 20, -20, 30, -30, 35, -35])]

        d = [mouse_pos[0] - smk.x, mouse_pos[1] - smk.y]
        mag = (d[0] ** 2 + d[1] ** 2) ** 0.5

        d[0] = (d[0] / mag) * 2
        d[1] = (d[1] / mag) * 2

        smk.create_smoke(d, change=[choice([5, -5, 2, -2, 4, -4]), choice([5, -5, 2, -2, 4, -4])])
 
    smk.update()

    for particle in smk.smokes:
        pr.draw_texture(smk_tx, int(particle.x), int(particle.y), pr.Color(particle.color[0], particle.color[1], particle.color[2], int(particle.opacity)))

    pr.draw_circle(smk.x + 30, smk.y + 30, 5, pr.RED)

    pr.end_drawing()