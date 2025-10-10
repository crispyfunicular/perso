# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot_player1 = pygame.image.load("robot.png")
x_player1 = 0
y_player1 = 480-robot_player1.get_height()

robot_player2 = pygame.image.load("robot.png")
x_player2 = 640/2
y_player2 = (480-robot_player1.get_height())/2

to_right_player1 = False
to_left_player1 = False
upwards_player1 = False
downwards_player1 = False

to_right_player2 = False
to_left_player2 = False
upwards_player2 = False
downwards_player2 = False

clock = pygame.time.Clock()

while True:
    #Player 1
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left_player1 = True
            if event.key == pygame.K_RIGHT:
                to_right_player1 = True
            if event.key == pygame.K_UP:
                upwards_player1 = True
            if event.key == pygame.K_DOWN:
                downwards_player1 = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left_player1 = False
            if event.key == pygame.K_RIGHT:
                to_right_player1 = False
            if event.key == pygame.K_UP:
                upwards_player1 = False
            if event.key == pygame.K_DOWN:
                downwards_player1 = False


        #Player 2
        if event.type == pygame.KEYDOWN:
            #left (with French keyboard AZERTY)
            if event.key == pygame.K_q:
                to_left_player2 = True
            #right
            if event.key == pygame.K_d:
                to_right_player2 = True
            #up (with French keyboard AZERTY)
            if event.key == pygame.K_z:
                upwards_player2 = True
            #down
            if event.key == pygame.K_s:
                downwards_player2 = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                to_left_player2 = False
            if event.key == pygame.K_d:
                to_right_player2 = False
            if event.key == pygame.K_z:
                upwards_player2 = False
            if event.key == pygame.K_s:
                downwards_player2 = False


        if event.type == pygame.QUIT:
            exit()

    
    #Player 1
    if to_right_player1:
        if x_player1+robot_player1.get_width()+2 >= 640:
            to_right_player1 = False
        else:
            x_player1 += 2
    if to_left_player1:
        if x_player1-2 <= 0:
            to_left_player1 = False
        else:
            x_player1 -= 2
    if upwards_player1:
        if y_player1-2 <= 0:
            upwards_player1 = False
        else:
            y_player1 -= 2
    if downwards_player1:
        if y_player1+robot_player1.get_height()+2 >= 480:
            downwards_player1 = False
        else:
            y_player1 += 2

    #Player 2
    if to_right_player2:
        if x_player2+robot_player2.get_width()+2 >= 640:
            to_right_player2 = False
        else:
            x_player2 += 2
    if to_left_player2:
        if x_player2-2 <= 0:
            to_left_player2 = False
        else:
            x_player2 -= 2
    if upwards_player2:
        if y_player2-2 <= 0:
            upwards_player2 = False
        else:
            y_player2 -= 2
    if downwards_player2:
        if y_player2+robot_player2.get_height()+2 >= 480:
            downwards_player2 = False
        else:
            y_player2 += 2


    window.fill((0, 0, 0))
    window.blit(robot_player1, (x_player1, y_player1))
    window.blit(robot_player2, (x_player2, y_player2))
    pygame.display.flip()

    clock.tick(60)
