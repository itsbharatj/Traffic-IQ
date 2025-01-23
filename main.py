# import pygame
# import sys
# from road import draw_road, draw_dashed_line
# from vehicle import Vehicle
# from lights import TrafficSignal

# # Initialize Pygame
# pygame.init()

# # Screen dimensions
# WIDTH, HEIGHT = 1920, 1080

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Traffic Simulation")

# # Colors
# WHITE = (255, 255, 255)

# # Clock for controlling frame rate
# clock = pygame.time.Clock()

# # Main game loop
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     # Fill background
#     screen.fill(WHITE)

#     # Draw roads and dashed lines
#     draw_road(screen)

#     # Update display
#     pygame.display.flip()
#     clock.tick(60)  # 60 FPS


import pygame
import random

# Colors
GRAY = (50, 50, 50)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Screen dimensions
WIDTH, HEIGHT = 1920, 1080

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Intersection Simulation with Routes")
clock = pygame.time.Clock()

from road import draw_road
draw_road(screen)


class Route:
    def __init__(self, waypoints):
        self.waypoints = waypoints

class Vehicle:
    def __init__(self, x, y, size, color, speed, route):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = speed
        self.route = route
        self.current_waypoint_index = 0

    def move(self):
        if self.current_waypoint_index < len(self.route.waypoints):
            target_x, target_y = self.route.waypoints[self.current_waypoint_index]
            dx, dy = target_x - self.x, target_y - self.y
            dist = (dx**2 + dy**2) ** 0.5
            if dist < self.speed:
                self.x, self.y = target_x, target_y
                self.current_waypoint_index += 1
            else:
                self.x += self.speed * dx / dist
                self.y += self.speed * dy / dist

    def draw(self, screen):
        side = {'small':15, 'med':25, 'large':40}.get(self.size)
        pygame.draw.rect(screen, self.color, (self.x, self.y, side, side))

# Define routes (list of waypoints)
routes = [
    Route([(1210,0),(1210.0, 480.0), (1213.8060233744357, 499.13417161825447), (1224.6446609406726, 515.3553390593274), (1240.8658283817456, 526.1939766255643), (1260.0, 530.0),(1920,530)]),  # TOP : Left turn : from top to right
    Route([(1920,830),(910,830),(910,0)])
]

# Initialize vehicles with routes
vehicles = [
    Vehicle(960, 0, random.choice(['small', 'med', 'large']) , random.choice([RED, BLUE, GREEN, YELLOW]), random.randint(2, 4), random.choice(routes))
    for _ in range(10)
]

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))
    draw_road(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for vehicle in vehicles:
        vehicle.move()
        if vehicle.current_waypoint_index >= len(vehicle.route.waypoints):
            vehicles.remove(vehicle)  # Remove vehicle after completing route
            continue
        vehicle.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()



