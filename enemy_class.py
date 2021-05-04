from random import *
import pygame
pygame.init()
class enemyX(object):
    def __init__(self, screen_WIDTH, screen_HEIGHT, image):
        self.width = 75
        self.height = 75
        self.color = 220, 220, 220
        self.velocity = 1
        self.y = self.height
        self.direction = 'Down'
        self.screen_HEIGHT = screen_HEIGHT
        self.screen_WIDTH = screen_WIDTH
        self.image = image
        self.copy = self.image
        self.randomize()
    def draw(self, surface):
        self.copy = pygame.transform.scale(self.copy, (73, 76))
        surface.blit(self.copy, (self.x, self.y))

    def randomize(self):
        if self.direction == 'Up':
            self.x = randint(2*self.width, self.screen_WIDTH-2*self.width)
            self.y = self.screen_HEIGHT - self.height
            self.copy = pygame.transform.rotate(self.copy, 90)

        elif self.direction == 'Down':
            self.x = randint(2*self.width, self.screen_WIDTH-2*self.width)
            self.y = 0 + self.height
            self.copy = pygame.transform.rotate(self.copy, 90)

    def Move(self):
        if self.direction == 'Up':
            self.y -= self.velocity

        if self.direction == 'Down':
            self.y += self.velocity

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    def setDirection(self, direction):
        self.direction = direction
    def setColor(self, color):
        self.color = color
    def setY(self, y):
        self.y = y
    def setVel(self, velocity):
        self.velocity = velocity

class enemyY(object):
    def __init__(self, screen_WIDTH, screen_HEIGHT, image):
        self.width = 75
        self.height = 75
        self.color = 220, 220, 220
        self.velocity = 1
        self.x = self.width
        self.direction = 'Left'
        self.screen_HEIGHT = screen_HEIGHT
        self.screen_WIDTH = screen_WIDTH
        self.image = image
        self.copy = self.image
        self.randomize()
    def setDirection(self, direction):
        self.direction = direction
    def randomize(self):
        if self.direction == 'Left':
            self.y = randint(2*self.height, self.screen_HEIGHT-2*self.height)
            self.x = self.screen_WIDTH - self.width
            self.copy = pygame.transform.rotate(self.copy, 90)
        elif self.direction == 'Right':
            self.y = randint(2*self.height, self.screen_HEIGHT-2*self.height)
            self.x = 0 + self.width
            self.copy = pygame.transform.rotate(self.copy, 90)
    def Move(self):
        if self.direction == 'Left':
            self.x -= self.velocity
        if self.direction == 'Right':
            self.x += self.velocity
    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    def draw(self, surface):
        self.copy = pygame.transform.scale(self.copy, (73, 76))
        surface.blit(self.copy, (self.x, self.y))

    def setColor(self, color):
        self.color = color
    def setX(self, x):
        self.x = x
    def setVel(self, velocity):
        self.velocity = velocity
print('Enemy class loaded.')