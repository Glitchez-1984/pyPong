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

    def move(self, ball_y):

        middle = self.y - (self.height//2)
        y_dif = abs(ball_y - (self.y + self.height // 2))
        if ball_y > self.y <= HEIGHT - self.height - 10 and not(self.y + self.speed > ball_y):
            self.y += self.speed
        elif ball_y < self.y >= 10 and not(self.y - self.speed < ball_y):
            self.y -= self.speed
        '''
        if self.y < ball_y:
            self.y += self.speed
        if self.y + self.height > ball_y:
            self.y -= self.speed

        if self.y <= 0:
           self.y = 0
        if self.y + self.height >= HEIGHT:
            self.y = HEIGHT - self.height
        '''
