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
    unistr1 = unichr(67) + unichr(82) + unichr(73) + unichr(84) + unichr(84) + unichr(69) + unichr(82)   #"88888888"...use unicode value for each character
    unistr2 = unichr(71) + unichr(85) + unichr(73) + unichr(84) + unichr(65) + unichr(82) + unichr(73)   #"88888888"...use unicode value for each character
    unistr3 = unichr(38)
    
    size = int(etc.knob2 * 100) + 5    
    font = pygame.font.Font(etc.mode_root + "/font.ttf", size)
    textpos1 = (0,0)
    textpos2 = (0,0)
    textpos3 = (0,0)
    phrase = 6
    lfo1.step = etc.knob1*5
    
    sel  = etc.knob4*8
    
    for i in range(0, 100) :
        scalar = int(etc.knob2*20+2)
        avg = etc.audio_in[i] + avg
        avg = scalar*avg / (i + 1)
    
    for i in range(phrase) :
    
        color = etc.color_picker()
        if sel >= 7 :
                color = (int(127 + 127 * math.sin((i*7) * .1 + time.time())),
                    int(127 + 127 * math.sin((i*7) * .05+ time.time())),
                    int(127 + 127 * math.sin((i*7) * .01 + time.time())))
        if 1 <= sel < 2 :
                color = (int(127 + 127 * math.sin((i*7) * .1 + time.time())),45,72)
        if 2 <= sel < 3 :
                color = (75,int(127 + 127 * math.sin((i*7) * .1 + time.time())),42)
        if 3 <= sel < 4 :
                color = (42,75,int(127 + 127 * math.sin((i*7) * .1 + time.time())))
        if 4 <= sel < 5 :
                color = (int(127 + 127 * math.sin((i*7) * .1 + time.time())),220,0)
        if 5 <= sel < 6 :
                color = (255,int(127 + 127 * math.sin((i*7) * .1 + time.time())),0)
        if 6 <= sel < 7 :
                color = (176,175,int(127 + 127 * math.sin((i*7) * .1 + time.time())))    
        if 1 > sel :
                color = (int(127 + 127 * math.sin((i*7) * .1 + time.time())),
                        int(127 + 127 * math.sin((i*7) * .1 + time.time())),
                        int(127 + 127 * math.sin((i*7) * .1 + time.time()))) # color on knob4

        
        text1 = font.render(unistr1, True, (color))   
        text2 = font.render(unistr2, True, (color))
        text3 = font.render(unistr3, True, (color)) 

        R = 1
        R = R + (avg / 10) * (i * .5)
        x = abs(R * math.cos((lfo1.update() /  1000.) * 6.28) + 640)
        y = abs(R * math.sin((lfo1.update() /  1000.) * 6.28) + 360)
        
        R1 = 1
        R1 = R1 + (avg / 10) * (i * .5)
        x1 = abs(R1 * math.sin((lfo1.update() /  1000.) * 6.28) + 640)
        y1 = abs(R1 * math.cos((lfo1.update() /  1000.) * 6.28) + 360)
        
        textpos1 = text1.get_rect(center = (x,y-size/1.25))
        screen.blit(text1, textpos1)
        
        textpos2 = text2.get_rect(center = (x,y+size/1.25))
        screen.blit(text2, textpos2)

        textpos3 = text3.get_rect(center = (x1,y1))
        screen.blit(text3, textpos3)

#TRAILS
    veil = pygame.Surface((1280,720))  
    veil.set_alpha(int(etc.knob3 * 200)) # adjust transparency on knob3
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0,0)) # (0,0) = starts at top left 