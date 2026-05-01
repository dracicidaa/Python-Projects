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
    return imageBits


#Initialize the screen, 
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('NASA Image Of The Day V0.1')

#Main loop
running = True
while running:
    #check for events
    print('check events')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #fill background with a color
    print('screen fill')
    screen.fill((155, 200, 10))
    nasaAPOD = pygame.image.load(nasaPicture()).convert()

    #blit the photo of the day to the screen
    print('screen blit')
    screen.blit(nasaAPOD, (0,0))

    #update the display
    print('screen flip')
    pygame.display.flip()

#cleanly exit pygame
pygame.quit()

