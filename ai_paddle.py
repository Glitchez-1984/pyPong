import pygame
from controls import *


class AI_Paddle:
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

    def move(self, ball_y):
        if ball_y > self.y and self.y <= HEIGHT - self.height - 10 and not (
                self.y + self.speed > ball_y):
            self.y += self.speed
        elif ball_y < self.y and self.y >= 10 and not (
                self.y - self.speed < ball_y):
            self.y -= self.speed
