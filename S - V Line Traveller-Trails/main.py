import os
import pygame
import time

x = 640
count = 0

def setup(screen, etc):
    pass

def draw(screen, etc):
    global count, x
    
    speed = etc.knob2*40 - 20
    count = int(count + speed)
    thick = int(etc.knob1*1279)+1
    color = etc.color_picker()
    peak = 0
    
    for i in range(0,100) :
        if etc.audio_in[i] > peak:
            peak = etc.audio_in[i]
    
    H =  peak/8
    y1 = 360 - H
    y2 = 360 + H
    
    if peak > 16:
        pygame.draw.line(screen, color, [x, y1], [x, y2], thick)
    x = x + speed
    if x > 1280 + thick/2 : x = 0 - thick/2 
    if x < 0 - thick/2 : x = 1280 + thick/2

    #Trails
    veil = pygame.Surface((1280,720))  
    veil.set_alpha(int(etc.knob3 * 200))
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0,0))