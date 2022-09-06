import pygame
from controls import *


class Ball:
    MAX_VEL = 5
    color = WHITE

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def restart(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def check_win(self, p1, p2):
        if self.x >= WIDTH:
            p1 += 1
            self.restart()
        elif self.x <= 0:
            p2 += 1
            self.restart()
        return p1, p2
