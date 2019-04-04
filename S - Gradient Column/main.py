
import pygame
import random
import time
import math
import pygame.gfxdraw

def setup(screen, etc):
    pass

def draw(screen, etc):
    
    cool = int(etc.knob1*710)+10 # number of circles and height
    yoff = int(360-etc.knob1*360)
    xtra = int(etc.knob2*1278)+2 # width control
    segs = 99 # number of audio data points to look at
    sel  = etc.knob4*5 # color select switch
    swell = etc.knob3*.999 + .001 # radius and scope shape
    
    if 0 <= sel < 1 : #grayscale
        for i in range(cool):
            audiopuff = (int(etc.audio_in[i%segs]/1000)+1)
            color = (int(127 + 127 * math.sin(i * .01 + time.time())),
                    int(127 + 127 * math.sin(i * .01 + time.time())),
                    int(127 + 127 * math.sin(i * .01 + time.time())))
            radius = int(12 + 12 * math.sin(i * .1*swell + time.time()))
            xpos = int((640 - xtra/144) + (xtra/2) * math.sin(i * 2.5 + time.time()))
            pygame.gfxdraw.filled_circle(screen, xpos, i+audiopuff+yoff, abs(radius), color)            
    
    if 1 <= sel < 2 :    # red
        for i in range(cool):
            audiopuff = (int(etc.audio_in[i%segs]/1000)+1)
            color = (int(127 + 127 * math.sin(i * .005 + time.time())),
                    0,
                    0)
            radius = int(12 + 12 * math.sin(i * .1*swell + time.time()))
            xpos = int((640 - xtra/144) + (xtra/2) * math.sin(i * 2.5 + time.time()))
            pygame.gfxdraw.filled_circle(screen, xpos, i+audiopuff+yoff, abs(radius), color)
    
    if 2 <= sel < 3 :    # green    
        for i in range(cool):
            audiopuff = (int(etc.audio_in[i%segs]/1000)+1)
            color = (0,
                    int(127 + 127 * math.sin(i * .01 + time.time())),
                    0)
            radius = int(12 + 12 * math.sin(i * .1*swell + time.time()))
            xpos = int((640 - xtra/144) + (xtra/2) * math.sin(i * 2.5 + time.time()))
            pygame.gfxdraw.filled_circle(screen, xpos, i+audiopuff+yoff, abs(radius), color)
    
    if 3 <= sel < 4 :        # blue
        for i in range(cool):
            audiopuff = (int(etc.audio_in[i%segs]/1000)+1)
            color = (0,
                    0,
                    int(127 + 127 * math.sin(i * .02 + time.time())))
            radius = int(12 + 12 * math.sin(i * .1*swell + time.time()))
            xpos = int((640 - xtra/144) + (xtra/2) * math.sin(i * 2.5 + time.time()))
            pygame.gfxdraw.filled_circle(screen, xpos, i+audiopuff+yoff, abs(radius), color)    
            
    if 4 <= sel :        # rainbow
        for i in range(cool):
            audiopuff = (int(etc.audio_in[i%segs]/1000)+1)
            color = (int(127 + 127 * math.sin(i * .005 + time.time())),
                    int(127 + 127 * math.sin(i * .01 + time.time())),
                    int(127 + 127 * math.sin(i * .02 + time.time())))
            radius = int(12 + 12 * math.sin(i * .1*swell + time.time()))
            xpos = int((640 - xtra/144) + (xtra/2) * math.sin(i * 2.5 + time.time()))
            pygame.gfxdraw.filled_circle(screen, xpos, i+audiopuff+yoff, abs(radius), color)