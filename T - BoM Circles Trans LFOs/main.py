import os
import pygame
import glob
import random


class LFOhalf : #uses three arguments: start point, min, and how far each step is.
	
	def __init__(self, start, min, step):
		self.start = start
		self.min = min
		self.step = step
		self.current = 0
		self.direction = -1

	def update(self):
        
        # when it gets to the bottom, start back at start 
		if (self.current <= self.min + self.step) :
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
		if (self.current >= self.max) :
			self.direction = -1
			self.current = self.max  # in case it steps above max
        
        # when it gets to the bottom, flip direction
		if (self.current <= self.start) :
			self.direction = 1
			self.current = self.start  # in case it steps below min
			
		self.current += self.step * self.direction
		
		return self.current
		
circlfo = LFO(4,200,10)
scalar = LFOhalf(1.0, 0.07, 0.01)

top_screen = pygame.Surface((1280,720))
bottom_screen = pygame.Surface((1280,720))

trig = 0
r = 0
g= 0
b= 0
x= 370
y= 650

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    global top_screen, bottom_screen, trig, r, g, b, x, y, scalar, linelfo
    

    scalar2=scalar.update()
    scalar.step = etc.knob2/2 # trails screen size change rate
    placex = int(1280 * scalar2)
    placey = int(720*scalar2)
    
    circ = int(abs(circlfo.update()))
    circlfo.step = etc.knob1*20 # circle size change rate
    
    if etc.audio_trig or etc.midi_note_new : trig = 1
    
    if trig == 1 :
        if etc.knob4 < .5 :
            r=g=b= int(etc.knob4*509+1) # grayscale selector for 1st half of knob4
        
        if etc.knob4 >= .5 :
            r = random.randrange(10,int(244*etc.knob4+11)) # random color selector for 2nd half of knob4
            g = random.randrange(10,int(244*etc.knob4+11))
            b = random.randrange(10,int(244*etc.knob4+11))
        
        x = random.randrange(-10,1290)
        y = random.randrange(-10,730)
        trig = 0 
       
    pygame.draw.circle(screen,(r,g,b),[x,y],circ)
    
    
    top_screen = screen.copy()
    bottom_screen = top_screen.copy()
    thing = pygame.transform.scale(top_screen, (abs(placex),abs(placey)) )
    thing.set_alpha(int(etc.knob3 * 200)) # adjust transparency on knob3
    bottom_screen.set_alpha(int(etc.knob3 * 200)) # adjust transparency on knob3
    bottom_screen = pygame.transform.flip(bottom_screen, 1,1)
    screen.blit(bottom_screen, (0,0))
    screen.blit(thing, (  ((1280 - placex) / 2), ((720 - placey) / 2) )   )