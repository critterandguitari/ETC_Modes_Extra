import os
import pygame
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

sqmover = LFO(-120,120,10)

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    
    for i in range(0, 7) :
        
        sqmover.step = etc.knob1*3 # slide speed
        sqmover.max = int(etc.knob2*120) # slide range
        sqmover.start = int(etc.knob2*-120)
        xoffset = sqmover.update()
        yoffset = -sqmover.update()*8/10

        for j in range(0, 10) :
            x = (j*(1280/8))-(1280/8)
            y = (i*(720/5))-(720/5)
            
            rad = abs(etc.audio_in[j-i] / 100)
            width = int(etc.knob3*99)+1 # square size
            sel = int(etc.knob4*8)
            if sel >= 7 :
                color = (int(127 + 127 * math.sin((i*7) * .1 + time.time())),
                    int(127 + 127 * math.sin((i*7) * .05+ time.time())),
                    int(127 + 127 * math.sin((i*7) * .01 + time.time())))
            if 1 <= sel < 2 :
                color = (int(127 + 127 * math.sin((i*7) * .1 + time.time())),45,72)
            if 2 <= sel < 3 :
                color = (75,int(127 + 127 * math.sin((i*7) * .1 + time.time())),42)
            if 3 <= sel < 4 :
                color = (42,75,int(127 + 127 * math.sin((i*7) * .1 + time.time())))
            if 4 <= sel < 5 :
                color = (int(127 + 127 * math.sin((i*7) * .1 + time.time())),220,0)
            if 5 <= sel < 6 :
                color = (255,int(127 + 127 * math.sin((i*7) * .1 + time.time())),0)
            if 6 <= sel < 7 :
                color = (176,175,int(127 + 127 * math.sin((i*7) * .1 + time.time())))    
            if 1 > sel :
                color = (int(127 + 127 * math.sin((i*7) * .1 + time.time())),
                        int(127 + 127 * math.sin((i*7) * .1 + time.time())),
                        int(127 + 127 * math.sin((i*7) * .1 + time.time()))) # color on knob4
            if (i%2) == 1 : 
                x = j*(1280/8)-(1280/8)+xoffset
            if (j%2) == 1 : 
                y = i*(720/5)-(720/5)+yoffset
            
            rect = pygame.Rect(0,0,width,width)
            rect.center = (x,y)
            rect.inflate_ip(rad,rad)
            
            pygame.draw.rect(screen, color, rect, 0) 

    