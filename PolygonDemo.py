"""
Polygon Drawing Demo
By u/iceninja1234567
"""
import pygame #Used to draw polygon
from pygame.locals import *
from time import time #Used to time the increase in sides
import math #Used to work out the position of ecah vertex

clock = pygame.time.Clock() #Creates pygame clock instance

pygame.init() #Initialises pygame

width = 500 #Defines width and height
height = 500
screen = pygame.display.set_mode((width,height)) #Creates main surface
backcolour = (255,255,255) #Defines WHITE background colour

pygame.display.set_caption("Polygons") #Sets title

size25 = pygame.font.SysFont('Ariel', 25) #Font used for text in corner
def txt(size,text,color,tx,ty): #Function to render text, borrowed from an older peice of code I wrote so isn't ideal
    label = size25.render(text, 1, color)
    screen.blit(label, (tx,ty))
    
running = True #Variable that decides if the game loop continues to run

angle = 0 #Angle to find vertex at
increase = 0 #Timer variable to increase side count every 0.25s

sides = 3 #Current number of sides

while running: #Main game loop

    screen.fill(backcolour) #Fills in entire screen

    clock.tick(60) #Timing

    if increase == 0: #When the loop first begins...
        increase = time() #...get the current timer()
    if time() - increase >= 0.25: #If 0.25s has passed since the last increase...
        sides += 1 #...increase the side count by 1
        increase = time() #Reset the timer
    
    for event in pygame.event.get(): #If the X is pressed, close the demo
        if event.type == pygame.QUIT:
            running = False

    points = [] #List of co-ordinates for all of the verticies
    angle = 0 #Angle from centre to find next vertex

    i = 0
    while i < sides: #Repeats for each vertex to find
        x = (math.cos(math.radians(angle - 90)) * 200) + 250 #Finds x co-ordinate
        y = (math.sin(math.radians(angle - 90)) * 200) + 250
        points.append((x, y)) #Adds co-ordinate to list
        angle += 360.0 / sides #Increase the angle by a certain fraction of 360 degrees.
        i += 1

    """
    The way it works is using some basic trigonometry. The program works by using an "arm" method. There is an arm facing upwards, at 0 degrees, with a length of 200px, starting at the centre of the screen.
    The end of this "arm" is where the vertex of the polygon is. The "arm" then rotates by a certain amount (360/side count). The new end position of the "arm" is the next vertex. This repeats for each side until the "arm" completes a full 360 degree rotation.
    """

    pygame.draw.circle(screen, (255,0,0), (250, 250), 200, 1) #Draws red reference circle
    pygame.draw.lines(screen, (0,0,255), True, points, 1) #Draws polygon from list

    txt(25, "Sides: " + str(sides), (0,0,255), 5, 5) #Displays side count in corner
        
    pygame.display.flip() #Updates screen

pygame.quit() #Closes pygame window when X is clicked
