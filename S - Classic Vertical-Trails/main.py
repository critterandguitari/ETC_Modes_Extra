import os
import pygame


def setup(screen,etc):
    pass

def draw(screen, etc):
    
#draw Classic Vertical, see params below:
    for i in range(0, 100) :
        
        seg(screen, etc, i)
   
#Trails
    veil = pygame.Surface((1280,720))  
    veil.set_alpha(int(etc.knob3 * 200)) # adjust transparency on knob3
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0,0)) # (0,0) = starts at top left
    
def seg(screen, etc, i) :
    
    x0 = 0
    x1 = 0 + (etc.audio_in[i] / 35)
    y = i * 8 - 40
    
    linewidth = int(etc.knob1*10)
    position = int(.5*1280)
    ballSize = int(etc.knob2*50)
    color = etc.color_picker()
    
    pygame.draw.circle(screen,color,(x1+position, y),ballSize, 0)
    pygame.draw.line(screen, color, [x0+position, y], [x1+position, y], linewidth)
    
    
   