
import pygame
import random
import time
import math
import pygame.gfxdraw

def setup(screen, etc):
    pass

def draw(screen, etc):

    shift3 = etc.knob3 #r channel rate
    shift2 = etc.knob2 #g channel rate
    shift1 = etc.knob1 #b channel rate
    master = shift1+shift2+shift3+.001 #vortex shape modifier
    select = int(etc.knob4*4) #color mode toggle
    
    if 0 <= select < 1 :
        for i in range(720):
            xshift = int((etc.audio_in[(i)%99]/60))
            color = (int(127 + 127 * math.sin(i * .01*shift1 + time.time())),
                    int(127 + 127 * math.sin(i * .01*shift2 + time.time())),
                    int(127 + 127 * math.cos(i * .01*shift3 + time.time())))
            radius = int(12 + 12 * math.cos(i * .02 + time.time()))
            xpos = int(1280 / 2 + 100 * math.sin(i * (9-master) + time.time()))
            pygame.gfxdraw.filled_circle(screen, xpos + xshift, i, int(abs(radius)), color)
    
    if 1 <= select < 2 :
        for i in range(720):
            xshift = int((etc.audio_in[(i)%99]/60))
            color = (int(127 + 127 * math.cos(i * .1*shift1 + time.time())),
                    int(127 + 127 * math.sin(i * .1*shift2 + time.time())),
                    int(127 + 127 * math.sin(i * .1*shift3 + time.time())))
            radius = int(12 + 12 * math.sin(i * .02 + time.time()))
            xpos = int(1280 / 2 + 100 * math.sin(i * (12+master) + time.time()))
            pygame.gfxdraw.filled_circle(screen, xpos + xshift, i, int(abs(radius)), color)  
    
    if 2 <= select < 3 :
        for i in range(720):
            xshift = int((etc.audio_in[(i)%99]/60))
            color = (int(127 + 127 * math.sin(i * 1*shift1 + time.time())),
                    int(127 + 127 * math.cos(i * 1*shift2 + time.time())),
                    int(127 + 127 * math.sin(i * 1*shift3 + time.time())))
            radius = int(12 + 12 * math.sin(i * .006*master + time.time()))
            xpos = int(1280 / 2 + 100 * math.sin(i * (18+master) + time.time()))
            pygame.gfxdraw.filled_circle(screen, xpos + xshift, i, int(abs(radius)), color)
            
    if 3 <= select :
        for i in range(720):
            xshift = int((etc.audio_in[(i)%99]/60))
            color = (int(127 + 127 * math.tan(i *(.001+(shift1*.01)) + time.time()))%255,
                    int(127 + 127 * math.tan(i * (.001+(shift2*.01)) + time.time()))%255,
                    int(127 + 127 * math.tan(i * (.001+(shift3*.01)) + time.time()))%255)
            radius = int(12 + 12 * math.sin(i * .02 + time.time()))
            xpos = int(1280 / 2 + 100 * math.sin(i * (3+master) + time.time()))
            pygame.gfxdraw.filled_circle(screen, xpos + xshift, i, int(abs(radius)), color)
                    