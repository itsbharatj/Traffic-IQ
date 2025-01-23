import pygame

class Vehicle:
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.width = 40
        self.height = 20

    def move(self, stop=False):
        if not stop:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
