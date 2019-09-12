import pygame
from pygame.locals import *
from time import time
import math

clock = pygame.time.Clock()

pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode((width,height))
backcolour = (255,255,255)

running = True

angle = 0

dots = []
wait = 0

while running:

    screen.fill(backcolour)

    clock.tick(60)

    if angle < 359:
        angle += 1
    if angle == 359:
        wait = time()
        angle = 360
    if time() - wait >= 2 and wait != 0:
        angle = 0
        dots = []
        wait = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x = (math.cos(math.radians(angle - 90)) * 200) + 250
    y = (math.sin(math.radians(angle - 90)) * 200) + 250
    point = [int(x),int(y)]

    if angle % 60 == 0:
        dots.append((point[0], point[1]))
    
    pygame.draw.circle(screen, (198,198,198), (250,250), 200, 1)
    pygame.draw.line(screen, (0,0,255), (250,250), (point[0], point[1]), 1)

    i = 0
    while i < len(dots):
        pygame.draw.circle(screen, (0,0,255), dots[i], 5)
        i += 1

    if angle == 360:
        pygame.draw.lines(screen, (0,0,255), True, dots, 1)
        
    pygame.display.flip()

pygame.quit()
