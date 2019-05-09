import os
import pygame
import time
import random
import math

lines = 20 
width = 720 / lines
offset = width / 2
xpos = 0

def setup(screen, etc):
    pass

def draw(screen, etc):
    global lines, offset, width, xpos
    # knob1 = x position ; knob2 = line thickness ; knob 3 = veil transparency ; knob 4 = color selector
    
    for i in range(0, lines) :
        color = etc.color_picker()
        pygame.draw.line(screen, color, [1280*etc.knob1-etc.audio_in[1]/40, 360-int(etc.audio_in[50]/40)], 
                                        [1280, offset + (i * width)], int(etc.knob2*39)+1)
        pygame.draw.line(screen, color, [0, offset + (i * width)], [1280*etc.knob1-etc.audio_in[1]/40, 360-int(etc.audio_in[50]/40) ], 
                                        int(etc.knob2*39)+1)

#TRAILS
    veil = pygame.Surface((1280,720))  
    veil.set_alpha(int(etc.knob3 * 200)) # adjust transparency on knob3
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0,0)) # (0,0) = starts at top left 
