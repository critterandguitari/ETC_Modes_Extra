import os
import pygame
import random
import math

trigger = False
ypos = []
x = 0
y = 0
height = 800 
width = 1280
linelength = 50
lineAmt = 20
ypos = [random.randrange(-100, height) for i in range(0, lineAmt + 2)]

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

xmover = LFO(1,640,10)

def setup(screen, etc):
     pass

def draw(screen, etc):
    global trigger, x, y, height, width, ypos, lineAmt, linelength
    
    xmover.step = int(etc.knob3 * 20) #set LFO Step (rate of change)
    linewidth = (width / lineAmt) + xmover.update()
    linelength = int(etc.knob2*600 + 1)
    color = etc.color_picker()
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
        
    if trigger == True :
        lineAmt = int(etc.knob1*69 + 1)
        ypos = [random.randrange(-100, height) for i in range(0, lineAmt + 2)]
    
    trigger = False           
            
    for j in range(0, lineAmt + 2) :
        
        auDio = int(etc.audio_in[j] / 180)
        y = ypos[j] + linelength
        x = (j * linewidth) + (linewidth/2)- 1
        if x > 1280 : x = x-960
        pygame.draw.line(screen, color, (x, ypos[j]+(auDio / 4)), (x+ int(etc.knob3 * 50 - 25), y+auDio), linewidth)
    
