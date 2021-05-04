print('Player class loaded.')
import pygame
pygame.init()



class player1(object):
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.move_length = 10
        self.width = 72
        self.width_copy = self.width
        self.height = 122
        self.height_copy = self.height
        self.color = 255, 255, 255
        self.win = False
        self.image = image
        self.copy = self.image
        self.angle = 4
        self.move_count = 0.5
        self.move_count_multiplier = 0.01

    def draw(self, surface):
        surface.blit(self.copy, (self.x, self.y))

    def draw_somewhere(self, x, y, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(x, y, self.width, self.height))


#MOVEMENT
    def moveLeft(self):
        self.x -= self.move_length
        self.angle = 1
        self.move_count += self.move_count_multiplier
    def moveRight(self):
        self.x += self.move_length
        self.angle = 3
        self.move_count += self.move_count_multiplier
    def moveUp(self):
        self.y -= self.move_length
        self.angle = 4
        self.move_count += self.move_count_multiplier
    def moveDown(self):
        self.y += self.move_length
        self.angle = 2
        self.move_count += self.move_count_multiplier

    def Movement(self, WIDTH, HEIGHT):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > self.width:
            self.moveLeft()
        if keys[pygame.K_RIGHT] and self.x < WIDTH - 2 * self.width:
            self.moveRight()
        if keys[pygame.K_UP] and self.y > self.height:
            self.moveUp()
        if keys[pygame.K_DOWN] and self.y < HEIGHT - 2 * self.height:
            self.moveDown()

    def rotate(self, angle):
        self.copy = pygame.transform.rotate(self.image, angle)
        if self.angle == 1 or self.angle == 3:
            self.width = self.height_copy
            self.height = self.width_copy
        else:
            self.height = self.height_copy
            self.width = self.width_copy

    def setMoveLength(self, length):
        self.move_length = length
    def setColor(self, color):
        self.color = color
    def setPos(self, x, y):
        self.x = x
        self.y = y
    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class player2(object):
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.move_length = 10
        self.image = image
        self.copy = self.image
        self.width = 72
        self.width_copy = self.width
        self.height = 122
        self.height_copy = self.height
        self.angle = 4
        self.color = 255, 255, 255
        self.win = False

    def draw(self, surface):
        surface.blit(self.copy, (self.x, self.y))

    def draw_somewhere(self, x, y, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(x, y, self.width, self.height))

    def moveLeft(self):
        self.x -= self.move_length
        self.angle = 1
    def moveRight(self):
        self.x += self.move_length
        self.angle = 3
    def moveUp(self):
        self.y -= self.move_length
        self.angle = 4
    def moveDown(self):
        self.y += self.move_length
        self.angle = 2

    def Movement(self, WIDTH, HEIGHT):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x > self.width:
            self.moveLeft()
        if keys[pygame.K_d] and self.x < WIDTH - 2 * self.width:
            self.moveRight()
        if keys[pygame.K_w] and self.y > self.height:
            self.moveUp()
        if keys[pygame.K_s] and self.y < HEIGHT - 2 * self.height:
            self.moveDown()

    def rotate(self, angle):
        self.copy = pygame.transform.rotate(self.image, angle)
        if self.angle == 1 or self.angle == 3:
            self.width = self.height_copy
            self.height = self.width_copy
        else:
            self.height = self.height_copy
            self.width = self.width_copy


    def setMoveLength(self, length):
        self.move_length = length
    def setColor(self, color):
        self.color = color
    def setPos(self, x, y):
        self.x = x
        self.y = y

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)