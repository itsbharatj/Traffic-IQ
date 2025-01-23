import pygame

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

class TrafficSignal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = "RED"  # Initial state
        self.timer = 0

    def update(self):
        self.timer += 1
        if self.timer > 100:  # Example: Change every 100 frames
            if self.state == "RED":
                self.state = "GREEN"
            elif self.state == "GREEN":
                self.state = "YELLOW"
            elif self.state == "YELLOW":
                self.state = "RED"
            self.timer = 0

    def draw(self, screen):
        color = RED if self.state == "RED" else GREEN if self.state == "GREEN" else YELLOW
        pygame.draw.circle(screen, color, (self.x, self.y), 20)
