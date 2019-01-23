import os
import pygame
import random
import math

trigger = False
xpos = []
x = 0
y = 0
height = 720 
width = 1300
linelength = 50
lineAmt = 20
xpos = [random.randrange(-200, 1280) for i in range(0, lineAmt+2)]

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

ymover = LFO(1,360,10)

def setup(screen, etc):
    pass

def draw(screen, etc):
    global trigger, x, y, height, width, xpos, lineAmt, linelength
    
    ymover.step = int(etc.knob3*10) #set LFO Step (rate of change)
    linewidth = (height / lineAmt) + ymover.update()
    
    linelength = int(etc.knob2*100)
    color = etc.color_picker()
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
        
    if trigger == True :
        
        lineAmt = int(etc.knob1*60 + 1)
        xpos = [random.randrange(-200, 1280) for i in range(0, lineAmt+2)]
    
    trigger = False           
            
    for i in range(0, lineAmt+2) :
        
        auDio = int(etc.audio_in[i] / 180)
       
        x = xpos[i] + linelength
        y = (i * linewidth) + int(linewidth/2)- 1
        if y >= 720 : y =   y-480
        pygame.draw.line(screen, color, (xpos[i]+(auDio / 4), y), (x+auDio, y + etc.knob3*50-25 ), linewidth)
    
