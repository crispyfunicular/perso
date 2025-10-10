# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))

x_start = 40
y_start = 80
count_y = 0

while count_y < 10:
    x_start += 10
    y_start += 20
    x = x_start
    y = y_start
    count_x = 0

    while count_x < 10:        
        window.blit(robot, (x, y))
        x += 40
        count_x += 1

    count_y += 1
      
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()