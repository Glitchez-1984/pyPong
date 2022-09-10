import pygame

import paddles
from paddles import *
from controls import *
from ball import *
from ai_paddle import *

# SCREEN INIT
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pongy boi")

# VARIABLES
ball_radius = 7
paddle_speed = 5
paddle_length = 100
FPS = 60
# DEFINE OBJECTS
# paddle1 = Paddle(paddle_length, 15, 100, paddle_speed, True, WHITE)
paddle2 = Paddle(paddle_length, WIDTH - 30, 100, paddle_speed, False, WHITE)
ball = Ball(WIDTH // 2, HEIGHT // 2, ball_radius)
font = pygame.font.SysFont(None, 24)
ai = Paddle_ai(paddle_length, 30, 100, paddle_speed, WHITE)


# COLLISION MANAGEMENT
def handle_collision(ball, paddle1, paddle2):
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1.05
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1.05

    if ball.x_vel < 0:
        if paddle1.y <= ball.y <= paddle1.y + paddle1.height:
            if ball.x - ball.radius <= paddle1.x + paddle1.width:
                ball.x_vel *= -1.05

                middle_y = paddle1.y + paddle1.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (paddle1.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1.05 * y_vel
    else:
        if paddle2.y <= ball.y <= paddle2.y + paddle2.height:
            if ball.x + ball.radius >= paddle2.x:
                ball.x_vel *= -1.05

                middle_y = paddle2.y + paddle2.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (paddle2.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1.05 * y_vel


# RENDER TEXT
def set_text(string, coordx, coordy, fontSize):
    font = pygame.font.Font('freesansbold.ttf', fontSize)
    text = font.render(string, True, WHITE)
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    return text, textRect


# HANDLE ALL GRAPHICS
def graphics(screen):
    screen.fill(BLACK)
    ai.draw(screen)
    paddle2.draw(screen)
    ball.draw(screen)
    # DRAWS DOTTED LINE
    for i in range(10, HEIGHT, HEIGHT // 20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 5, i, 8, HEIGHT // 40))


# GAME LOOP
def main():
    run = True
    clock = pygame.time.Clock()
    P1_SCORE, P2_SCORE = 0, 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # paddle1.move()
        paddle2.move()
        ball.move()
        ai.move(ball.y, ball.x)
        handle_collision(ball, ai, paddle2)
        P1_SCORE, P2_SCORE = ball.check_win(P1_SCORE, P2_SCORE)
        graphics(win)
        p1_display = set_text(str(P1_SCORE), WIDTH // 2 - 60, 70, 60)
        p2_display = set_text(str(P2_SCORE), WIDTH // 2 + 60, 70, 60)
        win.blit(p1_display[0], p1_display[1])
        win.blit(p2_display[0], p2_display[1])
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
