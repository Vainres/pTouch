# import pygame
# import button
# from pygame import*

# from ptouch import GameStage

# #create display window
# SCREEN_HEIGHT = 500
# SCREEN_WIDTH = 800

# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption('Button Demo')

# #load button images
# start_img = pygame.image.load('start_btn.png').convert_alpha()
# exit_img = pygame.image.load('exit_btn.png').convert_alpha()

# #create button instances
# start_button = button.Button(100, 200, start_img, 0.8)
# exit_button = button.Button(450, 200, exit_img, 0.8)

# #game loop
# run = True
# while run:

# 	screen.fill((202, 228, 241))

# 	if start_button.draw(screen):
# 		print('START')
# 	if exit_button.draw(screen):
# 		print('EXIT')

# 	#event handler
# 	for event in pygame.event.get():
# 		#quit game
# 		if event.type == pygame.QUIT:
# 			run = False 

# 	pygame.display.update()

# pygame.quit()


from matplotlib import image
import pygame, sys
from button import Button
from pygame import mixer
from ptouch import *
 
# Setup pygame/window ---------------------------------------- #
FPS=60
fpsclock = pygame.time.Clock()
from pygame.locals import *

pygame.init()

pygame.display.set_caption('game menu')

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)

SCREEN_W=600
SCREEN_H=800

nv_w=100
nv_h=100


SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H))

nv1 = pygame.image.load('wizard.png').convert_alpha()
nv1 = pygame.transform.scale(nv1,(nv_w,nv_h))

nv2 = pygame.image.load('lanternguy.png').convert_alpha()
nv2 = pygame.transform.scale(nv2,(nv_w,nv_h))

pink=pygame.image.load('pink.jpg').convert_alpha()
menuimage=pygame.transform.scale(pink,(200,80))

buybutton=pygame.transform.scale(pink,(200,100))


 
font = pygame.font.Font('8-BIT WONDER.TTF', 20)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def get_font(size): 
    return pygame.font.Font("8-BIT WONDER.TTF", size)
 
def play():
    while True:
        GameStage()
 
def store():
    while True:
           
        STORE_MOUSE_POS = pygame.mouse.get_pos()
     
        SCREEN.fill(WHITE)

        OPTIONS_TEXT = get_font(20).render("STORE", True, BLACK)
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(SCREEN_W/2,100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(menuimage, pos=(SCREEN_W/2, SCREEN_H-100), 
                            text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Green")
        #make character store                    
        SCREEN.blit(nv1,(50,200))
        STORE_BUY_nv1= Button(image=None, pos=(300,250), 
                            text_input= "WIZAD", font=get_font(30), base_color="Black", hovering_color="Green")

        SCREEN.blit(nv2,(50,350))
        STORE_BUY_nv2= Button(image=None, pos=(300,400), 
                            text_input="LANTERN GUY", font=get_font(30), base_color="Black", hovering_color="Green")

        # OPTIONS_BACK.changeColor(STORE_MOUSE_POS)
        # OPTIONS_BACK.update(SCREEN)
        
        for button in [OPTIONS_BACK,STORE_BUY_nv1,STORE_BUY_nv2]:
            button.changeColor(STORE_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(STORE_MOUSE_POS):
                    main_menu()
                # elif STORE_BUY_nv2.checkForInput(STORE_MOUSE_POS):
                #     Player.image=pygame.image.load('lanternguy.png')

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
                    store()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credit()   
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()

