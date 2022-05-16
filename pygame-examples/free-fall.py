import pygame

from const import Window, Colors, Gravity
from object import Object


def control_object(obj):
    if pygame.key.get_pressed()[pygame.K_UP]:
        obj.v_x -= 5
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        obj.v_x += 5
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        obj.v_x = 0
        obj.v_y = 0


def main():
    obj = Object(
        x=100,
        y=100,
        height=30,
        width=30,
        v_x=5,
        v_y=10,
        boundary_x=Window.HEIGHT,
        boundary_y=Window.WIDTH,
        color=Colors.WHITE,
    )
    obj2 = Object(
        x=100,
        y=50,
        height=160,
        width=20,
        v_x=0,
        v_y=0,
        boundary_x=Window.HEIGHT,
        boundary_y=Window.WIDTH,
        color=Colors.WHITE
    )

    timestep = 100
    pygame.init()
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode(
        Window.SIZE
    )  # Displaying on specified window size
    pygame.display.set_caption("Our game")
    run = True
    while run:
        clock.tick(timestep)
        surface.fill(Colors.BLACK)  # Window Bg

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # To quit on clicking the X
                run = False
        control_object(obj2)
        obj.update(Gravity.No, timestep / 1000)
        obj2.update(Gravity.No, timestep/1000)
        obj.draw(surface)
        obj2.draw(surface)
        pygame.display.update()  # To update the display with newly added codes

    pygame.quit()


main()
