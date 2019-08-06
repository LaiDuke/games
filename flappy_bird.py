import time
import random
import pygame

pygame.init()
pygame.font.get_fonts()

display_width = 650
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

background = pygame.image.load("img/background.png")
BirdImg = pygame.image.load("img/Flappy_Bird_Icon.png")
block1 =  pygame.image.load("img/block.png")
block2 =  pygame.image.load("img/block1.png")


def blocked(tx, th):
    gameDisplay.blit(block1, (tx, th-325))
    gameDisplay.blit(block2, (tx, th+180))



def bird(x, y, angle):
    gameDisplay.blit(pygame.transform.rotate(BirdImg, angle), (x, y))


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(text, x , y, color, size):
    largeText = pygame.font.Font('8-Bit.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()


def crash(count):
    message_display('GAME OVER', (display_width/2), display_height/3, red, 120)
    message_display('%d SCORE' %count, (display_width/2), display_height/3+100, black, 100)
    time.sleep(2)
    game_loop()


def game_loop():
    game_Exit = False
    speed = 5
    count = 0

    #bird
    x = 100
    y = 200
    t = 0
    g = 0.1
    angle = 0


    #blocks
    block_x1 = display_width
    block_x2 = display_width+280
    block_x3 = display_width+560
    height1 = random.randrange(145,325)
    height2 = random.randrange(145, 325)
    height3 = random.randrange(145, 325)

    while not game_Exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_Exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.type== pygame.K_SPACE:
                    t = -10
                    angle = 60
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    t += 4
                    angle -= 15

        if (block_x1>120 and block_x1<=125) or (block_x2>120 and block_x2<=125) or (block_x3>120 and block_x3<=125):
            count+=1
        v = g*t
        y = y + abs(v)*t
        t += 0.32
        block_x1 -= speed
        block_x2 -= speed
        block_x3 -= speed
        if angle > -45:
            angle -= 2

        if block_x1 < -190:
            block_x1 = display_width
            height1 = random.randrange(145,325)
        if block_x2 < -190:
            block_x2 = display_width
            height2 = random.randrange(145,325)
        if block_x3 < -190:
            block_x3 = display_width
            height3 = random.randrange(145,325)


        gameDisplay.blit(background,(0,0))
        blocked(block_x1, height1)
        blocked(block_x2, height2)
        blocked(block_x3, height3)
        font = pygame.font.Font("bitout.fon", 10)
        bit = font.render("%d" % count, True, black)
        alert = pygame.transform.scale(bit,(50,100))
        gameDisplay.blit(alert, (display_width/2,50))


        bird(x, y, angle)
        if x+74 > block_x1 and x < block_x1+90:
            if y+10 < height1 or y> height1+180:
                game_Exit = True
        if x+74 > block_x2 and x < block_x2+90:
            if y+10 < height2 or y> height2+180:
                game_Exit = True
        if x+74 > block_x3 and x < block_x3+90:
            if y+10 < height3 or y> height3+180:
                game_Exit = True

        if y < 0 or (y + 60) > display_height:
            crash(count)
            game_Exit = True




        pygame.display.update()
        if game_Exit == True:
            crash(count)
        clock.tick(60)




game_loop()
pygame.quit()
quit()
