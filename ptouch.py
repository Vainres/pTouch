from cProfile import run
from doctest import FAIL_FAST
from enum import Flag
from pickle import GLOBAL
from turtle import up, update
from cv2 import line
import pygame, sys

from pygame.locals import *
import random, time

from pyparsing import White
from GraphHandler import generator,imagePredict
import numpy as np
import matplotlib.pyplot as plt
import cv2

from button import Button


# from main import RANK

#option

#Initializing 
pygame.init()
 
# FPS 
FPS = 144
fpsclock = pygame.time.Clock()
 
# colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
 
#
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_W=600
SCREEN_H=800
SPEED=3
LIFE = 0

playerCoin=0

line=[]

objheight=100
objwidth=100
 
nv_height=50
nv_width=50

nv_w=100
nv_h=100

#Setting up Fonts
font = pygame.font.Font('8-BIT WONDER.TTF', 20)
font_small = pygame.font.SysFont("Verdana", 20)
# game_over = font.render("GAME OVER", True, BLACK)
# main_font = pygame.font.SysFont("comicsans", 50)
# lost_font = pygame.font.SysFont("comicsans", 60)
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H))
# DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("ptouch")

# obj=pygame.image.load('gach.webp').convert_alpha()
# obj=pygame.transform.scale(obj,(objwidth ,objheight))

RANK=1
W,yDraw=generator.CreateGraph(RANK,'dothi.png')
dothi=pygame.image.load('dothi.png').convert_alpha()
hinhdothi=pygame.transform.scale(dothi,(100 ,100)).convert_alpha()

obj=pygame.image.load('image/bigdrill_3.png').convert_alpha()
obj=pygame.transform.scale(obj,(objwidth ,objheight)).convert_alpha()

nv = pygame.image.load('hexagont.png').convert_alpha()
nv = pygame.transform.scale(nv,(nv_width,nv_height))
 
BG=pygame.image.load('gray3.png').convert_alpha()
BG=pygame.transform.scale(BG,(SCREEN_WIDTH,1000))

BG1=pygame.image.load('BlacknWhite.webp').convert_alpha()
BG1=pygame.transform.scale(BG1,(SCREEN_WIDTH,1000))

BG2=pygame.image.load('BlacknWhite2.png').convert_alpha()
BG2=pygame.transform.scale(BG2,(SCREEN_WIDTH,1000))

GRASS=pygame.image.load('grass.jpg').convert_alpha()
GRASS=pygame.transform.scale(GRASS,(500,150))

nv1 = pygame.image.load('hexagont.png').convert_alpha()
nv1 = pygame.transform.scale(nv1,(nv_w,nv_h))

nv2 = pygame.image.load('image/cityball.png').convert_alpha()
nv2 = pygame.transform.scale(nv2,(nv_w,nv_h))

nv3 = pygame.image.load('image/metal_ball.png').convert_alpha()
nv3 = pygame.transform.scale(nv3,(nv_w,nv_h))

nv4 = pygame.image.load('image/earthball.png').convert_alpha()
nv4 = pygame.transform.scale(nv4,(nv_w,nv_h))

nv5 = pygame.image.load('image/knifeball.png').convert_alpha()
nv5 = pygame.transform.scale(nv5,(nv_w,nv_h))

nv6 = pygame.image.load('image/ppball.png').convert_alpha()
nv6 = pygame.transform.scale(nv6,(nv_w,nv_h))


pink=pygame.image.load('pink.jpg').convert_alpha()
menuimage=pygame.transform.scale(pink,(200,80))

buybutton=pygame.transform.scale(pink,(200,100))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = obj
        self.surf = pygame.Surface((objwidth ,objheight))
        self.rect = self.surf.get_rect(center = (random.randint(objwidth,SCREEN_WIDTH-objwidth), 0))
        self.alive=True
        

    def move(self,W,yDraw,RANK,line,playerDraw):
            global LIFE
            self.rect.move_ip(0,SPEED)
            if (self.rect.bottom >= (SCREEN_HEIGHT-75)):
                
                self.rect.top = 0
                self.rect.center = (random.randint(objwidth//2,SCREEN_WIDTH-objwidth//2), 0)
                return True
            return False            
                
            
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = nv
        self.surf = pygame.Surface((nv_width,nv_height))
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT-100))
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT] or pressed_keys[K_a]:
                  self.rect.move_ip(-10, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
                  self.rect.move_ip(10, 0)
    
    def draw(self,screen):
        player_idle=pygame.sprite.Group()
        player_idle.add(self)
        player_idle.update(0.5)
        player_idle.draw(screen)
                   
class Background():
      def __init__(self):
            self.bgimage = BG
            self.rectBGimg = self.bgimage.get_rect()
            
 
            self.bgY1 = 0
            self.bgX1 = 0
 
            self.bgY2 = self.rectBGimg.height
            self.bgX2 = 0
 
            self.movingUpSpeed = 5
         
      def update(self):
        self.bgY1 -= self.movingUpSpeed
        self.bgY2 -= self.movingUpSpeed
        if self.bgY1 <= -self.rectBGimg.height:
            self.bgY1 = self.rectBGimg.height
        if self.bgY2 <= -self.rectBGimg.height:
            self.bgY2 = self.rectBGimg.height
             
      def draw(self):
        DISPLAYSURF.blit(self.bgimage, (self.bgX1, self.bgY1))
        DISPLAYSURF.blit(self.bgimage, (self.bgX2, self.bgY2))
        # DISPLAYSURF.blit(GRASS,(0,SCREEN_HEIGHT-150))
        # DISPLAYSURF.blit(GRASS,(0,SCREEN_HEIGHT-(150*2)))
        # DISPLAYSURF.blit(GRASS,(SCREEN_WIDTH-500,SCREEN_HEIGHT-150))
        # DISPLAYSURF.blit(GRASS,(SCREEN_WIDTH-500,SCREEN_HEIGHT-(150*2)))
        
         

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
Player1=Player()
 
bg = Background()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
Char = pygame.sprite.Group()
Char.add(P1)






# obj_group=pygame.sprite.Group()


#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
    
# def gameover():
#     # DISPLAYSURF.fill(WHITE)
#     Game_over_label=font.render("GOODLUCK NEXT TIME",1,BLACK)
#     Restart_label=font.render("PRESS SPACE TO RESTART",1,BLACK)
#     DISPLAYSURF.blit(Game_over_label,(SCREEN_WIDTH/2 - Game_over_label.get_width()/2, 400))
#     DISPLAYSURF.blit(Restart_label,(SCREEN_WIDTH/2 - Restart_label.get_width()/2, 500))
#     pygame.display.update()


def getHighestScore():
    with open("highest score.txt","r") as f:
        return f.read()

def Coin():
    with open("coin.txt","r") as f:
        return f.read()

def get_font(size): 
    return pygame.font.Font("8-BIT WONDER.TTF", size)

playerDraw=False
def play():
    run=True
    global hinhdothi
    global LIFE 
    global line
    global playerDraw
    global SPEED
    global W,yDraw
    global RANK

    try:
        highestScore = int(getHighestScore())
    except:
        highestScore = 0

    

    while run:
            # entity.move()
        #Cycles through all occurring events   
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                SPEED += 0.1     
            if event.type == QUIT:
                run=False
            # elif event.type == pygame.KEYUP:
            #     if event.key == pygame.K_SPACE:
            #             GameStage()
            if pygame.mouse.get_pressed()[0]:
                    positionX,positionY=pygame.mouse.get_pos()
                    line.append((pygame.mouse.get_pos()))
                    playerDraw=True
            else:
                    if playerDraw==True:
                        playerDraw=False
                        # pxarray = imagePredict.get_pixel_data(screen,[701,401],[1000,700])
                        # print(pxarray.shape)
                        # plt.imsave('image.png',pxarray)
                        # pygame.image.save(pxarray,'input.png')
                        PredictResult=imagePredict.Proccess(W,yDraw,RANK,line)
                        
                        line=[]
                        if PredictResult:
                            LIFE+=1
                            RANK=(LIFE+4)//4
                            W,yDraw=generator.CreateGraph(RANK,'dothi.png')
                            dothi=pygame.image.load('dothi.png').convert_alpha()
                            # obj=pygame.transform.scale(dothi,(objwidth ,objheight)).convert_alpha()
                            hinhdothi=pygame.transform.scale(dothi,(100 ,100)).convert_alpha()               
            if event.type ==pygame.KEYDOWN:
                    if event.key==pygame.K_p:
                        line=[]
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_SPACE and gameover:
            #         for entity in all_sprites:
            #             DISPLAYSURF.blit(entity.image, entity.rect)
            #             entity.move()
        bg.update()
        bg.draw()
        DISPLAYSURF.blit(hinhdothi,(SCREEN_WIDTH/3,0)) 
        #DISPLAYSURF.blit(background, (0,0))

        if(highestScore < LIFE):
            highestScore = LIFE
        with open("highest score.txt","w") as f:
            f.write(str(highestScore))

        LIFES = font_small.render(f"SCORE: {LIFE}", True, BLACK)
        DISPLAYSURF.blit(LIFES, (10,10))

        HIGHSCORE = font_small.render(f"HIGHEST SCORE: {highestScore}", True, BLACK)
        DISPLAYSURF.blit(HIGHSCORE, (10,30))
    
        #Moves and Re-draws all Sprites
        Player1.move()
        # for entity in Char:
        #     DISPLAYSURF.blit(entity.image, entity.rect)
        #     entity.move()
        # conclide=False
        for entity in enemies:
            DISPLAYSURF.blit(entity.image, entity.rect)
            echk=entity.move(W,yDraw,RANK,line,playerDraw)
            # if echk:
            #     conclide=True
        # if conclide:
        #     LIFE -= 2
        if len(line)>1:
            for i in range(1,len(line)):
                pygame.draw.line(DISPLAYSURF,GREEN,(line[i-1][0],line[i-1][1]),(line[i][0],line[i][1]),7)
                pygame.draw.line(DISPLAYSURF,BLACK,(line[i-1][0],line[i-1][1]),(line[i][0],line[i][1]),5)
                # pygame.draw.line(DISPLAYSURF,WHITE,(line[i-1][0],line[i-1][1]),(line[i][0],line[i][1]),3)
        #To be run if collision occurs between Player and Enemy
        # print(Player1.rect,'',E1.rect)
        if pygame.sprite.collide_rect(Player1,E1):
        #     #   pygame.mixer.Sound('crash.wav').play()
        #     #   time.sleep(0.8)
            
            print('collide')
            run=False
            E1.rect.top = 0
            Player1.rect.center=(300, 700)
            line=[]
            GameOver(LIFE)
        #     # DISPLAYSURF.fill(RED)
        #     # DISPLAYSURF.blit(game_over, (30,250))
            
            
        #     # for entity in enemies:
        #     #         # entity.kill()
        #     #         LIFE=LIFE - 1 
        # if LIFE<=0:
        #         # GameOver()
        #         # time.sleep(1.5)
        #         # pygame.quit()
        #         # sys.exit()  
        #     GameOver()
        # if run==False:
        #     LIFE=11
        #     gameover()
        #     time.sleep(2)
        #     GameStage()
            
        # for event in pygame.event.get():
            
            # pygame.display.update()
            # time.sleep(1.5)
            # pygame.quit()
            # sys.exit()
        Player1.draw(DISPLAYSURF)
        pygame.display.update()
        fpsclock.tick(FPS)
    pygame.quit()
    




# GameStage()
def items(screen,nv,ImgPosition,textPosition,text,bColor="Black",hColor="Green"):
    SCREEN.blit(nv,ImgPosition)
    STORE_BUY= Button(image=None, pos=textPosition, text_input= text, font=get_font(30), base_color=bColor, hovering_color=hColor)
    return STORE_BUY

def Buyitems(screen,textPosition,text,bColor="Gray",hColor="Green"):
    STORE_BUY= Button(image=None, pos=textPosition, text_input= text, font=get_font(30), base_color=bColor, hovering_color=hColor)
    return STORE_BUY

def Delete_Buyitems(screen,textPosition,text,bColor="Gray",hColor="Green"):
    STORE_BUY= Button(image=None, pos=None, text_input= None, font=get_font(30), base_color=bColor, hovering_color=hColor)
    return STORE_BUY

def store_1():
    playerCoi=addCoin()
    while True:
           
        STORE_MOUSE_POS = pygame.mouse.get_pos()
     
        SCREEN.fill(WHITE)

        OPTIONS_TEXT = get_font(20).render("STORE 1", True, BLACK)
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(SCREEN_W/2,100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(menuimage, pos=(100, SCREEN_H-100), 
                            text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Green")

        OPTIONS_MENU = Button(menuimage, pos=(300, SCREEN_H-100), 
                            text_input="MENU", font=get_font(30), base_color="Black", hovering_color="Green")

        OPTIONS_NEXT = Button(menuimage, pos=(500, SCREEN_H-100), 
                            text_input="NEXT", font=get_font(30), base_color="Black", hovering_color="Green")

        
        #make character store                    
        STORE_BUY_nv1=items(SCREEN,nv1,(50,200),(300,250),'HEXAGON')
        STORE_BUY_BUTTON_nv1=Buyitems(SCREEN,(520,250),'100')
        
        STORE_BUY_nv2= items(SCREEN,nv2,(50,350),(300,400),'CITY BALL')
        STORE_BUY_BUTTON_nv2=Buyitems(SCREEN,(520,400),'100')
        
        STORE_BUY_nv3= items(SCREEN,nv3,(50,500),(300,550),'METAL BALL')
        STORE_BUY_BUTTON_nv3=Buyitems(SCREEN,(520,550),'100')

        for button in [OPTIONS_BACK,STORE_BUY_nv1,STORE_BUY_nv2,STORE_BUY_nv3,OPTIONS_MENU,OPTIONS_NEXT, STORE_BUY_BUTTON_nv1,
        STORE_BUY_BUTTON_nv2,STORE_BUY_BUTTON_nv3]:
            button.changeColor(STORE_MOUSE_POS)
            button.update(SCREEN)

        COINS = font.render(f"COIN {playerCoi}", True, BLACK)
        DISPLAYSURF.blit(COINS, (10,92))

        with open("coin.txt","w") as f:
            f.write(str(playerCoi))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if OPTIONS_BACK.checkForInput(STORE_MOUSE_POS):
                    main_menu()
                if OPTIONS_MENU.checkForInput(STORE_MOUSE_POS):
                    main_menu()
                if OPTIONS_NEXT.checkForInput(STORE_MOUSE_POS):
                    store_2()
                if playerCoi>=100 and STORE_BUY_BUTTON_nv2.checkForInput(STORE_MOUSE_POS):
                    playerCoi=playerCoi-100

       

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if STORE_BUY_nv2.checkForInput(STORE_MOUSE_POS):
                    Player1.image= pygame.transform.scale(pygame.image.load('image/cityball.png'),(nv_width,nv_height)).convert_alpha()
                elif STORE_BUY_nv1.checkForInput(STORE_MOUSE_POS):
                    Player1.image= pygame.transform.scale(pygame.image.load('hexagont.png'),(nv_width,nv_height)).convert_alpha()
                elif STORE_BUY_nv3.checkForInput(STORE_MOUSE_POS):
                    Player1.image= pygame.transform.scale(pygame.image.load('image/metal_ball.png'),(nv_width,nv_height)).convert_alpha()
        

        pygame.display.update()

def store_2():
    playerCoi=addCoin()
    while True:
           
        STORE_MOUSE_POS = pygame.mouse.get_pos()
     
        SCREEN.fill(WHITE)

        OPTIONS_TEXT = get_font(20).render("STORE 2", True, BLACK)
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(SCREEN_W/2,100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(menuimage, pos=(100, SCREEN_H-100), 
                            text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Green")

        OPTIONS_MENU = Button(menuimage, pos=(300, SCREEN_H-100), 
                            text_input="MENU", font=get_font(30), base_color="Black", hovering_color="Green")

        OPTIONS_NEXT = Button(menuimage, pos=(500, SCREEN_H-100), 
                            text_input="NEXT", font=get_font(30), base_color="Black", hovering_color="Green")
        #make character store                    
    
        STORE_BUY_nv4= items(SCREEN,nv4,(50,200),(300,250),'EARTH BALL')
        STORE_BUY_BUTTON_nv4=Buyitems(SCREEN,(520,250),'BUY')

        STORE_BUY_nv5= items(SCREEN,nv5,(50,350),(300,400),'KNIFE BALL')
        STORE_BUY_BUTTON_nv5=Buyitems(SCREEN,(520,400),'BUY')

        STORE_BUY_nv6= items(SCREEN,nv6,(50,500),(300,550),'PUPLE BALL')
        STORE_BUY_BUTTON_nv6=Buyitems(SCREEN,(520,550),'BUY')

        for button in [OPTIONS_BACK,STORE_BUY_nv4,STORE_BUY_nv5,STORE_BUY_nv6,OPTIONS_MENU,OPTIONS_NEXT, 
        STORE_BUY_BUTTON_nv4, STORE_BUY_BUTTON_nv5, STORE_BUY_BUTTON_nv6]:
            button.changeColor(STORE_MOUSE_POS)
            button.update(SCREEN)

        COINS = font.render(f"COIN {playerCoi}", True, BLACK)
        DISPLAYSURF.blit(COINS, (10,92))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(STORE_MOUSE_POS):
                    store_1()
                if OPTIONS_MENU.checkForInput(STORE_MOUSE_POS):
                    main_menu()

                elif STORE_BUY_nv4.checkForInput(STORE_MOUSE_POS):
                    Player1.image= pygame.transform.scale(pygame.image.load('image/earthball.png'),(nv_width,nv_height)).convert_alpha()
                elif STORE_BUY_nv5.checkForInput(STORE_MOUSE_POS):
                    Player1.image= pygame.transform.scale(pygame.image.load('image/knifeball.png'),(nv_width,nv_height)).convert_alpha()
                elif STORE_BUY_nv6.checkForInput(STORE_MOUSE_POS):
                    Player1.image= pygame.transform.scale(pygame.image.load('image/ppball.png'),(nv_width,nv_height)).convert_alpha()


        pygame.display.update()


def credit():
    while True:
           
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()
     
        SCREEN.fill(WHITE)

        OPTIONS_TEXT = get_font(20).render("Credits", True, BLACK)
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(SCREEN_W/2, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(menuimage, pos=(SCREEN_W/2, SCREEN_H-100), 
                            text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Green")

        CREATER_NHAN = Button(image=None, pos=(SCREEN_W/2, 250), 
                            text_input="MAKE BY NHAN", font=get_font(40), base_color="Black", hovering_color="Green")
        CREATER_MINH = Button(image=None, pos=(SCREEN_W/2, 350), 
                            text_input="MAKE BY MINH", font=get_font(40), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(CREDITS_MOUSE_POS)


        OPTIONS_BACK.update(SCREEN)
        for button in [OPTIONS_BACK,CREATER_NHAN,CREATER_MINH]:
            button.changeColor(CREDITS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(CREDITS_MOUSE_POS):
                    main_menu()

        pygame.display.update()
def addCoin(point=0):
    try:
        playerCoin = int(Coin())
    except:
        playerCoin = 0
    playerCoin+=point
    with open("coin.txt","w") as f:
            f.write(str(playerCoin))
    return playerCoin
def GameOver(point):
    addCoin(point)
    
    while True:
        GAME_OVER_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill(WHITE)
        GAME_OVER_TEXT = get_font(20).render("GAME OVER", True, BLACK)
        GAME_OVER_RECT = GAME_OVER_TEXT.get_rect(center=(SCREEN_W/2, 100))
        SCREEN.blit(GAME_OVER_TEXT, GAME_OVER_RECT)

        GAME_OVER_BACK = Button(image=None, pos=(150, SCREEN_H-100), 
                            text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Green")

        GAME_OVER_AGAIN = Button(image=None, pos=(450, SCREEN_H-100), 
                            text_input="PLAY AGAIN", font=get_font(30), base_color="Black", hovering_color="Green")

        GAME_OVER_BACK.update(SCREEN)

        for button in [GAME_OVER_BACK,GAME_OVER_AGAIN]:
            button.changeColor(GAME_OVER_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GAME_OVER_BACK.checkForInput(GAME_OVER_MOUSE_POS):
                    global LIFE
                    LIFE=0
                    global SPEED
                    SPEED=3
                    global RANK
                    RANK=1
                    line=[]
                    
                    global playerDraw
                    playerDraw=False
                    global W,yDraw
                    W,yDraw=generator.CreateGraph(RANK,'dothi.png')
                    global hinhdothi
                    dothi=pygame.image.load('dothi.png').convert_alpha()
                    hinhdothi=pygame.transform.scale(dothi,(100 ,100)).convert_alpha()
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GAME_OVER_AGAIN.checkForInput(GAME_OVER_MOUSE_POS):
                    # global LIFE
                    LIFE=0
                    # global SPEED
                    SPEED=3
                    # global RANK
                    RANK=1
                    # global line
                    
                    # global playerDraw
                    playerDraw=False
                    # global W,yDraw
                    W,yDraw=generator.CreateGraph(RANK,'dothi.png')
                    # global hinhdothi
                    dothi=pygame.image.load('dothi.png').convert_alpha()
                    hinhdothi=pygame.transform.scale(dothi,(100 ,100)).convert_alpha()

                    play()

        pygame.display.update()




def main_menu():
    
    while True:
        SCREEN.fill(WHITE)
        # SCREEN.blit(the, (40, -140))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(70).render("PTOUCH", True,BLACK)
        MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN_W/2, 100))

        PLAY_BUTTON = Button(menuimage, pos=(SCREEN_W/2, 250), 
                            text_input="PLAY", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        STORE_BUTTON = Button(menuimage, pos=(SCREEN_W/2, 370), 
                            text_input="STORE", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        CREDITS_BUTTON = Button(menuimage, pos=(SCREEN_W/2, 490), 
                            text_input="CREDITS", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        QUIT_BUTTON = Button(menuimage, pos=(SCREEN_W/2, 610), 
                            text_input="QUIT", font=get_font(30), base_color="#CCFFFF", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [CREDITS_BUTTON,PLAY_BUTTON, STORE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if CREDIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                #    lan()
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if STORE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    store_1()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credit()   
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()


