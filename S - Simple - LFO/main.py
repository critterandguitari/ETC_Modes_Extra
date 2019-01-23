import os
import pygame
    
last_point = [0, 360]
first_point = []

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

lfo1 = LFO(1,200,1)


def setup(screen, etc):
    pass

def draw(screen, etc):
    global last_point, first_point
    
    #Lines
    for i in range(0, 100) :
        lineseg(screen, etc, i)
    
    #Trails
    veil = pygame.Surface((1280,720))  
    veil.set_alpha(int(etc.knob3 * 200))
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0,0))

def lineseg(screen, etc, i):
    global last_point, first_point
    
    lfo1.step = int(etc.knob1*30)+1
    linewidth = lfo1.update()
    y1 = (int(etc.knob2 * 720) + (etc.audio_in[i] / 75))
    x = (i * 15) - 110 
    color = etc.color_picker()

    if i == 0 : 
        last_point = [-110, 360]
    else :
        last_point = last_point
    
    pygame.draw.line(screen, color, last_point, [x, y1-linewidth], linewidth)
    last_point = [x, y1+linewidth]