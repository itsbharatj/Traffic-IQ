import pygame
import random
import math

from vehicle import Vehicle

from intersections import iiser_t
from utils import colors

# Screen dimensions
WIDTH, HEIGHT = 1920, 1080

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Intersection Simulation")
clock = pygame.time.Clock()

# # Vehicle class
# class Vehicle:
#     def __init__(self, color, route, speed):
#         self.color = color
#         self.route = route  # List of waypoints
#         self.speed = speed
#         self.current_index = 0
#         self.x, self.y = self.route.waypoints[self.current_index]  # Starting point

#     def move(self):
#         if self.current_index < len(self.route.waypoints) - 1:
#             # Get the next waypoint
#             next_x, next_y = self.route.waypoints[self.current_index + 1]

#             # Calculate the direction vector
#             dx, dy = next_x - self.x, next_y - self.y
#             distance = math.sqrt(dx**2 + dy**2)
#             if distance > 0:
#                 # Normalize the direction vector and scale by speed
#                 dx, dy = dx / distance, dy / distance
#                 self.x += dx * self.speed
#                 self.y += dy * self.speed

#             # Check if the vehicle has reached the next waypoint
#             if distance < self.speed:
#                 self.current_index += 1

#     def draw(self, screen):
#         pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 10)

# Function to spawn vehicles
def spawn_vehicle():
    color = random.choice(colors)
    route = random.choice(iiser_t.routes)
    speed = random.uniform(2, 5)  # Random speed between 2 and 5
    return Vehicle(color, route, speed)

# Main simulation loop
running = True
vehicles = [spawn_vehicle() for _ in range(10)]  # Spawn initial 10 vehicles

# # Drawing the Road Markings.
# iiser_t.road_surface.draw(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the road markings
    iiser_t.road_surface.draw(screen)

    # Update and draw each vehicle
    for vehicle in vehicles:
        vehicle.move(vehicles)
        vehicle.draw(screen)

    # Randomly spawn a new vehicle with a small probability
    if random.random() < 0.08:  # 2% chance to spawn a vehicle each frame
        vehicles.append(spawn_vehicle())

    # Remove vehicles that have completed their routes
    vehicles = [v for v in vehicles if v.current_index < len(v.route.waypoints) - 1]

    # Update the display
    pygame.display.flip()
    clock.tick(140)

pygame.quit()
