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

#Initialize stuff
pygame.init()
load_dotenv()
apiKey = os.getenv('NASA_KEY')
nasa = nasapy.Nasa(apiKey)

#Functions
def nasaPicture():
    #Get nasa image of the day
    apod = nasa.picture_of_the_day(date='2000-04-28')
    imgUrl = apod['url']
    #download the photo into ram
    response = requests.get(imgUrl)
    imageBits = io.BytesIO(response.content)
    imageBits.seek(0)
    return imageBits

def nasaSurface(imageData):
    #get needed image, rects, centers
    nasaAPOD = pygame.image.load(imageData).convert()
    screenRect = screen.get_rect()
    imageRect = nasaAPOD.get_rect()
    imageRect.center = screenRect.center
    #blit the photo of the day to the screen
    print('screen blit')
    screen.blit(nasaAPOD, imageRect)


#Initialize the screen, 
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption('NASA Image Of The Day V0.1')

#Fetch the daily image to initialize
imageData = pygame.image.load(nasaSurface(nasaPicture()))
#Main loop
running = True
while running:
    #check for events
    print('check events')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.VIDEORESIZE:
            #update screen size
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    
    #fill background with a color
    print('screen fill')
    screen.fill((155, 200, 10))
    nasaSurface(imageData)
    
    #update the display
    print('screen flip')
    pygame.display.flip()

#cleanly exit pygame
pygame.quit()

