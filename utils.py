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
            round(cx + radius * math.cos(start_angle + i * angle_step), 2),
            round(cy + radius * math.sin(start_angle + i * angle_step), 2)
        )
        for i in range(num_points)
    ]

    return points

def draw_arc (start, end, form) :

    if form == 'tr' : 
        arc = arc_points(end, start, 15, False)
        arc.reverse()

    elif form == 'tl': 
        arc = arc_points(start, end, 15, False)



    return arc

def breakpoint_to_path (breakpoints, arc_form) : 
    for i in breakpoints : 
        path = [i[0]]
        path.extend(draw_arc(i[1],i[2],arc_form))
        path.append(i[3])

        print(f"Route({path}),")

def get_breakpoints (path_points, s0 : str, s1 : str) :
    
    breaks = []

    for i in range(0,300,100) :

        tup_form_1 = lambda tup : (tup[0] + i, tup[1]) 
        tup_form_2 = lambda tup : (tup[0] - i, tup[1]) 
        tup_form_3 = lambda tup : (tup[0], tup[1] + i) 
        tup_form_4 = lambda tup : (tup[0], tup[1] - i) 

        def update_tup (tup, mod) :

            if mod[0] == "+" : 
                if mod[1] == '0' :
                    tup = tup_form_1(tup)
                if mod[1] == '1' :
                    tup = tup_form_3(tup)

            elif mod[0] == "-" : 
                if mod[1] == '0' :
                    tup = tup_form_2(tup)
                if mod[1] == '1' :
                    tup = tup_form_4(tup)
            else :
                raise ValueError

            # print(tup, mod)
            return tup
        
        breaks.append([update_tup(tup, s0 if idx < 2 else s1) for idx, tup in enumerate(path_points)])
        
        
    return breaks
    

initial_breakpoints = [
    ([(1010,0),(1010,480),(1260,730),(1920,730)], '+0', '-1'),    # tl
    ([(1010,0),(1010,480),(660,830),(0,830)], '+0', '+1'),    # tr
    # ([(1920,830),(1260,830),(660,830),(0,830)], '+', '+'),    # rl
    ([(1920,830),(1260,830),(910,480),(910,0)], '+1', '-0'),    # rt
    ([(0,1030),(660,1030),(910,480),(910,0)], '-1', '-0'),    # lt
    # ([(1920,830),(1260,830),(910,480),(910,0)], '+1', '-0'),    # lr
]

for i_bp in initial_breakpoints : 
    breakpoints = get_breakpoints(i_bp[0], i_bp[1], i_bp[2])
    paths = [breakpoint_to_path(bp) for bp in breakpoints]