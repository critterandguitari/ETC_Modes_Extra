import os
import pygame

def setup(screen, etc):
    pass

def draw(screen, etc):
    
    R = 1 
    
    peak = 0
    for i in range(0,100) :
        if etc.audio_in[i] > peak:
            peak = etc.audio_in[i]
    R = (peak / 100) + (0.5 * 100)

    x = int(etc.knob1*1280)
    y = int(etc.knob2*720)
    color = etc.color_picker()
    
    pygame.draw.circle(screen,color,(x,y),(int(R)+10))

    #TRAILS
    veil = pygame.Surface((1280,720))  
    veil.set_alpha(int(etc.knob3 * 200)) # adjust transparency on knob3
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0,0)) # (0,0) = starts at top left 
    
        
