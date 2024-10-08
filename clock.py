import pygame
import math
from datetime import datetime
import sys

pygame.init()
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()  # Create a clock object
start_position = (320, 240)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((255, 255, 255))

    current_time = datetime.now()
    milliseconds = current_time.microsecond / 1000000

    # Second hand
    radius = 200
    seconds_angle = (current_time.second + milliseconds) * 6 - 90
    end_offset = [radius*math.cos(math.radians(seconds_angle)), radius*math.sin(math.radians(seconds_angle))]
    end_position = (end_offset[0] + start_position[0], end_offset[1] + start_position[1])
    pygame.draw.line(screen, (255,0,0), start_position, end_position, 2)  # Made thinner and red

    # Minute hand
    radius = 150
    minutes_angle = (current_time.minute + current_time.second / 60) * 6 - 90
    end_offset = [radius*math.cos(math.radians(minutes_angle)), radius*math.sin(math.radians(minutes_angle))]
    end_position = (end_offset[0] + start_position[0], end_offset[1] + start_position[1])
    pygame.draw.line(screen, (0,0,0), start_position, end_position, 4)
    
    # Hour hand
    radius = 100
    hours_angle = (current_time.hour % 12 + current_time.minute / 60) * 30 - 90
    end_offset = [radius*math.cos(math.radians(hours_angle)), radius*math.sin(math.radians(hours_angle))]
    end_position = (end_offset[0] + start_position[0], end_offset[1] + start_position[1])
    pygame.draw.line(screen, (0,0,0), start_position, end_position, 6)

    # Draw a circle that encompasses the lines
    max_radius = 225
    pygame.draw.circle(screen, (0,0,0), start_position, max_radius, 1)
    
    # Draw lines every 30 degrees
    for angle in range(0, 360, 30):
        end_offset = [max_radius*0.9*math.cos(math.radians(angle)), max_radius*0.9*math.sin(math.radians(angle))]
        end_position = (start_position[0] + end_offset[0], start_position[1] + end_offset[1])
        direction = [start_position[0] - end_position[0], start_position[1] - end_position[1]]
        direction_length = math.hypot(direction[0], direction[1])
        direction = [direction[0] / direction_length, direction[1] / direction_length]
        new_end_position = (end_position[0] + direction[0] * max_radius * 0.1, end_position[1] + direction[1] * max_radius * 0.1)
        pygame.draw.line(screen, (0,0,0), end_position, new_end_position, 3)

    pygame.display.flip()
    clock.tick(60)  # Limit the frame rate to 60 FPS

pygame.quit()
sys.exit()