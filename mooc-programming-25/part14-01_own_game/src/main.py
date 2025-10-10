# Complete your game here
import pygame, random


class Robot:
    def __init__(self):
        self.image = pygame.image.load("robot.png")
        self.x = (1280 - self.image.get_width())/2
        self.y = (960 - self.image.get_height())/2
    
    def get_x_y(self):
        self.min_x = self.x
        self.min_y = self.y
        self.max_x = self.x + self.image.get_width()
        self.max_y = self.y + self.image.get_height()
        return self.min_x, self.min_y, self.max_x, self.max_y

    def move(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.x = event.pos[0]-self.image.get_width()/2
            self.y = event.pos[1]-self.image.get_height()/2


class Monster():
    def __init__(self):
        self.image = pygame.image.load("monster.png")
        # Monster starts at a random position
        self.x = random.randint(0, 1280-self.image.get_width())
        self.y = random.randint(0, 590-self.image.get_height())
        self.min_x = self.x
        self.min_y = self.y
        self.max_x = self.x + self.image.get_width()
        self.max_y = self.y + self.image.get_height()
                       
        self.velocity = 1
  
    def appear(self):
        if random.randint(0, 500) == 1:
            return Monster()

"""
    def move(self):
        #to be done
        self.y += self.velocity

    def rebound(self):
        #to be done
        if self.y + self.image.get_height() == 960:
            exit()

    def collision(self, robocop: Robot):
        #to be done
        max_y = self.y + self.image.get_height()
        max_x = self.x + self.image.get_width()
        min_x = self.x
        robot_top = robocop.y
        if max_y >= robot_top:
            if robocop.get_left() < max_x < robocop.get_right() or robocop.get_left() < min_x < robocop.get_right():
                self.displayed = False
                return True
"""

class Coin():
    def __init__(self):
        self.image = pygame.image.load("coin.png")
        # Coin appears at random x and y positions  
        self.limit_x = 1280 - self.image.get_width()
        self.limit_y = 960 - self.image.get_height()
        self.x = random.randint(0, self.limit_x)
        self.y = random.randint(0, self.limit_y)    

        self.collected = False

    def get_x_y(self):
        self.min_x = self.x
        self.min_y = self.y
        self.max_x = self.x + self.image.get_width()
        self.max_y = self.y + self.image.get_height()
        return self.min_x, self.min_y, self.max_x, self.max_y

    def appear(self):
        if random.randint(0, 500) == 1:
            return Coin()

    def collect(self, robot: Robot):
        self.min_x, self.min_y, self.max_x, self.max_y = self.get_x_y()
        robot.min_x, robot.min_y, robot.max_x, robot.max_y = robot.get_x_y()
        
        print(f"{robot.min_x} < {self.min_x} < {robot.max_x} or {robot.min_x} < {self.max_x} < {robot.max_x}")
        if robot.min_x < self.min_x < robot.max_x or robot.min_x < self.max_x < robot.max_x:
            print("test_x ok")
            print(f"{robot.min_y} < {self.min_y} < {robot.max_y} or {robot.min_y} < {self.max_y} < {robot.max_y}")
            if robot.min_y < self.min_y < robot.max_y or robot.min_y < self.max_y < robot.max_y:
                print("collected")
                self.collected = True
        
    def disappear(self):
        pass


class Game:
    def __init__(self):
        self.points = 0
        self.robot = Robot()
        self.monster = Monster()
        self.monsters = []
        self.coin = Coin()
        self.coins = []
        #self.monster = Monster()

        pygame.init()
        self.window = pygame.display.set_mode((1280, 960))
        pygame.display.set_caption("Morgane's Game")

        self.main_loop()


    """

    def collision(self, robot: Robot, monster: Monster):
        max_y_robot = robot.y + robot.image.get_height()
        max_x_robot = robot.x + robot.image.get_width()
        min_x = self.x
        robot_top = robot.y
        if max_robot_y >= robot_top:
            if robot.get_left() < max_x < robot.get_right() or robot.get_left() < min_x < robot.get_right():
                exit()
    """
      
        
    def main_loop(self):
        while True:
            for event in pygame.event.get():
                self.robot.move(event)
                if event.type == pygame.QUIT:
                    exit()
            monster = self.monster.appear()
            if monster:
                self.monsters.append(monster)
            coin = self.coin.appear()
            if coin:
                self.coins.append(coin)
            self.coin.collect(self.robot)
            self.draw_window()

    def draw_window(self):
        self.window.fill((100, 100, 100))
        self.window.blit(self.robot.image, (self.robot.x, self.robot.y))
        for m in self.monsters:
            self.window.blit(m.image, (m.x, m.y))
        for c in self.coins:
            self.window.blit(c.image, (c.x, c.y))
            if c.collected:
                self.coins.remove(c)
                self.point += 1
        
        #Points
        game_font = pygame.font.SysFont("Arial", 24)
        text = game_font.render(f"Points: {self.points}", True, (255, 0, 0))
        self.window.blit(text, (1150, 10))

        pygame.display.flip()


if __name__ == "__main__":
    Game()