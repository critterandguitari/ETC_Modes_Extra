import os
import pygame
import time
import random
import math

rad = 5
xpos = 300
ypos = 300
color = (0,0,0)
last_point = [320, 0]
last_point1 = [320, 0]

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

lfo1 = LFO(-200,200,1)
lfo2 = LFO(-300,300,1)

def setup(screen, etc) :
    pass

def draw(screen, etc) : 
    global rad, xpos, ypos, color, last_point, last_point1
    
    color = etc.color_picker()
    audio1 = etc.audio_in[0] /450
    audio2 = etc.audio_in[1] /450
    linewidth= int(etc.knob1*20)+1
    #mouth
    for i in range(0, 100) :
        
        xscale = (640/99*i)
        xoffset = int(640+xscale)*etc.knob2*i/128 + (720-etc.knob2*640) #mouth width
        yoffset = 600 - etc.audio_in[2]/640
        auDio = etc.audio_in[i] / (500-int(etc.knob2*499))
        color = etc.color_picker()
        
        if i == 0 : last_point = [(0*etc.knob2+ -auDio)+ (720-etc.knob2*640), (yoffset+ auDio)]
        
        pygame.draw.line(screen, color, last_point, [xoffset + -auDio, yoffset + auDio], linewidth)
        last_point = [(xoffset + -auDio),(yoffset + auDio)]
    #eyes
    rad = int(etc.knob1*200)+20 #eye size
    xpos1 = 400+audio1
    ypos1 = 240-audio1
    xpos2 = 880-audio2
    ypos2 = 240-audio2
    xrad = (rad/2) * math.sin((etc.audio_in[20]*.0001)) 
    yrad = (rad/2) * math.cos((etc.audio_in[25]*.0001))
    
    lfo1.step = etc.knob3*30 #eye bounce speed
    lfo2.step = etc.knob3*40
    roll1 = int(lfo1.update())
    roll2 = -int(lfo1.update())
    slide1 = int(lfo2.update())
    slide2 = -int(lfo2.update())
    
    pygame.draw.circle(screen, color, [xpos1+slide1,ypos1+roll1], rad)
    pygame.draw.circle(screen, (245,200,255), [xpos1+int(xrad)+slide1,ypos1-int(yrad)+roll1], rad/2)
    pygame.draw.circle(screen, color, [xpos2+slide2,ypos2+roll2], rad)
    pygame.draw.circle(screen, (245,200,255), [xpos2+int(xrad)+slide2,ypos2-int(yrad)+roll2], rad/2)

    
    
    
    
        
    
   
       
        
   
    
    