import os
import pygame
import pygame.gfxdraw

circles = 10

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

ypos = LFO(0,720,10)

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    color = etc.color_picker() #on knob4
    ypos.step = int(etc.knob3*50) #LFO rate of change
    
    circles = int(etc.knob1*25)+1
    space = (1280/circles)
    offset = int(etc.knob2*30)
    y = ypos.update()
    
    for i in range (0, circles) :
        auDio = abs(etc.audio_in[i] / 194)
        r = auDio + offset
        ax = (i*space)+(space/2)
    
        pygame.gfxdraw.filled_circle(screen, ax, y, r, color)