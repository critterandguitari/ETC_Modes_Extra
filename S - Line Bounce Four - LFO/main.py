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
bounce3 = LFO(0,360,2)
bounce4 = LFO(360,720,2)
y = 0

def setup(screen, etc):
	pass
    
def draw(screen, etc):
    global bounce1, bounce2, bounce3, bounce4, y
    
   
    y = etc.audio_in[50] / 150
    
    #create many so the random colors are different....
    color = etc.color_picker()
    color2 = etc.color_picker()
    color3 = etc.color_picker()
    color4 = etc.color_picker()
    
    size1 = int(etc.knob1 * 100) +1
    size2 = int(etc.knob2 * 50) +1
    
    bounce1.step = int(etc.knob3 * 15)+5
    bounce2.step = int(etc.knob3 * 30)+5
    bounce3.step = int(etc.knob3 * 5)+2
    bounce4.step = int(etc.knob3 * 5)+2

    posx1 = bounce1.update()
    posx2 = bounce2.update()
    posy1 = bounce3.update()
    posy2 = bounce4.update()
    
    pygame.draw.line(screen, color3, [0, posy1], [1280, posy1], size2)
    pygame.draw.line(screen, color4, [0, posy2], [1280, posy2], size2) 
    pygame.draw.line(screen, color, [posx1, 180-y], [posx1, 360], size1)
    pygame.draw.line(screen, color2, [posx2, 360], [posx2, 540+y], size1)
       
    
    
    
    