import sys
import pygame
import random

############
#INITIALIZE
############
#equivalent to load in Love
pygame.init() #starts off pygame

#scene setup
# 0 = title
# 1 = game
# 2 = game over/replay prompt

scene = 1


#enemy image load
enemy = pygame.image.load("barnacle.png")
enemy2 = pygame.image.load("block.png")
enemy3 = pygame.image.load("slime.png")

enemies = [enemy, enemy2, enemy3]

#setup screen
width = 600
height = 400
size = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dungeon Splat")
pygame.display.set_icon(enemy3)

#define colors
green = (74, 99, 35)
orange = (243, 121, 78)
black = (0, 0, 0)

#-------TITLE STUFF--------
titleY = 100
playY = 300
btnMargin = 10

titleFont = pygame.font.SysFont("Arial", 65)
enemyTitle = titleFont.render("Dungeon Splat!", False, green)
gameOverTitle = titleFont.render("GAME OVER", False, orange)

buttonFont = pygame.font.SysFont("Arial", 30)
playWord = buttonFont.render("PLAY", False, green)
quitWord = buttonFont.render("QUIT", False, green)
restartWord = buttonFont.render("RESTART", False, orange)

playBtn = pygame.draw.rect(screen, black, ((width/2)-(playWord.get_width()/2) - btnMargin, playY - btnMargin, playWord.get_width() + (btnMargin*2), playWord.get_height()+(btnMargin*2)),0)

quitBtn = pygame.draw.rect(screen, black, ((width/4)-quitWord.get_width()/2 - btnMargin, playY - btnMargin, quitWord.get_width() + (btnMargin * 2), quitWord.get_height() +(btnMargin *2)), 0)

restartBtn = pygame.draw.rect(screen, green, ((width * .75)-(restartWord.get_width()/2) - btnMargin, playY - btnMargin, restartWord.get_width() + (btnMargin * 2), restartWord.get_height() +(btnMargin *2)), 0)






#--------------------------

#--------GAMEPLAY MODE LOAD
#enemy definitions
counter = 0
numOfThings = 7
enemyImage = []
enemyX = []
enemyY = []
enemySpeed = []
baseSpeed = .05
speedMulti = 1.2

#release the enemies
while counter < numOfThings:
    enemyImage.append(random.choice(enemies)) #assign random image
    enemyX.append(random.randint(0, width - enemyImage[counter].get_width()))
    enemyY.append(0 - random.randint(enemyImage[counter].get_height(), enemyImage[counter].get_height() * 2))
    enemySpeed.append(baseSpeed * random.random())

    counter += 1

##########
#GAME LOOP
##########
gameOver = False
while not gameOver:
    #quit event (pygame quirk)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    
    ###########
    #CLICKS
    ###########
    if pygame.mouse.get_pressed()[0]: #left click
        coords = pygame.mouse.get_pos() #get position at click
        if scene == 0: #if title screen
            #button to play
            print("title screen")
        elif scene == 1: #play area
            #we can't use collidepoint() because don't have
            #individual rects on each enemy image. So old school.
            counter = 0
            while counter < numOfThings:
                #click greater= left side and less= right side and greater than top, less than bottom (within image)
                if coords[0] >= enemyX[counter] and coords[0] <= enemyX[counter] + enemyImage[counter].get_width() and coords[1] >= enemyY[counter] and coords[1] <= enemyY[counter] + enemyImage[counter].get_height():
                    #print("Clicked it")
                    enemyImage[counter] = random.choice(enemies)
                    enemyX[counter] = random.randint(0, width - enemyImage[counter].get_width())
                    enemyY[counter] = 0 - random.randint(enemyImage[counter].get_height(), enemyImage[counter].get_height() * 2)
                    enemySpeed[counter] *= speedMulti
                    
                counter += 1
        else: #gameover screen
            #print("game over screen")
            scene = 2
            if pygame.Rect.collidepoint(quitBtn, coords):
                gameOver = True
            if pygame.Rect.collidepoint(restartBtn, coords):
                #RESET YOUR GAME BEFORE RELOADING OR GOING BACK
                counter = 0
                while counter < numOfThings:
                    enemyImage[counter] = random.choice(enemies)
                    enemyX[counter] = random.randint(0, width - enemyImage[counter].get_width())
                    enemyY[counter] = 0 - random.randint(enemyImage[counter].get_height(), enemyImage[counter].get_height() * 2)
                    enemySpeed.append(baseSpeed * random.random())
                    counter +=1
                scene = 1




    ###########
    # UPDATE
    ###########
    # movement and floor checks
    if scene == 1:
        counter = 0
        while counter < numOfThings:
            #check if hit bottom
            if enemyY[counter] + enemyImage[counter].get_height() > height:
                scene = 2
            else:
                enemyY[counter] += enemySpeed[counter]
            counter += 1


    ############
    # DRAW
    ############
    #title scene
    if scene == 0:
        screen.fill(orange)
    
    #game play
    elif scene == 1:
        screen.fill(green)
        #draw the enemies
        counter = 0
        while counter < numOfThings:
            screen.blit(enemyImage[counter], (enemyX[counter], enemyY[counter]))
            counter += 1

    else:
        screen.fill(black)
        #gameOver text
        screen.blit(gameOverTitle, (width/2 - gameOverTitle.get_width()/2, titleY))
        
        #-------BUTTONS---------
        #QUIT
        coords = pygame.mouse.get_pos()
        if pygame.Rect.collidepoint(quitBtn, coords): #check if mouse is hovering over button and flip colors
            quitBtn = pygame.draw.rect(screen, green, ((width/4)-quitWord.get_width()/2 - btnMargin, playY - btnMargin, quitWord.get_width() + (btnMargin * 2), quitWord.get_height() +(btnMargin *2)), 0)
        else:
            quitBtn = pygame.draw.rect(screen, orange, ((width/4)-quitWord.get_width()/2 - btnMargin, playY - btnMargin, quitWord.get_width() + (btnMargin * 2), quitWord.get_height() +(btnMargin *2)), 0)
            screen.blit(quitWord, ((width/4)-(quitWord.get_width()/2), playY))
        #RESTART
        if pygame.Rect.collidepoint(restartBtn, coords): #if hovered over
            restartBtn = pygame.draw.rect(screen, orange, ((width * .75)-(restartWord.get_width()/2) - btnMargin, playY - btnMargin, restartWord.get_width() + (btnMargin * 2), restartWord.get_height() +(btnMargin *2)), 0)
        else:
            restartBtn = pygame.draw.rect(screen, green, ((width * .75)-(restartWord.get_width()/2) - btnMargin, playY - btnMargin, restartWord.get_width() + (btnMargin * 2), restartWord.get_height() +(btnMargin *2)), 0)
            screen.blit(restartWord, ((width * .75) - (restartWord.get_width()/2), playY))
    #at end of draw, flip display
    pygame.display.flip()

#make sure we have quit
pygame.display.quit()    





