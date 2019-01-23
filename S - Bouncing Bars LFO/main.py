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

bounce1 = LFO(0,720,10)
bounce2 = LFO(0,720,19)
xmover1 = LFO(0,640,30)
xmover2 = LFO(0,640,15)
y = 0

def setup(screen, etc):
	pass

def draw(screen, etc):
    global bounce1, bounce2, y
    
   
    y = etc.audio_in[30] / 50
    y2 = etc.audio_in[70] / 50
    
    color = etc.color_picker()
    color2 = etc.color_picker()
    
    size1 = int(etc.knob1 * 250) +1
    
    bounce1.step = int(etc.knob3 * 25)+1
    bounce2.step = int(etc.knob3 * 50)+1
    posy1 = bounce1.update()
    posy2 = bounce2.update()
    
    xmover1.step = int(etc.knob2 * 50)+1
    xmover2.step = int(etc.knob2 * 25)+1
    posx1 = xmover1.update()
    posx2 = xmover2.update()
    
    pygame.draw.line(screen, color, [0+posx1, posy1], [y+posx1, posy1], size1)
    pygame.draw.line(screen, color, [1280-posx2, posy2], [1280-y2-posx2, posy2], size1)
    
    peak = 0
    for i in range(0,100) :
        if etc.audio_in[i] > peak:
            peak = etc.audio_in[i]
    R = (peak / 300) + (etc.knob3 * 100)

   #pygame.draw.circle(screen,color,(640, 360, (int(R)+10))
    
    
    
    
    
    