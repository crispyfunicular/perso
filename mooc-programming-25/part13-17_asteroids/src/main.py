# WRITE YOUR SOLUTION HERE:
import pygame, random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")

clock = pygame.time.Clock()

asteroids_lst = []

points = 0     


class Robot:
    def __init__(self):
        self.x = 0
        self.y = 480-robot.get_height()
        self.velocity = 3
        self.right = False
        self.left = False

    def get_direction(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.left = True
            if event.key == pygame.K_RIGHT:
                self.right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.left = False
            if event.key == pygame.K_RIGHT:
                self.right = False

    def move(self):
        if self.right:
            self.x += self.velocity
        if self.left:
            self.x -= self.velocity

        if self.x < 0:
            self.x = 0
        if self.x + robot.get_width() > 640:
            self.x = 640 - robot.get_width()

    def get_right(self):
        return self.x + robot.get_width()
    
    def get_left(self):
        return self.x
    
    def get_top(self):
        return self.y


class Asteroid:
    def __init__(self):
        # Asteroid starts at a random x position
        self.x = random.randint(0, 590)

        # Asteroid always starts the the top of the screen
        self.y = 0
        
        # Speed of the fall
        self.velocity = 1

        self.displayed = True

    # Exits when the asteroid reaches the ground
    def reach_ground(self):
        if self.y + rock.get_height() == 480:
            exit()

    def fall(self):
        self.y += self.velocity

    def collision(self, robocop: Robot):
        max_y = self.y + rock.get_height()
        max_x = self.x + rock.get_width()
        min_x = self.x
        robot_top = robocop.y
        if max_y >= robot_top:
            if robocop.get_left() < max_x < robocop.get_right() or robocop.get_left() < min_x < robocop.get_right():
                self.displayed = False
                return True


robocop = Robot()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        # Changes the direction of the robot maybe if an event occurs
        robocop.get_direction(event)
    
    # Move the robot
    robocop.move()

    # Creates asteroid
    if random.randint(0, 150) == 1:
        asteroid_obj = Asteroid()
        asteroids_lst.append(asteroid_obj)
    
    # Makes asteroids fall
    for a in asteroids_lst:
        if a.displayed:
            a.fall()
            a.reach_ground()
            if a.collision(robocop):
                points += 1

    # Removes the destroyed asteroid from the list (could have used a "remove" method instead)
    asteroids_lst = [a for a in asteroids_lst if a.displayed]

    # Reset image
    window.fill((0, 0, 0))

    # Display robot
    window.blit(robot, (robocop.x, robocop.y))
    
    # Display asteroids
    for a in asteroids_lst:
        window.blit(rock, (a.x, a.y))
    
    game_font = pygame.font.SysFont("Arial", 24)
    text = game_font.render(f"Points: {points}", True, (255, 0, 0))
    window.blit(text, (520, 10))

    pygame.display.flip()

    clock.tick(60)
