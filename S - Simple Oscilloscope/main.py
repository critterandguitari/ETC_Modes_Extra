import os
import pygame
    
last_point = [0, 360]
first_point = []


def setup(screen, etc):
    pass

def draw(screen, etc):
    global last_point, first_point
    
    #Lines
    for i in range(0, 100) :
        lineseg(screen, etc, i)
    
    #Trails
    veil = pygame.Surface((1280,720))  
    veil.set_alpha(int(etc.knob3 * 200))
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0,0))

def lineseg(screen, etc, i):
    global last_point, first_point
    
    linewidth = int(etc.knob1*100)+1
    y1 = int(etc.knob2 * 720) + (etc.audio_in[i] / 75)
    x = (i * 15) - 110
    color = etc.color_picker()

    if i == 0 : 
        last_point = [-110, 360]
    else :
        last_point = last_point
    
    pygame.draw.line(screen, color, last_point, [x , y1], linewidth)
    last_point = [x , y1]