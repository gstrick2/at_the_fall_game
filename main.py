#at_the_fall - based on short story, "At the Fall," by Alec Nevala-Lee
#by Georgia Stricklen

import pygame
import math
import time
import random
import sys
import os

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
darkblue = (0, 0, 88)
 
dis_width = 800
dis_height = 600

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#Create screen
screen = pygame.display.set_mode((dis_width, dis_height))

#Winning screen
asset_url = resource_path('final_whale_fall.jpg')
win_background = pygame.image.load(asset_url)
win_background = pygame.transform.smoothscale(win_background, (800,600))

#low battery screen
asset_url = resource_path('low_battery.jpg')
bat_background = pygame.image.load(asset_url)
bat_background = pygame.transform.smoothscale(bat_background, (800,600))

#Beginning background
asset_url = resource_path('beginning.jpg')
begin_background = pygame.image.load(asset_url)
begin_background = pygame.transform.smoothscale(begin_background, (800,600))
#background = pygame.transform.scale(background, (800, 600))

sharkSpeed = 2
clock = pygame.time.Clock()
pygame.display.set_caption("At the Fall")

font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 40)



def message(msg, color, adjX, adjY):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [(dis_width / 6) + adjX, (dis_height / 3) + adjY])

def Your_energy(energy):
    value = score_font.render("Eunice's Power: " + str(energy) + "%", True, red)
    screen.blit(value, [20, 10])

def intro():
    began = True
    while began:
        screen.fill(white)
        screen.blit(begin_background, (0, 0))
        message("It appears James, Eunice's creator, has abandoned her.", white, 0, -100)
        message("You must help her cross the ocean with her limited power supply.", white, -100, -70)
        message("She'll start with 10% power and lose 2% power every five seconds.", white, -100, -40)
        message("To refule, make it to each whale fall you find.", white, 0, -10)
        message("She will get a 10% boost for each whale fall you reach.", white, 0, 20)
        message("Beware of the shark. It drains Eunice 30% every time it catches her.", white, -100, 50)
        message("Ready? Press y-Play and n-Leave game.", white, 0, 140)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    game_loop()
                if event.key == pygame.K_n:
                    began = False
                



def game_loop():
    running = True
    game_close = False
    asset_url = resource_path('robotWhale.png')
    eunice = pygame.image.load(asset_url)
    eunice = pygame.transform.scale(eunice, (130, 100))
    euniceX = 400
    euniceY = 300
    euniceX_change = 0
    euniceY_change = 0

    asset_url = resource_path('shark.png')
    shark = pygame.image.load(asset_url)
    shark = pygame.transform.scale(shark, (120, 90))
    sharkX = 400
    sharkY = 150
    
    asset_url = resource_path('whale_fall.png')
    whale_fall = pygame.image.load(asset_url)
    whale_fall = pygame.transform.scale(whale_fall, (100, 70))
    whale_fallX = round(random.randrange(0, dis_width - 50) / 10.0) * 10.0
    whale_fallY = round(random.randrange(0, dis_height - 50) / 10.0) * 10.0

    energy = 10
    time = 0
    defend = False


    while running:
        # RGB = Red, Green, Blue
        screen.fill(darkblue)
        # Background Image
        #screen.blit(background, (0, 0))

        while game_close == True:
            screen.fill(white)

            if energy >= 100:
                screen.blit(win_background, (0, 0))
                message("Eunice made it, but James is not comming back.", white, 0, -50)
                message("Welcome to the final whale fall.", white, 0, -20)
                message("Eunice will soon reunite with her sisters.", white, 0, 10)
                message("Thank you for playing.", white, 0, 40)
                message("Press c-Play Again or q-Quit", white, 0, 70)
            elif energy <= 0:
                screen.blit(bat_background, (0, 0))
                message("Eunice ran out of power!", red, 0, -60)
                message("Press c-Play Again or q-Quit", red, 0, -30)
 
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        game_close = False
                    if event.key == pygame.K_c:
                        running = True
                        game_close = False
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    euniceX_change = -4
                    euniceY_change = 0
                elif event.key == pygame.K_RIGHT:
                    euniceX_change = 4
                    euniceY_change = 0
                elif event.key == pygame.K_UP:
                    euniceY_change = -4
                    euniceX_change = 0
                elif event.key == pygame.K_DOWN:
                    euniceY_change = 4
                    euniceX_change = 0

        euniceX += euniceX_change
        euniceY += euniceY_change
        if euniceX <= 0:
            euniceX = 0
        elif euniceX >= 710:
            euniceX = 710

        if euniceY <= 0:
            euniceY = 0
        elif euniceY >= 550:
            euniceY = 550
        
        
        screen.blit(eunice, (euniceX, euniceY))
        screen.blit(shark, (sharkX, sharkY))
        screen.blit(whale_fall, (whale_fallX, whale_fallY))

        #Distance from shark
        dx = euniceX - sharkX
        dy = euniceY - sharkY
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist 
        
        
        sharkX += dx * sharkSpeed
        sharkY += dy * sharkSpeed

        #Distance from whale fall
        dxW = euniceX - whale_fallX
        dyW = euniceY - whale_fallY
        distW = math.hypot(dxW, dyW)

        #Player got to whale fall, increase energy stores and move the whale fall
        if distW <= 20:
            energy += 10
            whale_fallX = round(random.randrange(0, dis_width - 100) / 10.0) * 10.0
            whale_fallY = round(random.randrange(0, dis_height - 100) / 10.0) * 10.0

        #Shark has caught eunice, player loses 30% power
        if dist <= 30:
            energy -= 30
            sharkX = round(random.randrange(0, dis_width - 50) / 10.0) * 10.0
            sharkY = round(random.randrange(0, dis_height - 50) / 10.0) * 10.0

        Your_energy(energy)

        #If energy reaches 100%, player wins, if it reaches 0, player loses
        if energy >= 100:
            game_close = True

        #If energy is less than or equal to zero, then player has ran out of power and they lose
        if energy <= 0:
            game_close = True

        
        #Take away energy every 5 seconds
        if time != round(pygame.time.get_ticks() / 1000):
            #update time
            time = round(pygame.time.get_ticks() / 1000)
            if time % 5 == 0:
                energy -= 2

        
        pygame.display.update()
        clock.tick(35)

    pygame.quit()
    sys.exit()


intro()
