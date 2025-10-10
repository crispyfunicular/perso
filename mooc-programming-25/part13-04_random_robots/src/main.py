# WRITE YOUR SOLUTION HERE:
import random, pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))

count = 0
while count < 1001:
    x = random.randint(0, 590)
    y = random.randint(0, 400)
    window.blit(robot, (x, y))
    count += 1
      
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()