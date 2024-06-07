import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

# DONE: Create a Ball class.
# DONE: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# DONE: Methods: __init__, draw, move

class Ball:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed_x = random.randint(5, 8)
        self.speed_y = random.randint(5, 8)
        self.radius = random.randint(5, 45)
        self.color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))


    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.y = self.y + self.speed_y
        self.x = self.x + self.speed_x
        if self.y > self.screen.get_height() + self.radius or self.y < 0 + self.radius:
            self.speed_y = -1*self.speed_y
        if self.x > self.screen.get_width() + self.radius or self.x < 0 + self.radius:
            self.speed_x = -1*self.speed_x
        if self.x > self.screen.get_width() - self.radius or self.x < 0 - self.radius:
            self.speed_x = -1*self.speed_x
        if self.y > self.screen.get_width() - self.radius or self.y < 0 - self.radius:
            self.speed_y = -1*self.speed_y




def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    # DONE: Create an instance of the Ball class called ball1
    ball1 = Ball(screen, 300, 50)

    list = []
    list.append(ball1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_SPACE]:
                    ball1.speed_x = 0*ball1.speed_x
                    ball1.speed_y = 0*ball1.speed_y
            if pressed_keys[pygame.K_LSHIFT]:
                    ball1.speed_x = random.randint(5, 8) + ball1.speed_x
                    ball1.speed_y = random.randint(5, 8) + ball1.speed_y
            if pressed_keys[pygame.K_LEFT]:
                list.append(Ball(screen,random.randint(10, 580), random.randint(10, 580)))
        screen.fill(pygame.Color('gray'))
        for ball in list:
            ball.move()
        for ball in list:
            ball.draw()


        clock.tick(60)


    # DONE: Move the ball
    # DONE: Draw the ball
        ball1.draw()
        ball1.move()




        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
