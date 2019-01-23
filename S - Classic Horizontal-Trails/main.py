import os
import pygame

def setup(screen,etc) :
    pass

def draw(screen, etc):

    for i in range(0, 100) :
        seg(screen, etc, i)

 #print background color layer over entire image
    veil = pygame.Surface((1280,720))  
    veil.set_alpha(int(etc.knob3 * 200)) # adjust transparency on knob3
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0,0)) # (0,0) = starts at top left 
        
def seg(screen, etc, i) :

    y0 = 0
    y1 = (etc.audio_in[i] / 90)
    x = i * 13 - 10
    
    linewidth = int(etc.knob1*10)
    position = 360
    ballSize = int(etc.knob2*50)
    color = etc.color_picker()
    
    pygame.draw.circle(screen,color,(x, y1+position),ballSize, 0)
    pygame.draw.line(screen, color, [x, y0+position], [x, y1+position], linewidth)