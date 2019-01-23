import os
import pygame
import time

y = 360
count = 0

def setup(screen, etc):
    pass

def draw(screen, etc):
    global count, y
    
    speed = etc.knob2*40 - 20
    count = int(count + speed)
    thick = int(etc.knob1*719)+1
    color = etc.color_picker()
    peak = 0
    
    for i in range(0,100) :
        if etc.audio_in[i] > peak :
            peak = etc.audio_in[i]
    
    L =  peak/6
    x1 = 640 - L
    x2 = 640 + L
    
    if peak > 16:
        pygame.draw.line(screen, color, [x1, y], [x2, y], thick)
    
    y = y + speed
    if y > 720 + thick/2 : y = 0 - thick/2 
    if y < 0 - thick/2 : y = 720 + thick/2

    #Trails
    veil = pygame.Surface((1280,720))  
    veil.set_alpha(int(etc.knob3 * 200))
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0,0))