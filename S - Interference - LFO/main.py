import os
import pygame
import time
import random

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

fanner = LFO(1,260,1)
pointer = LFO(1,260,1)

def setup(screen, etc):
    pass

def draw(screen, etc):
    
    lines = int(etc.knob1*59)+1
    color = etc.color_picker() #knob4
    
    fanner.step = int(etc.knob1*10)
    pointer.step = int(etc.knob1*10)
  
    R = etc.audio_in[1]*0.01 + 360
    L = etc.audio_in[11]*0.01 + 360
    T = etc.audio_in[21]*0.01 + 360
    E = etc.audio_in[45]*0.01 + 360
    F = etc.audio_in[75]*0.01 + 360

    fan=fanner.update()*etc.knob3/8
    point=pointer.update()*etc.knob2/8
    
    for i in range (0,lines) :
        
        modi = i%2
        if modi == 1 :
            pygame.draw.aalines(screen, color, True, [[0, R-i*point], [640, L-i*fan], [1280, T-i*point], [960, E-i*fan], [340, F-i]], 1)
        if modi == 0 :
            pygame.draw.aalines(screen, color, True, [[0, R+i*point], [640, L+i*fan], [1280, T+i*point], [960, E+i*fan], [340, F+i]], 1)
