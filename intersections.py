from utils import get_breakpoints, breakpoint_to_path
from road import RoadSurface

class Intersection : 
    def __init__(self, initial_bp : list, road_elements : list):
        self.road_surface = RoadSurface(road_elements)
        self.initial_breakpoints = initial_bp
        self.routes = self.get_routes()

    def get_routes (self) :
        routes = []

        for i_bp in self.initial_breakpoints :
            breakpoints = get_breakpoints(i_bp[1], i_bp[2], i_bp[3], i_bp[4])

            routes.extend([breakpoint_to_path(bp, i_bp[0]) for bp in breakpoints])

        return routes

iiser_t_initial_breakpoints = [
    ('tr', [(1010,0),(1010,480),(1260,730),(1920,730)], '+0', '-1', 3),
    ('tl', [(1010,0),(1010,480),(660,830),(0,830)], '+0', '+1', 3),
    ('rt', [(1920,830),(1260,830),(910,480),(910,0)], '+1', '-0', 3),
    ('lt', [(0,530),(660,530),(710,480),(710,0)], '+1', '+0', 3),

    # ([(1920,830),(1260,830),(660,830),(0,830)], '+', '+'),    # rl
    # ([(1920,830),(1260,830),(910,480),(910,0)], '+1', '-0'),    # lr
]

iiser_t_roads = [
    # Main Roads
    {"type": "road", "size": (0, 480, 1920, 600)},  # Horizontal road
    {"type": "road", "size": (660, 0, 600, 1080)},  # Vertical road

    # Divider Lines (Solid)
    {"type": "line", "start": (0, 780), "end": (660, 780), "dashed": False},
    {"type": "line", "start": (1260, 780), "end": (1920, 780), "dashed": False},
    {"type": "line", "start": (960, 0), "end": (960, 480), "dashed": False},
    {"type": "line", "start": (960, 0), "end": (960, 480), "dashed": False},

    # Lane Markings (Dashed)
    {"type": "line", "start": (0, 580), "end": (660, 580), "dashed": True},
    {"type": "line", "start": (0, 680), "end": (660, 680), "dashed": True},
    {"type": "line", "start": (0, 880), "end": (660, 880), "dashed": True},
    {"type": "line", "start": (0, 980), "end": (660, 980), "dashed": True},
    {"type": "line", "start": (0, 980), "end": (660, 980), "dashed": True},

    {"type": "line", "start": (1260, 580), "end": (1920, 580), "dashed": True},
    {"type": "line", "start": (1260, 680), "end": (1920, 680), "dashed": True},
    {"type": "line", "start": (1260, 880), "end": (1920, 880), "dashed": True},
    {"type": "line", "start": (1260, 980), "end": (1920, 980), "dashed": True},
    {"type": "line", "start": (1260, 980), "end": (1920, 980), "dashed": True},

    {"type": "line", "start": (860, 0), "end": (860, 480), "dashed": True},
    {"type": "line", "start": (760, 0), "end": (760, 480), "dashed": True},
    {"type": "line", "start": (1060, 0), "end": (1060, 480), "dashed": True},
    {"type": "line", "start": (1160, 0), "end": (1160, 480), "dashed": True},
    {"type": "line", "start": (1160, 0), "end": (1160, 480), "dashed": True},
]

iiser_t = Intersection(iiser_t_initial_breakpoints, iiser_t_roads)

