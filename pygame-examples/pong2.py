import pygame
from const import Colors, Window, Gravity
from paddle2 import Paddle
from ball2 import Ball


def main():
    paddle1 = Paddle(
        x=100,
        y=100,
        height=120,
        width=20,
        color=Colors.PINK,
    )
    paddle2 = Paddle(
        x=Window.WIDTH - 100,
        y=300,
        height=120,
        width=20,
        color=Colors.BLUE
    )
    ball = Ball(
        x=0,
        y=0,
        radius=10,
        v=0,
        bearing=0,
        color=Colors.WHITE
    )
    timestep = 100
    pygame.init()
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode(Window.SIZE)  # Displaying on specified window size
    pygame.display.set_caption("Our game")
    font = pygame.font.SysFont("verdana", 16)
    run = True
    ball.restart()
    scores = {
        'left': 0,
        'right': 0
    }
    while run:
        clock.tick(timestep)
        surface.fill(Colors.GREEN)  # Window Bg

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # To quit on clicking the X
                run = False

        paddle1_up = pygame.key.get_pressed()[pygame.K_w]
        paddle2_up = pygame.key.get_pressed()[pygame.K_UP]
        paddle1_down = pygame.key.get_pressed()[pygame.K_s]
        paddle2_down = pygame.key.get_pressed()[pygame.K_DOWN]

        paddle1.update(timestep/1000, paddle1_up, paddle1_down)
        paddle2.update(timestep / 1000, paddle2_up, paddle2_down)
        ball.update(timestep/1000, paddles=[paddle1, paddle2], scores=scores)

        paddle1.draw(surface, score=scores['left'], font=font)
        paddle2.draw(surface, score=scores['right'], font=font)
        ball.draw(surface)
        pygame.display.update()  # To update the display with newly added codes
        print(scores)

    pygame.quit()


main()