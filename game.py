import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Welcome to ShefPuff')

black = (0,0,0)
white = (255,255,255)
background = (153, 217, 234)
grass = (0, 128, 0)
pink = (255, 94, 154)
red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

clock = pygame.time.Clock()
crashed = False

flowerImg = pygame.image.load('flower.png')
flowerImg = pygame.transform.scale(flowerImg, (90, 80))

bugImg = pygame.image.load('bug.png')
bugImg = pygame.transform.scale(bugImg, (100, 100))

sunImg = pygame.image.load('sun.png')
sunImg = pygame.transform.scale(sunImg, (100, 100))

cloudImg = pygame.image.load('cloud.png')
cloudImg = pygame.transform.scale(cloudImg, (80, 100))

def score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def flower(x,y):
    gameDisplay.blit(flowerImg, (x,y))

def bug(x,y):
    gameDisplay.blit(bugImg, (x,y))

def sun():
    gameDisplay.blit(sunImg,(20,20))
            
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    gameLoop()
    
    

def crash():
    message_display('You Crashed!')

def quitgame():
    pygame.quit()
    quit()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("freesansbold.ttf",25)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def game_intro():

    intro = True
    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 
        gameDisplay.fill(background)
        for i in range(0, display_width , 80):
            for j in range(0, display_height , 90):
                flower(i,j)

        pygame.draw.rect(gameDisplay, background,(160,220,490,150))

        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("PowPuff", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("START!",150,450,100,50,green,bright_green,gameLoop)
        button("QUIT!",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def gameLoop():
    # print(2)
    x =  (display_width * 0.45)
    y = (display_height * 0.85)

    x_change = 0
    
    bug_startx = random.randrange(0, display_width)
    bug_starty = -600
    bug_speed = 8

    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # print(1)
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
            
        gameDisplay.fill(background)

        bug(bug_startx, bug_starty)
        bug_starty += bug_speed

        pygame.draw.rect(gameDisplay, grass, [0, display_height - 10, display_width, 10])

        flower(x,y)

        sun()

        score(dodged)

        if x > display_width - 90 or x < 0:
            crash()

        if bug_starty > display_height:
            bug_starty = 0 - 80
            bug_startx = random.randrange(0,display_width)
            dodged += 1
            bug_speed += 1

        if y < bug_starty+50:
            if x > bug_startx and x < bug_startx + 90 or x+90 > bug_startx and x + 80 < bug_startx+90:
                crash()

        pygame.display.update()
        clock.tick(60)

game_intro()
gameLoop()
pygame.quit()
quit()