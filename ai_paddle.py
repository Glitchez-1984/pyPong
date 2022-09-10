import pygame
from controls import *
import random

class Paddle_ai:
    def __init__(self, height, x, y, speed, color):
        self.height = height
        self.width = 15
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed

    def draw(self, win):
        paddle_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, self.color, paddle_rect)

    def move(self, ball_y, ball_x):
        y_dif = abs(ball_y - (self.y + self.height//2))
        if ball_x - 7 <= self.x + self.width or self.width == 15:
            target = self.y + random.randint(0, self.height)
        if ball_y > target and self.y <= HEIGHT - self.height - 10 and y_dif >= self.speed:
            self.y += self.speed
        elif ball_y < target and self.y >= 10 and y_dif >= self.speed:
            self.y -= self.speed
