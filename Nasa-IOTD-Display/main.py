#Nasa IOTD Display
#Version 0.1
#Change log:
#-created window with pygame
#-added nasapy pull request for images using demo key
#-displayed an image via pygame
#-used IO to store an image


#Import dependencies
import os
import nasapy
import pygame
import requests
import io
from dotenv import load_dotenv
from datetime import date

#Initialize stuff
pygame.init()
load_dotenv()
apiKey = os.getenv('NASA_KEY')
nasa = nasapy.Nasa(apiKey)
date = date.today()

#Functions
def nasaPicture():
    #Get nasa image of the day
    apod = nasa.picture_of_the_day(date=date)
    imgUrl = apod['url']
    #download the photo into ram
    response = requests.get(imgUrl)
    imageBits = io.BytesIO(response.content)
    imageBits.seek(0)
    return pygame.image.load(imageBits).convert()

def nasaSurface(imageData):
    #get needed image, rects, centers
    nasaAPOD = imageData
    screenRect = screen.get_rect()
    imageRect = nasaAPOD.get_rect()
    imageRect.center = screenRect.center
    #blit the photo of the day to the screen
    print('screen blit')
    screen.blit(nasaAPOD, imageRect)

def menuScreen():
    pass

#Initialize the screen,
screenW, screenH = 600, 800
screen = pygame.display.set_mode((screenH, screenW), pygame.RESIZABLE)
pygame.display.set_caption('NASA Image Of The Day V0.1')

#Fetch the daily image to initialize
imageData = nasaPicture()
#resize the image dynamically
apod = pygame.transform.scale(imageData, (screenH, screenW))
#Main loop
running = True
while running:
    #check for events
    print('check events')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.VIDEORESIZE:
            #update screen size and image scale
            screenH, screenW = event.h, event.w
            screen = pygame.display.set_mode((screenH, screenW), pygame.RESIZABLE)
            apod = pygame.transform.scale(imageData, (screenH, screenW))
    
    #fill background with a color
    print('screen fill')
    screen.fill((155, 200, 10))
    nasaSurface(apod)
    
    #update the display
    print('screen flip')
    pygame.display.flip()

#cleanly exit pygame
pygame.quit()

