import os
import pygame
import glob
import random

#NO AUDIO RESPONSE

class LFOhalf : #uses three arguments: start point, min, and how far each step is.
	
	def __init__(self, start, min, step):
		self.start = start
		self.min = min
		self.step = step
		self.current = 0
		self.direction = -1

	def update(self):
        
        # when it gets to the bottom, start back at start 
		if (self.current <= self.min) :
			#self.direction = 1
			self.current = self.start  # in case it steps below min
			
		self.current += self.step * self.direction
		
		return self.current


class LFO : #uses three arguments: start point, max, and how far each step is.
	
	def __init__(self, start, max, step):
		self.start = start
		self.max = max
		self.step = step
		self.current = 0
		self.direction = 1

	def update(self):
        
        # when it gets to the top, flip direction
		if self.current > self.max - self.step :
			self.direction = -1
			self.current = self.max  # in case it steps above max
        
        # when it gets to the bottom, flip direction
		if (self.current <= self.start) :
			self.direction = 1
			self.current = self.start  # in case it steps below min
			
		self.current += self.step * self.direction
		
		return self.current


scalar = LFOhalf(1.0, 0.07, 0.01)
bounce3 = LFO(0,720,2)
trig = 0
rlfo= LFO(0,255, 1)
glfo= LFO(0,255, 1)
blfo= LFO(0,255, 1)
x= 0
y= 0
x2= 0
y2= 0

top_screen = pygame.Surface((1280,720))
bottom_screen = pygame.Surface((1280,720))

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    global top_screen, bottom_screen, trig, rlfo, glfo, blfo, x, y, x2, y2, scalar, bounce3#linelfo, 
    
    scalar2=scalar.update()
    scalar.step = 0.01
    placex = int(1280 * scalar2)
    placey = int(720*scalar2)
    
    r = int(abs(rlfo.update()))
    g = int(abs(glfo.update()))
    b = int(abs(blfo.update()))
    
    rlfo.step = int(etc.knob1*15+1) # knob1 = LFO rate controlling red level
    glfo.step = int(etc.knob2*15+1) # knob2 = LFO rate controlling green level
    blfo.step = int(etc.knob3*15+1) # knob3 = LFO rate controlling blue level
   
    bounce3.step = int(etc.knob4 * 50) # LFO rate controlling bar bounce speed
    posy2 = bounce3.update()
   
    pygame.draw.line(screen, (r,g,b), [0, posy2], [1280, posy2], 10) 
    
    top_screen = screen.copy()
    bottom_screen = top_screen.copy()
    thing = pygame.transform.scale(top_screen, (placex,placey) )
    thing.set_alpha(int(20))
    bottom_screen.set_alpha(int(20))
    bottom_screen = pygame.transform.flip(bottom_screen, 1,1)
    screen.blit(bottom_screen, (0,0))
    screen.blit(thing, (  ((1280 - placex) / 2), ((720 - placey) / 2) )   )
    
    
    