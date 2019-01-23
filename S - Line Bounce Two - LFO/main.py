import os
import pygame
import math

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

bounce1 = LFO(100,1180,10)
bounce2 = LFO(100,1180,19)
bounce3 = LFO(0, 25, 1)
y = 0

def setup(screen, etc):
	pass
    
def draw(screen, etc):
    global bounce1, bounce2, y
    
    y = etc.audio_in[50] / 150

    color = etc.color_picker()
    color2 = etc.color_picker()

    bounce1.step = etc.knob3*10+1
    bounce2.step = etc.knob3*19+2
    posx1 = bounce1.update()
    posx2 = bounce2.update()
    width = int(etc.knob2*100)+1
    #rate = etc.knob1*3*bounce3.step+1
    rise = int((bounce3.update()* etc.knob1*10))+1
    
    pygame.draw.line(screen, color, [posx1, 100-(y+rise)], [posx1, 300+rise], width)
    pygame.draw.line(screen, color2, [posx2, 300+rise], [posx2, 480+y+rise], width*2)
    
    
    
    
    