# WRITE YOUR SOLUTION HERE:
import pygame, math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

angle = 0
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    n = 0.63
    radius = 135
    i = 0
    while i < 10:
        x = 320+math.cos(angle + i * n)*radius-robot.get_width()/2
        y = 240+math.sin(angle + i * n)*radius-robot.get_height()/2    
        window.blit(robot, (x, y))
        i += 1

    pygame.display.flip()

    angle += 0.01
    clock.tick(60)

