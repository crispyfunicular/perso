# WRITE YOUR SOLUTION HERE:
import pygame, math
from datetime import datetime

pygame.init()
display = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

x_center = 640/2
y_center = 480/2
radius = 200

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
        # Reset display
    display.fill((0, 0, 0))

    now = datetime.now()

    # Display inner circle
    pygame.draw.circle(display, (255, 0, 0), [x_center, y_center], 10)

    # Display outer circle
    pygame.draw.circle(display, (255, 0, 0), [x_center, y_center], radius, 5)

    # Display hour needle
    radius_hours = radius - 50
    angle_hours = -math.pi/2 + (2 * math.pi / 12) * now.hour
    x_hours = x_center + radius_hours * math.cos(angle_hours)
    y_hours = y_center + radius_hours * math.sin(angle_hours)
    pygame.draw.line(display, (0, 0, 255), (x_center, y_center), (x_hours, y_hours), 4)

    # Display minute needle
    radius_minutes = radius - 20
    angle_minutes = -math.pi/2 + (2 * math.pi / 60) * now.minute
    x_minutes = x_center + radius_minutes * math.cos(angle_minutes)
    y_minutes = y_center + radius_minutes * math.sin(angle_minutes)
    pygame.draw.line(display, (0, 0, 255), (x_center, y_center), (x_minutes, y_minutes), 2)

    # Display second needle
    radius_seconds = radius - 20
    angle_seconds = -math.pi/2 + (2 * math.pi / 60) * now.second
    x_seconds = x_center + radius_seconds * math.cos(angle_seconds)
    y_seconds = y_center + radius_seconds * math.sin(angle_seconds)
    #print(f"{x_seconds} = {x_center} + {radius_seconds} * {math.cos(angle_seconds)}")
    pygame.draw.line(display, (0, 0, 255), (x_center, y_center), (x_seconds, y_seconds), 1)

    # Display new image
    pygame.display.flip()
    
    # Wait one second to display the next image
    clock.tick(1)