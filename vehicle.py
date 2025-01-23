import pygame, random, math

class Vehicle:
    def __init__(self, color, route, speed):
        self.color = color
        self.route = route  # List of waypoints
        self.speed = speed  # Speed in km/h
        self.current_index = 0
        self.x, self.y = self.route.waypoints[self.current_index]  # Starting point
        self.speed_per_frame = self.convert_speed_to_pixels_per_frame(speed)

    def convert_speed_to_pixels_per_frame(self, speed_kmh):
        """
        Convert the speed from km/h to pixels per frame.
        """
        frame_rate = 140  # Assuming 60 FPS
        # Convert speed to meters per second
        speed_mps = 100 * (speed_kmh * 1000) / 3600
        # Convert speed to pixels per frame based on frame rate
        return speed_mps / frame_rate

    def move(self, vehicles):
        """
        Move the vehicle along the route.
        Adjust speed if there's a slower vehicle ahead.
        """
        # Check if there is any vehicle ahead within a certain range (e.g., 30px)
        vehicle_in_front = self.check_vehicle_in_front(vehicles, distance_threshold=30)

        if vehicle_in_front:
            # If the vehicle ahead is slower, reduce speed
            if vehicle_in_front.speed < self.speed:
                self.adjust_speed(vehicle_in_front)

        if self.current_index < len(self.route.waypoints) - 1:
            # Get the next waypoint
            next_x, next_y = self.route.waypoints[self.current_index + 1]

            # Calculate the direction vector
            dx, dy = next_x - self.x, next_y - self.y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            if distance > 0:
                # Normalize the direction vector and scale by speed
                dx, dy = dx / distance, dy / distance
                self.x += dx * self.speed_per_frame
                self.y += dy * self.speed_per_frame

            # Check if the vehicle has reached the next waypoint
            if distance < self.speed_per_frame:
                self.current_index += 1

    def check_vehicle_in_front(self, vehicles, distance_threshold=100):
        """
        Check if there is a vehicle ahead within a given distance threshold.
        """
        for vehicle in vehicles:
            if vehicle != self and vehicle.current_index > self.current_index:
                # Calculate the distance to the vehicle in front
                next_x, next_y = vehicle.route.waypoints[vehicle.current_index]
                dx, dy = next_x - self.x, next_y - self.y
                distance_to_vehicle = math.sqrt(dx**2 + dy**2)

                # If the vehicle is within the threshold distance, return it
                if distance_to_vehicle <= distance_threshold:
                    return vehicle
        return None

    def adjust_speed(self, vehicle_in_front):
        """
        Adjust the speed based on the vehicle in front.
        If the vehicle ahead is slower, reduce speed.
        """
        # Reduce speed to match the vehicle in front's speed, but not increase it above its own max
        self.speed = max(vehicle_in_front.speed, self.speed - 1)  # Reduce speed by 1 km/h for example
        self.speed_per_frame = self.convert_speed_to_pixels_per_frame(self.speed)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 10)
