import os
import pygame


def setup(screen, etc) :
    pass

def draw(screen, etc) :
    
    for i in range (0,50) :
        
        x0 = int((etc.knob1*640) + 640) 
        x1 = x0 + (etc.audio_in[i] / 35)
        y = i * 14.4
        color = etc.color_picker() #on knob4
        pygame.draw.line(screen, color, [x0, y], [x1, y], int(etc.knob2*100+1))

    for i in range (51,100) :
       
        x0 = int(640 - (etc.knob1*640))
        x1 = x0 + (etc.audio_in[i] / 35)
        y = (i - 50) * 14.4
        color = etc.color_picker() #on knob4
        pygame.draw.line(screen, color, [x0, y], [x1, y], int(etc.knob2*100+1))

#print background color layer over entire image
    veil = pygame.Surface((1280,720))  
    veil.set_alpha(int(etc.knob3 * 200)) # adjust transparency on knob3
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0,0)) # (0,0) = starts at top left