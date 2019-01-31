import os
import pygame
import glob
import random


last_screen = pygame.Surface((1280,720))

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    global last_screen
    
    if etc.audio_trig or etc.midi_note_new :
        if etc.knob4 < .5 :
            r=g=b= int(etc.knob4*509+1) # first half of knob4 is graycale
        
        if etc.knob4 >= .5 :
            r = random.randrange(10,int(244*etc.knob4+11)) # second half of knob4 is color
            g = random.randrange(10,int(244*etc.knob4+11))
            b = random.randrange(10,int(244*etc.knob4+11))
        
        x = random.randrange(0,1280)
        y = random.randrange(0,720)
        pygame.draw.circle(screen,(r,g,b),[x,y],int(200*etc.knob1+10)) # ball size on knob1

    image = last_screen
    last_screen = screen.copy()
    thing = pygame.transform.scale(image, (int(1270*etc.knob2), int(710*etc.knob2)) ) # mirror screen scale
    thing.set_alpha(int(etc.knob3 * 200)) # adjust transparency on knob3
    screen.blit(thing, (640-int(etc.knob2*635), 360-int(etc.knob2*355))) # mirror screen scale
