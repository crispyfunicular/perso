# WRITE YOUR SOLUTION HERE:
import pygame, math

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")

x = 640/2 - ball.get_width()/2
y = 480/2 - ball.get_height()/2
velocity = 1
dir_x = 1
dir_y = 1
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    ### REBOUND ###

    #up/down wall
    if y == 0 or y+ball.get_height() >= 480:
        dir_y *= -1

    #left/right wall
    if x == 0 or x+ball.get_width() >= 640:
        dir_x *= -1


    ### MOVE ###
    x = x + dir_x * velocity
    y = y + dir_y * velocity

    
    window.blit(ball, (x, y))
    pygame.display.flip()

    clock.tick(120)

