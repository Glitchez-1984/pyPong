import pygame
from controls import *
import random
import time


class Ball:
    MAX_VEL = BALL_SPEED
    color = FG

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0
        self.x_norm = self.MAX_VEL

    def restart(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.y_vel = random.randint(-5, 5)
        self.x_vel = self.x_norm

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def check_score(self, p1, p2):
        name = None
        win = False
        if self.x >= WIDTH:
            p1 += 1
            self.restart()
        elif self.x <= 0:
            p2 += 1
            self.restart()
        if p1 == 10:
            win = True
            name = "Player 1"
        elif p2 == 10:
            win = True
            name = "Player 2"
        return p1, p2, (win, name)
