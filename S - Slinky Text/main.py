import os
import pygame
import time
import random
import math

# knob1 = text rotation LFO rate ; knob2 = text size ; knob3 = veils transparency ; knob4 = color

class LFO : #uses three arguments: start point, max, and how far each step is.
	
	def __init__(self, start, max, step):
		self.start = start
		self.max = max
		self.step = step
		self.current = 0
		self.direction = 1

	def update(self):
        
        # when it gets to the top, flip direction
		if (self.current >= self.max) :
			self.direction = -1
			self.current = self.max  # in case it steps above max
        
        # when it gets to the bottom, flip direction
		if (self.current <= self.start) :
			self.direction = 1
			self.current = self.start  # in case it steps below min
			
		self.current += self.step * self.direction
		
		return self.current

lfo1 = LFO(-1000,1000,1)

def setup(screen, etc):
    pass

def draw(screen, etc):
    
    avg = 0
    unistr = unichr(56) + unichr(56) + unichr(56) + unichr(56) + unichr(56) + unichr(56) + unichr(56) + unichr(56)   #"88888888"...use unicode value for each character
    size = int(etc.knob2 * 200) + 5    
    font = pygame.font.Font(etc.mode_root + "/font.ttf", size)
    textpos = (0,0)
    phrase = 6
    lfo1.step = etc.knob1*5
    
    for i in range(0, 100) :
        scalar = int(etc.knob2*20+2)
        avg = etc.audio_in[i] + avg
        avg = scalar*avg / (i + 1)
    
    for i in range(phrase) :
    
        color = etc.color_picker()
        if .9 <= etc.knob4 :
            color = (int(127 + 127 * math.sin((i*7) * .1 + time.time())),
                    int(127 + 127 * math.sin((i*7) * .05+ time.time())),
                    int(127 + 127 * math.sin((i*7) * .01 + time.time())))
        if .1 >= etc.knob4 :
            color = (int(127 + 127 * math.sin((i*7) * .1 + time.time())),
                    int(127 + 127 * math.sin((i*7) * .1+ time.time())),
                    int(127 + 127 * math.sin((i*7) * .1 + time.time())))
    
        text = font.render(unistr, True, (color))   
        R = 1
        R = R + (avg / 10) * (i * .5)
        x = R * math.cos((lfo1.update() /  1000.) * 6.28) + 640
        y = R * math.sin((lfo1.update() /  1000.) * 6.28) + 360
        
        textpos = text.get_rect(center = (x,y))
        screen.blit(text, textpos)

#TRAILS
    veil = pygame.Surface((1280,720))  
    veil.set_alpha(int(etc.knob3 * 200)) # adjust transparency on knob3
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0,0)) # (0,0) = starts at top left 
   

