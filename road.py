import pygame

GRAY = (18, 18, 18)
WHITE = (255, 255, 255)

def draw_dashed_line(screen, color, start_pos, end_pos, dash_length=10):
    x1, y1 = start_pos
    x2, y2 = end_pos
    total_length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    num_dashes = int(total_length // dash_length)
    for i in range(0, num_dashes, 2):
        start = (
            x1 + (x2 - x1) * (i / num_dashes),
            y1 + (y2 - y1) * (i / num_dashes),
        )
        end = (
            x1 + (x2 - x1) * ((i + 1) / num_dashes),
            y1 + (y2 - y1) * ((i + 1) / num_dashes),
        )
        pygame.draw.line(screen, color, start, end, 2)

def draw_road(screen):

    # Main Roads...
    pygame.draw.rect(screen, GRAY, (0,480,1920,600))  # Horizontal road
    pygame.draw.rect(screen, GRAY, (660,0,600,1080))  # Vertical road

    # Divider Lines
    pygame.draw.line(screen, WHITE,(0,780),(660,780), 5)
    pygame.draw.line(screen, WHITE,(1260,780),(1920,780), 5)
    pygame.draw.line(screen, WHITE,(960,0),(960,480), 5)

    # Lane Markings
    draw_dashed_line(screen, WHITE, (0,580), (660,580))
    draw_dashed_line(screen, WHITE, (0,680), (660,680))
    draw_dashed_line(screen, WHITE, (0,880), (660,880))
    draw_dashed_line(screen, WHITE, (0,980), (660,980))
    
    draw_dashed_line(screen, WHITE, (1260,580), (1920,580))
    draw_dashed_line(screen, WHITE, (1260,680), (1920,680))
    draw_dashed_line(screen, WHITE, (1260,880), (1920,880))
    draw_dashed_line(screen, WHITE, (1260,980), (1920,980))

    draw_dashed_line(screen, WHITE, (860,0), (860,480))
    draw_dashed_line(screen, WHITE, (760,0), (760,480))
    draw_dashed_line(screen, WHITE, (1060,0), (1060,480))
    draw_dashed_line(screen, WHITE, (1160,0), (1160,480))