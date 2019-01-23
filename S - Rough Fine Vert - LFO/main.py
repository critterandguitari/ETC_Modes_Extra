import os
import pygame
import glob
import random
import math
import time

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

bounce1 = LFO(75,650,10)
slower = 0

trigger = False
color = (0,0,0)

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    global trigger, bounce1 
    
    #oscilloscope
    for i in range(0, 100) :
        seg(screen, etc, i)
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
    if trigger == True :
        trigger = False

def seg(screen, etc, i) :
    global bounce1, slower
    
    y0 = 0
    y1 = (etc.audio_in[i] / 90)
    x = i * 13 - 10
    
    linewidth = int(etc.knob2*20)
    ballSize = int(etc.knob3*50)
    color = etc.color_picker()
    
    position = bounce1.update()
    bounce1.step = 0
    if slower >= int(etc.knob1 * 25):
        bounce1.step = int(etc.knob2 *400)
        slower = 0
    slower += 1
    
    
    pygame.draw.circle(screen,color,(x, y1+position),ballSize, 0)
    pygame.draw.line(screen, color, [x, y0+position], [x, y1+position], linewidth)
