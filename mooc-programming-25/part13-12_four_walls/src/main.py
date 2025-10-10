# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x = 0
y = 480-robot.get_height()

upwards = False
downwards = False
to_right = False
to_left = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                upwards = True
            if event.key == pygame.K_DOWN:
                downwards = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                upwards = False
            if event.key == pygame.K_DOWN:
                downwards = False


        if event.type == pygame.QUIT:
            exit()

    
    if to_right:
        if x+robot.get_width()+2 >= 640:
            to_right = False
        else:
            x += 2
    if to_left:
        if x-2 <= 0:
            to_left = False
        else:
            x -= 2
    if upwards:
        if y-2 <= 0:
            upwards = False
        else:
            y -= 2
    if downwards:
        if y+robot.get_height()+2 >= 480:
            downwards = False
        else:
            y += 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)