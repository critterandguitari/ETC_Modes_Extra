import os
import pygame
import time
import random
import math

x21 = y21 = x2=y2=x3=y3=x11=y11=x1=y1=x4=y4=0
sound = 0

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    global sound
    
    if etc.audio_trig or etc.midi_note_new :
        sound = (((2*etc.knob2-1)/10 + sound))

    a = math.pi*sound
    xc = 640
    yc = 360
    linewidth = 640 - int(etc.knob1*639)
    L = etc.knob1*1000 + linewidth
    if L > 1280 : L = 1280
    
    color = etc.color_picker()
    
    if etc.knob2 < .5 :
        x21 = (L/2)*math.cos(a)
        y21 = (L/2)*math.sin(a)
        x2 = int(xc+x21)
        y2 = int(yc-y21)
        x3 = int(xc-x21)
        y3 = int(yc+y21)
        pygame.draw.line(screen, color, [x2,y2], [x3, y3], linewidth)
    
    if etc.knob2 > .5 :
        x11 = (L/2)*math.cos(a)
        y11 = (L/2)*math.sin(a)
        x1 = xc-x11
        y1 = yc+y11
        x4 = xc+x11
        y4 = yc-y11
        pygame.draw.line(screen, color, [x1,y1], [x4, y4], linewidth)
    
    
    #Trails
    veil = pygame.Surface((1280,720))  
    veil.set_alpha(int(etc.knob3 * 200))
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0,0))


