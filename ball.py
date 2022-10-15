import pygame
from controls import *
import random


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
        self.score = False
        self.countdown = False

    def handle_collision(self, p1, p2):
        if self.y + self.radius >= HEIGHT:
            self.y_vel *= -1.05
        elif self.y - self.radius <= 0:
            self.y_vel *= -1.05

        if self.x_vel < 0:
            if p1.y - 5 <= self.y <= p1.y + p1.height:
                if self.x - self.radius <= p1.x + p1.width:
                    self.x_vel *= -1.05

                    middle_y = p1.y + p1.height / 2
                    difference_in_y = middle_y - self.y
                    reduction_factor = (p1.height / 2) / self.MAX_VEL
                    y_vel = difference_in_y / reduction_factor
                    self.y_vel = -1.05 * y_vel
        else:
            if p2.y - 5 <= self.y <= p2.y + p2.height:
                if self.x + self.radius >= p2.x:
                    self.x_vel *= -1.05

                    middle_y = p2.y + p2.height / 2
                    difference_in_y = middle_y - self.y
                    reduction_factor = (p2.height / 2) / self.MAX_VEL
                    y_vel = difference_in_y / reduction_factor
                    self.y_vel = -1.05 * y_vel

    def restart(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.y_vel = random.randint(-5, 5)
        self.x_vel = self.x_norm * random.choice([-1, 1])

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self):
        if not self.countdown:
            self.x += self.x_vel
            self.y += self.y_vel

    def check_score(self, p1, p2):
        name = None
        win = False
        if self.x >= WIDTH:
            p1 += 1
            self.score = True
        elif self.x <= 0:
            p2 += 1
            self.score = True
        if p1 == 10:
            win = True
            name = "Player 1"
        elif p2 == 10:
            win = True
            name = "Player 2"
        return p1, p2, (win, name)
