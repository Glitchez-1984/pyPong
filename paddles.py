import pygame
import controls


class Paddle:
    def __init__(self, height, x, y, speed, is_wa, color):
        self.height = height
        self.width = 15
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.movement = {"up": pygame.K_UP, "down": pygame.K_DOWN}
        if is_wa:
            self.movement = {"up": pygame.K_w, "down": pygame.K_s}

    def draw(self, win):
        paddle_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, self.color, paddle_rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[self.movement["up"]] and self.y >= 10:
            self.y -= self.speed
        elif keys[self.movement["down"]] and self.y <= controls.HEIGHT - self.height - 10:
            self.y += self.speed
