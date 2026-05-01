#Nasa IOTD Display
#Version 0.1
#Change log:
#-created window with pygame


#Import dependencies
import os
import pygame

#Initialize stuff
pygame.init()

#Initialize the screen, 
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('NASA Image Of The Day V0.1')

#Main loop
running = True
while running:
    #check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #fill background with a color
    screen.fill((155, 200, 10))

    #update the display
    pygame.display.flip()

#cleanly exit pygame
pygame.quit()

