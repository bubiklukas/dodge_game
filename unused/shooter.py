import pygame
from random import *
from players_class import *
from enemy_class import *
import time

pygame.init()
pygame.font.init()
WIDTH = 1024
HEIGHT = 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))

player1_image = pygame.image.load('player1.png')



color_red = 255, 0, 0
color_green = 0, 255, 0
color_blue = 0, 0, 255
color_aqua = 0, 200, 255
color_white = 255, 255, 255
color_yellow = 255, 255, 0
color_background = 0, 0, 0
end_text = False

class score(object):
    def __init__(self):
        self.count = 1
        self.multiplier = 0.25
    def add(self, num):
        self.count += num

    def setMultiplier(self, num):
        self.multiplier = num


def isOut(obj):
    if (obj.x > WIDTH and obj.direction == 'Right') or (obj.x < 0 and obj.direction == 'Left'):
        #print('function done')
        return True
    if (obj.y > HEIGHT and obj.direction == 'Down') or (obj.y < 0 and obj.direction == 'Up'):
        #print('function done')
        return True

def isCollision(objA, objB):
    return objA.getRect().colliderect(objB.getRect())

def text(text, x, y, color, size):
    myfont = pygame.font.SysFont('Arial', size)
    textsurface = myfont.render(str(text), False, color)
    screen.blit(textsurface, (x, y))

def resetDraw(num):
    if num == 1:
        player1.x = WIDTH * 2/3
        player1.y = HEIGHT / 2
        player1.draw(screen)
    if num == 2:
        player1.x = WIDTH * 2/3
        player1.y = HEIGHT / 2
        player2.x = WIDTH * 1/3
        player2.y = HEIGHT / 2
        player1.draw(screen)
        player2.draw(screen)

player1 = player1(WIDTH * 2/3, HEIGHT / 2)
player2 = player2(WIDTH * 1/3, HEIGHT / 2)



enemX = enemyX(WIDTH, HEIGHT)
enemY = enemyY(WIDTH, HEIGHT)

score = score()
speed = enemX.velocity


player1.setColor(color_white)
player2.setColor(color_yellow)

enemyY_generation = True
enemyX_generation = True

game_over = False
keys = pygame.key.get_pressed()
menu = True

enemyY_list = []
enemyY_count = 4
y = True

enemyX_list = []
enemyX_count = 4
x = True

menuList = ['1 Player', '2 Players', 'Settings', 'Quit Game']
settingsList = ['Speed', 'Speed limit', 'Player1 Color', 'Player2 Color', 'Back']
item = 0
color = color_aqua
Players2 = False
settings = False
start_time = time.time()
###########################################################################################
#LOOP
while not game_over:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    player1.Movement(WIDTH, HEIGHT)
    player2.Movement(WIDTH, HEIGHT)

#MENU
    while menu:
        pygame.display.update()
        for i, elem in enumerate(menuList):
            if item == i:
                color = color_yellow
            else:
                color = color_aqua
            text(elem, 50, i*150 + 20, color, 100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #game_over = True
                game_over = True
                menu = False
                screen.fill(color_background)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and item > 0:
                    item -= 1
                if event.key == pygame.K_DOWN and item < len(menuList) - 1:
                    item += 1
                if event.key == pygame.K_RETURN:
                    if item == menuList.index('1 Player'):
                        player1.setPos(WIDTH/2, HEIGHT/2)
                        Players2 = False
                        menu = False
                    if item == menuList.index('2 Players'):
                        player1.setPos(WIDTH/2 - 100, HEIGHT/2)
                        player2.setPos(WIDTH/2 + 100, HEIGHT/2)
                        Players2 = True
                        menu = False
                    if item == menuList.index('Settings'):
                        screen.fill(color_background)
                        settings = True
                        menu = False
                        item = 0
                    if item == menuList.index('Quit Game'):
                        print('quit')
                        game_over = True
                        menu = False
#SETTINGS
    while settings:
        pygame.time.delay(10)
        pygame.display.update()
        for i, elem in enumerate(settingsList):
            if item == i:
                color = color_yellow
            else:
                color = color_aqua
            text(elem, 50, i*150 + 20, color, 100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                settings = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and item > 0:
                    item -= 1
                if event.key == pygame.K_DOWN and item < len(settingsList) - 1:
                    item += 1
                if event.key == pygame.K_RETURN:
                    if item == settingsList.index('Speed'):
                        pass
                    if item == settingsList.index('Speed limit'):
                        pass
                    if item == settingsList.index('Player1 Color'):
                        pass
                    if item == settingsList.index('Player2 Color'):
                        pass
                    if item == settingsList.index('Back'):
                        settings = False
                        menu = True
                        item = 0
    
###############################################################################################

    #GENERATION Y
    change = 1
    while len(enemyY_list) < enemyY_count and enemyY_generation == True and game_over == False:
        e = enemyY(WIDTH, HEIGHT)
        collision = False
        for e2 in enemyY_list:
            if isCollision(e , e2):
                collision = True
                break
        if collision:
            continue
        if change == 0:
            e.setDirection('Left')
            change = 1
        else:
            e.setDirection('Right')
            change = 0
        if collision == False:
            e.setColor(color_red)
            enemyY_list.append(e)
            print(enemyY_list)
    
    if y:
        print('Generation  Y done.')
        y = False	
    enemyY_generation = False

    #GENERATION X
    change = 1
    while len(enemyX_list) < enemyX_count and enemyX_generation == True and game_over == False:
        e = enemyX(WIDTH, HEIGHT)
        collision = False
        for e2 in enemyX_list:
            if isCollision(e , e2):
                collision = True
                break
        if collision:
            continue
        if change == 0:
            e.setDirection('Up')	
            change = 1
        else:
            e.setDirection('Down')
            change = 0
        if collision == False:
            e.setColor(color_red)
            enemyX_list.append(e)
            print(enemyX_list)
    if x and game_over == False:
        print('Generation X done.')
        x = False	
    enemyX_generation = False

#####################################
    
    #speed *= score.multiplier

    

    #MOVE, DRAW AND COLLISION ENEMY Y
    if game_over == False:
        for e in enemyY_list:
            e.setVel(speed)
            e.Move()
            e.draw()
            if isCollision(player1, e):
                player2.win = True
                end_text = True
                run_delay = True
                displayUpdate = True
            elif isCollision(player2, e) and Players2:
                player1.win = True
                end_text = True
                run_delay = True
                displayUpdate = True
            if isOut(e):
                score.add(1)
                collision = True			
                while collision: 
                    e.randomize()
                    collision = False
                    for elem in enemyY_list:
                        if elem.y == e.y:
                            continue
                        if isCollision(e, elem):					
                            collision = True
                            break
    #MOVE, DRAW AND COLLISION ENEMY X
    if game_over == False:
        for e in enemyX_list:
            e.setVel(speed)
            e.Move()
            e.draw()
            if isCollision(player1, e):
                player2.win = True
                end_text = True
                run_delay = True
                displayUpdate = True
            elif isCollision(player2, e) and Players2:
                print('coll')
                player1.win = True
                end_text = True
                run_delay = True
                displayUpdate = True
            if isOut(e):
                score.add(1)
                collision = True			
                while collision: 
                    e.randomize()
                    collision = False
                    for elem in enemyX_list:
                        if elem.x == e.x:
                            continue
                        if isCollision(e, elem):					
                            collision = True
                            break
    
###########################################
    #END TEXT

    while end_text:
        pygame.time.delay(50)
        screen.fill(color_background)
        if player1.win:
            text('Player 1 Won.', 400, 300, color_aqua, 50)
        if player2.win and Players2: 
            text('Player 2 Won.', 400, 300, color_aqua, 50)
        if player2.win and not Players2:
            text('You Lost.', 430, 300, color_aqua, 50)

        text(score.count, 640, 500, color_aqua, 50)
        text('Your score is ', 380, 500, color_aqua, 50)
        text('Press R to play again.', 340, 600, color_aqua, 50)
        pygame.display.update()
        keys = pygame.key.get_pressed()
        pygame.event.pump()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('QUIT GAME')
                end_text = False
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    screen.fill(color_background)
                    if Players2:
                        resetDraw(2)
                    else:
                        resetDraw(1)
                    enemyX_list.clear()
                    enemyY_list.clear()
                    enemyX_generation = True
                    enemyY_generation = True
                    pygame.display.update()
                    speed = enemX.velocity
                    score.count = 0
                    player1.win = False
                    player2.win = False
                    print(enemyX_generation)
                    player1.setPos(WIDTH/2, HEIGHT/2)
                    end_text = False
                if event.key == pygame.K_m:
                    menu = True
                    end_text = False

            

##############################################
    if not menu and not game_over:
        player1.draw(screen, player1_image)
        if Players2:
            player2.draw(screen)
    pygame.display.update()
    screen.fill(color_background)

    #ENEMY SPEED
    end_time = time.time()
    time_length = 1
    speed_limit = 9
    score.setMultiplier(0.25)
    if end_time - start_time > time_length and speed < speed_limit:
        speed += score.multiplier
        start_time = time.time()
        print(speed)

pygame.quit()
