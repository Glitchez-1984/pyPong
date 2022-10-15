import pygame
from paddles import *
from controls import *
from ball import *
from ai_paddle import *

# SCREEN INIT
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
icon = pygame.image.load('glitch.png')
pygame.display.set_icon(icon)

# VARIABLES
ball_radius = 7
paddle_speed = PADDLE_VEL
ai_paddle_speed = AI_VEL
paddle_length = 100
FPS = 75
# DEFINE OBJECTS

paddle2 = Paddle(paddle_length, WIDTH - 30, 100, paddle_speed, False, FG)
ball = Ball(WIDTH // 2, HEIGHT // 2, ball_radius)
font = pygame.font.SysFont(None, 24)
if MULTIPLAYER == 0:
    paddle1 = AI_Paddle(paddle_length, 30, 100, ai_paddle_speed, FG)
else:
    paddle1 = Paddle(paddle_length, 15, 100, paddle_speed, True, FG)


def set_text(string, coordx, coordy, fontSize):
    fontx = pygame.font.Font('freesansbold.ttf', fontSize)
    text = fontx.render(string, True, FG)
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    return text, textRect


# HANDLE ALL GRAPHICS
def graphics(screen):
    screen.fill(BG)
    paddle1.draw(screen)
    paddle2.draw(screen)
    ball.draw(screen)
    # DRAWS DOTTED LINE
    for i in range(10, HEIGHT, HEIGHT // 20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(screen, FG, (WIDTH // 2 - 5, i, 8, HEIGHT // 40))


# GAME LOOP
def main():
    run = True
    clock = pygame.time.Clock()
    P1_SCORE, P2_SCORE, check_win = 0, 0, (False, None)
    current_time = 0
    stop_time = 0
    while run:
        clock.tick(FPS)
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if check_win[0]:
            win_screen = set_text("Game Over. " + str(check_win[1]) + " Won", WIDTH // 2, 150, 40)
            win.blit(win_screen[0], win_screen[1])
            pass
        else:
            paddle2.move()
            if MULTIPLAYER == 0:
                paddle1.move(ball.y)
                if ball.score:
                    paddle1.hit = True
            else:
                paddle1.move()
            ball.handle_collision(paddle1, paddle2)
            P1_SCORE, P2_SCORE, check_win = ball.check_score(P1_SCORE, P2_SCORE)
            graphics(win)
            if ball.score:
                ball.restart()
                stop_time = pygame.time.get_ticks()
                ball.countdown = True
                ball.score = False
            if ball.countdown and current_time > stop_time + 1000:
                ball.countdown = False
            ball.move()
            p1_display = set_text(str(P1_SCORE), WIDTH // 2 - 60, 70, 60)
            p2_display = set_text(str(P2_SCORE), WIDTH // 2 + 60, 70, 60)
            win.blit(p1_display[0], p1_display[1])
            win.blit(p2_display[0], p2_display[1])
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
