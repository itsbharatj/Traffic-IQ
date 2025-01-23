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
    # Route([(1210,0),(1210.0, 480.0), (1213.8060233744357, 499.13417161825447), (1224.6446609406726, 515.3553390593274), (1240.8658283817456, 526.1939766255643), (1260.0, 530.0),(1920,530)]),  # TOP : Left turn : from top to right
    # Route([(1920,830),(910,830),(910,0)])

    # TOP TO LEFT
    Route([(1010, 0), (1010.0, 480.0), (1007.8, 519.19), (1001.22, 557.88), (990.36, 595.6), (975.34, 631.86), (956.35, 666.21), (933.64, 698.22), (907.49, 727.49), (878.22, 753.64), (846.21, 776.35), (811.86, 795.34), (775.6, 810.36), (737.88, 821.22), (699.19, 827.8), (660.0, 830.0), (0, 830)]),
    Route([(1110, 0), (1110.0, 480.0), (1107.17, 530.38), (1098.72, 580.13), (1084.75, 628.63), (1065.44, 675.25), (1041.03, 719.41), (1011.82, 760.57), (978.2, 798.2), (940.57, 831.82), (899.41, 861.03), (855.25, 885.44), (808.63, 904.75), (760.13, 918.72), (710.38, 927.17), (660.0, 930.0), (0, 930)]),
    Route([(1210, 0), (1210.0, 480.0), (1206.54, 541.58), (1196.21, 602.39), (1179.14, 661.65), (1155.53, 718.64), (1125.7, 772.62), (1090.01, 822.92), (1048.91, 868.91), (1002.92, 910.01), (952.62, 945.7), (898.64, 975.53), (841.65, 999.14), (782.39, 1016.21), (721.58, 1026.54), (660.0, 1030.0), (0, 1030)]),
    # TOP TO RIGHT
    Route([(1010, 0), (1010.0, 480.0), (1011.57, 507.99), (1016.27, 535.63), (1024.03, 562.57), (1034.76, 588.47), (1048.32, 613.01), (1064.54, 635.87), (1083.22, 656.78), (1104.13, 675.46), (1126.99, 691.68), (1151.53, 705.24), (1177.43, 715.97), (1204.37, 723.73), (1232.01, 728.43), (1260.0, 730.0), (1920, 730)]),
    Route([(1110, 0), (1110.0, 480.0), (1110.94, 496.79), (1113.76, 513.38), (1118.42, 529.54), (1124.85, 545.08), (1132.99, 559.8), (1142.73, 573.52), (1153.93, 586.07), (1166.48, 597.27), (1180.2, 607.01), (1194.92, 615.15), (1210.46, 621.58), (1226.62, 626.24), (1243.21, 629.06), (1260.0, 630.0), (1920, 630)]),
    Route([(1210, 0), (1210.0, 480.0), (1210.31, 485.6), (1211.25, 491.13), (1212.81, 496.51), (1214.95, 501.69), (1217.66, 506.6), (1220.91, 511.17), (1224.64, 515.36), (1228.83, 519.09), (1233.4, 522.34), (1238.31, 525.05), (1243.49, 527.19), (1248.87, 528.75), (1254.4, 529.69), (1260.0, 530.0), (1920, 530)]),
]

# Initialize vehicles with routes
vehicles = [
    Vehicle(960, 0, random.choice(['small', 'med', 'large']) , random.choice([RED, BLUE, GREEN, YELLOW]), random.randint(2, 4), random.choice(routes))
    for _ in range(50)
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



