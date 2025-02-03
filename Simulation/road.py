import pygame

GRAY = (18, 18, 18)
WHITE = (255, 255, 255)

class RoadSurface:
    def __init__(self, elements):
        
        self.road_surfaces = []
        self.line_markings = []

        for element in elements : 
            if element["type"] == "road" :
                self.road_surfaces.append(self.Road(element["size"]))
            
            if element["type"] == "line" :
                self.line_markings.append(self.Line(element["start"], element["end"], dashed=element["dashed"]))

    def draw (self, screen) :

        for road_surface in self.road_surfaces : 
            road_surface.draw(screen)

        for line_marking in self.line_markings : 
            line_marking.draw(screen)

    class Road():
        def __init__(self, rect, color=GRAY):
            super().__init__()
            self.rect = rect
            self.color = color

        def draw(self, screen):
            pygame.draw.rect(screen, self.color, self.rect)


    class Line():
        def __init__(self, start_pos, end_pos, color=WHITE, dashed=False, dash_length=10):
            super().__init__()
            self.start_pos = start_pos
            self.end_pos = end_pos
            self.color = color
            self.dashed = dashed
            self.dash_length = dash_length

        def draw(self, screen):
            if self.dashed:
                self._draw_dashed_line(screen)
            else:
                pygame.draw.line(screen, self.color, self.start_pos, self.end_pos, 5)

        def _draw_dashed_line(self, screen):
            x1, y1 = self.start_pos
            x2, y2 = self.end_pos
            total_length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            num_dashes = int(total_length // self.dash_length)
            for i in range(0, num_dashes, 2):
                start = (
                    x1 + (x2 - x1) * (i / num_dashes),
                    y1 + (y2 - y1) * (i / num_dashes),
                )
                end = (
                    x1 + (x2 - x1) * ((i + 1) / num_dashes),
                    y1 + (y2 - y1) * ((i + 1) / num_dashes),
                )
                pygame.draw.line(screen, self.color, start, end, 2)
