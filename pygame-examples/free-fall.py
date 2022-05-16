import pygame

from const import Window, Colors, Gravity
from object import Object


def main():
    obj = Object(
        x=100,
        y=100,
        height=40,
        width=40,
        v_x=0,
        v_y=0,
        boundary_x=Window.HEIGHT,
        boundary_y=Window.WIDTH,
        color=Colors.WHITE,
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
        obj.update(Gravity.Earth, timestep / 1000)
        obj2.update(Gravity.Earth, timestep / 1000)
        obj.draw(surface)
        obj2.draw(surface)
        pygame.display.update()  # To update the display with newly added codes

    pygame.quit()


main()
