import os
import pygame
import time
import random
import math

note_down = False
# knob 1 = x origin point LFO rate ; knob 2 = line width ; knob3 = endpoint LFO rate ; knob4 = color

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

sqmover = LFO(-360,360,10)
adjust1 = LFO(-50,50,10)
adjust2 = LFO(-100,100,10)

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    
    for i in range(0, 100) :
        width = int(etc.knob2*60+1)
        #LFOs
        adjuster1 = adjust1.update()
        adjust1.step = 1-etc.knob1
        adjuster2 = adjust2.update()
        adjust2.step = abs(1/(etc.knob1+.001))
        if etc.knob1 == 0 : adjuster1 = adjuster2 = 0
        if etc.knob1 == 1 : adjuster2 = adjuster1 = 0
        if .51 > etc.knob1 > .49 : adjuster2 = adjuster1 = 0
        sqmover.step = etc.knob3*2
        angle = sqmover.update()
        if etc.knob3 == 0 : angle = 0
        
        #color
        color = etc.color_picker()
        if .9 <= etc.knob4 :
            color = (int(127 + 127 * math.sin((i*1) * .1 + time.time())),
                    int(127 + 127 * math.sin((i*1) * .05+ time.time())),
                    int(127 + 127 * math.sin((i*1) * .01 + time.time())))
        if .1 >= etc.knob4 :
            color = (int(127 + 127 * math.sin((i*3) * .1 + time.time())),
                    int(127 + 127 * math.sin((i*3) * .1+ time.time())),
                    int(127 + 127 * math.sin((i*3) * .1 + time.time())))
        
        #lines
        if  i < 25:  
            x0 = 490  + adjuster1*i
            x1 = x0 - int(etc.audio_in[i] / 60)
            y = 210 + i * 12 + adjuster2
            pygame.draw.line(screen, color, [x0, y], [x1, y - angle], width)
    
        if i >= 25 and i < 50:
            x = 190 + i * 12 + adjuster2
            y0 = 510 + adjuster1*i
            y1 = y0 + int(etc.audio_in[i] / 80)
            pygame.draw.line(screen, color, [x, y0], [x + angle, y1], width)        
                
        if i >= 50 and i < 75:
            x0 = 790 + adjuster1*i
            x1 = x0 + int(etc.audio_in[i] / 60)
            y = 1110 - i * 12 + adjuster2
            pygame.draw.line(screen, color, [x0, y], [x1, y + angle], width)
                        
        if i >= 75 and i < 100:
            x = 1690 - i * 12 + adjuster2
            y0 = 210 + adjuster1*i
            y1 = y0 - abs(etc.audio_in[i] / 80)
            pygame.draw.line(screen, color, [x, y0], [x - angle, y1], width)
        
        if i == 1:
            x = 490 + adjuster2
            y0 = 210 + adjuster1*i
            y1 = y0 - int(etc.audio_in[i] / 80)
            pygame.draw.line(screen, color, [x, y0], [x - angle, y1], width)

    
    