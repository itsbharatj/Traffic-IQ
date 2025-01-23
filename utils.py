import math

def arc_points(start, end, num_points=5, flip=False):
    """
    Generate points on an arc between two points, flipping the arc across the joining line if needed.

    Args:
        start (tuple): Start point (x1, y1).
        end (tuple): End point (x2, y2).
        radius (float): Radius of the arc.
        num_points (int): Number of points on the arc.
        flip (bool): Whether to flip the arc across the line joining the two points.

    Returns:
        list: List of tuples representing points on the arc.
    """
    x1, y1 = start
    x2, y2 = end

    radius = abs(x1-x2)

    end, start = start, end

    # Midpoint of the line segment
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2

    # Distance between start and end points
    chord_length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Height of the arc from the midpoint
    height = math.sqrt(radius**2 - (chord_length / 2)**2)

    # Perpendicular direction vector
    dx, dy = x2 - x1, y2 - y1
    perp_dx, perp_dy = -dy, dx
    perp_length = math.sqrt(perp_dx**2 + perp_dy**2)
    perp_dx /= perp_length
    perp_dy /= perp_length

    # Original center of the arc
    cx, cy = mx + height * perp_dx, my + height * perp_dy

    # Flip the center across the line joining the two points if needed
    if flip:
        # Reflect the center across the line
        line_dx, line_dy = x2 - x1, y2 - y1
        line_length = math.sqrt(line_dx**2 + line_dy**2)
        line_dx /= line_length
        line_dy /= line_length

        # Projection of the center onto the line
        proj_length = (cx - x1) * line_dx + (cy - y1) * line_dy
        proj_x = x1 + proj_length * line_dx
        proj_y = y1 + proj_length * line_dy

        # Reflect the center
        cx, cy = 2 * proj_x - cx, 2 * proj_y - cy

    # Start and end angles
    start_angle = math.atan2(y1 - cy, x1 - cx)
    end_angle = math.atan2(y2 - cy, x2 - cx)

    # Ensure counterclockwise arc
    if end_angle < start_angle:
        end_angle += 2 * math.pi

    # Generate equally spaced points
    angle_step = (end_angle - start_angle) / (num_points - 1)
    points = [
        (
            cx + radius * math.cos(start_angle + i * angle_step),
            cy + radius * math.sin(start_angle + i * angle_step)
        )
        for i in range(num_points)
    ]

    return points

# # Example usage
# start = (1210, 480)
# end = (1260,530)

# start, end = end, start


# # Original arc
# print("Original Arc:")
# arc1 = arc_points(start, end, radius)
# print(list(reversed(arc1)))


# # Flipped arc
# print("\nFlipped Arc:")
# arc2 = arc_points(start, end, radius, flip=True)
# print(arc2)





def draw_path (start_point : tuple, end_point : tuple) : 
    
    if start_point == end_point : return 0
    if not start_point or not end_point : return -1

    draw_line ()
    draw_arc ()
    draw_line ()