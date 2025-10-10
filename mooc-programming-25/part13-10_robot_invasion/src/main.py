# WRITE YOUR SOLUTION HERE:
import pygame, random

robots_lst = []

class Robot:
    def __init__(self):
        self.x = random.randint(0, 590)
        self.y = 0
        self.velocity = 1
        self.direction = "downwards"
        self.count = 0

    def move(self):
        if self.direction == "downwards":
            self.y += self.velocity
        if self.direction == "right":
            self.x += self.velocity
        if self.direction == "left":
            self.x -= self.velocity

    def turning(self):
        choice = random.randint(0, 1)
        if choice == 0:
            self.direction = "right"
        elif choice == 1:
            self.direction = "left"


pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    # Creates robots
    if random.randint(0, 100) == 1:
        robot_obj = Robot()
        robots_lst.append(robot_obj)

    # Displays image
    window.fill((0, 0, 0))
    for r in robots_lst:
        window.blit(robot, (r.x, r.y))
    pygame.display.flip()

    # Moves robots
    for r in robots_lst:
        r.move()
        if r.y+robot.get_height() >= 480 and r.count == 0:
            r.turning()
            r.count = 1

    clock.tick(60)