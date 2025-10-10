# WRITE YOUR SOLUTION HERE:
import pygame, random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

robot_x = 0
robot_y = 0

clock = pygame.time.Clock()

while True:
    max_x = robot_x + robot.get_width()
    min_x = robot_x
    max_y = robot_y + robot.get_height()
    min_y = robot_y

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if min_x <= event.pos[0] <= max_x and min_y <= event.pos[1] <= max_y:
                robot_x = random.randrange(640 - robot.get_width())
                robot_y = random.randrange(480 - robot.get_height())

        if event.type == pygame.QUIT:
            exit(0)


    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)