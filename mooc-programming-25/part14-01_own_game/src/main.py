# The robot (stuck to the mouse) must collect coins to gain points,
# while avoiding the monsters (ghosts),
# which can move either upwards, downwards, to the left or the the right.
# In case a collision with a monster happens, the game ends.
# Both the coins and the robots appear randomly.


import pygame, random
from random import randint, choice

class Image():
    def __init__(self, image):
        self.image = pygame.image.load(image)
        self.x = randint(0, 1280-self.image.get_width())
        self.y = randint(0, 960-self.image.get_height())

    def get_x_y(self):
        self.min_x = self.x
        self.min_y = self.y
        self.max_x = self.x + self.image.get_width()
        self.max_y = self.y + self.image.get_height()
        return self.min_x, self.min_y, self.max_x, self.max_y

    def collision(self, image):
        min_x, min_y, max_x, max_y = self.get_x_y()
        Image.min_x, image.min_y, image.max_x, image.max_y = image.get_x_y()
        
        if image.min_x < min_x < image.max_x or image.min_x < max_x < image.max_x:
            if image.min_y < min_y < image.max_y or image.min_y < max_y < image.max_y:
                return True


class Robot(Image):
    def __init__(self):
        super().__init__("robot.png")  

    def move(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.x = event.pos[0]-self.image.get_width()/2
            self.y = event.pos[1]-self.image.get_height()/2


class Monster(Image):
    def __init__(self):
        super().__init__("monster.png")
                     
        self.velocity = randint(1,3)
        self.direction = choice(["left", "right", "up", "down"])
        if self.direction in ["left", "right"]:
            self.x = 0
        else:
            self.y = 0

    @staticmethod
    def appear():
        if random.randint(0, 600) == 1:
            return Monster()

    def move(self):
        min_x, min_y, max_x, max_y = self.get_x_y()

        if self.direction == "left":
            self.x -= self.velocity
            if min_x <= 0:
                self.direction = "right"
        elif self.direction == "right":
            self.x += self.velocity
            if max_x >= 1280:
                self.direction = "left"
        elif self.direction == "up":            
            self.y -= self.velocity
            if min_y <= 0:
                self.direction = "down"
        elif self.direction == "down":         
            self.y += self.velocity
            if max_y >= 960:
                self.direction = "up"


class Coin(Image):
    def __init__(self):
        super().__init__("coin.png")

    @staticmethod
    def appear():
        if random.randint(0, 400) == 1:
            return Coin()


class Game:
    def __init__(self):
        self.points = 0
        self.robot = Robot()
        self.monsters = []
        self.coins = []

        pygame.init()
        self.window = pygame.display.set_mode((1280, 960))
        pygame.display.set_caption("Morgane's Game")

        self.main_loop()
            
    def main_loop(self):
        while True:
            for event in pygame.event.get():
                self.robot.move(event)
                if event.type == pygame.QUIT:
                    exit()

            # Monsters
            monster = Monster.appear()
            if monster:
                self.monsters.append(monster)
            for m in self.monsters:
                m.move()
                if m.collision(self.robot):
                    exit()
            
            # Coins
            coin = Coin.appear()
            if coin:
                self.coins.append(coin)
            for c in self.coins:
                c.collision(self.robot)
            
            # Display image
            self.draw_window()

    def draw_window(self):
        self.window.fill((100, 100, 100))
        self.window.blit(self.robot.image, (self.robot.x, self.robot.y))
        for m in self.monsters:
            self.window.blit(m.image, (m.x, m.y))
        for c in self.coins:
            self.window.blit(c.image, (c.x, c.y))
            if c.collision(self.robot):
                self.coins.remove(c)
                self.points += 1
        
        #Points
        game_font = pygame.font.SysFont("Arial", 24)
        text = game_font.render(f"Points: {self.points}", True, (255, 0, 0))
        self.window.blit(text, (1150, 10))

        pygame.display.flip()


if __name__ == "__main__":
    Game()