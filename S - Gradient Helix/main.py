
import pygame
import random
import time
import math
import pygame.gfxdraw
# original code adapted from zach lieberman's talk
# https://www.youtube.com/watch?v=bmztlO9_Wvo

def setup(screen, etc):
    pass 

def draw(screen, etc):
    cool = 720
    ypos = 360-int(cool)/2
    xtra = int(etc.knob1*1280) + int(360*etc.knob2*math.sin(.5 + time.time())) # L-R control
    segs = int(etc.knob3*96+3) # number of audio data points to look at
    sel  = etc.knob4*5 # color select switch
    puff = etc.knob3 # radius
    
    if 0 <= sel < 1 :
    
        for i in range(cool):
        
            xshift = int(5*(etc.audio_in[(i)%segs]/300)) + xtra
            color = (int(128 + 127 * math.sin(i * .04 + time.time())),
                     int(127 + 127 * math.sin(i * .04 + time.time())),
                     int(127 + 127 * math.sin(i * .04 + time.time())))
            radius = abs(int(20  + 30  * math.sin(i *  .005 + time.time())))
            xpos = int(0 + 100 * math.sin(i * .8 + time.time())) 
            pygame.gfxdraw.filled_circle(screen, xpos+xshift, i+ypos, int(radius*puff)+1, color)
            
    if 1 <= sel < 2 :
    
        for i in range(cool):
        
            xshift = int(5*(etc.audio_in[(i)%segs]/300)) + xtra
            color = (int(128 + 127 * math.sin(i * .04 + time.time())),0,0)
            radius = abs(int(20  + 30  * math.sin(i *  .005 + time.time())))
            xpos = int(0 + 100 * math.sin(i * .8 + time.time()))
            pygame.gfxdraw.filled_circle(screen, xpos+xshift, i+ypos, int(radius*puff)+1, color)   
    
    if 2 <= sel < 3 :
    
        for i in range(cool):
        
            xshift = int(5*(etc.audio_in[(i)%segs]/300)) + xtra
            color = (0, int(127 + 127 * math.sin(i * .018 + time.time())),0)
            radius = abs(int(20  + 30  * math.sin(i *  .005 + time.time())))
            xpos = int(0 + 100 * math.sin(i * .8 + time.time()))
            pygame.gfxdraw.filled_circle(screen, xpos+xshift, i+ypos, int(radius*puff)+1, color)   
            
    if 3 <= sel < 4 :
    
        for i in range(cool):
        
            xshift = int(5*(etc.audio_in[(i)%segs]/300)) + xtra
            color = (0,0,int(127 + 127 * math.sin(i * .012 + time.time())))
            radius = abs(int(20  + 30  * math.sin(i *  .005 + time.time())))
            xpos = int(0 + 100 * math.sin(i * .8 + time.time()))
            pygame.gfxdraw.filled_circle(screen, xpos+xshift, i+ypos, int(radius*puff)+1, color)
            
    if 4 <= sel :
            
        for i in range(cool):
            
            xshift = int(5*(etc.audio_in[(i)%segs]/300)) + xtra
            color = (int(128 + 127 * math.sin(i * .04 + time.time())),
                     int(127 + 127 * math.sin(i * .018 + time.time())),
                     int(127 + 127 * math.sin(i * .012 + time.time())))
            radius = abs(int(20  + 30  * math.sin(i *  .005 + time.time())))
            xpos = int(0 + 100 * math.sin(i * .8 + time.time()))
            pygame.gfxdraw.filled_circle(screen, xpos+xshift, i+ypos, int(radius*puff)+1, color)    