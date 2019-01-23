import os
import pygame
import time
import random
import glob

last_point = [0, 360]
images = []
image_index = 0

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
mover = LFO(1,720,1)
imagesizer = LFO(1,100,1)

def setup(screen, etc):
    global images
    for filepath in sorted(glob.glob(etc.mode_root + '/Images/*.png')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath).convert_alpha()
        images.append(img)

def draw(screen, etc):
    global last_point
    
    #knob1 = image size     
    #knob2 = LFO rate
    #knob3 = circle size and fill
    #knob4 = circle color

    for i in range(0, 100) :
        seg(screen, etc, i)   
    
def seg(screen, etc, i):
    global last_point, images
    xoffset = 0
    mover.step = etc.knob2*50
    y1 = int(mover.update()) + (etc.audio_in[i] / 35)
    x = i * 13
    color = etc.color_picker()

    max_circle = 120
    image_size = 1
    circle_size = 0
    line_width = 0
    if etc.knob3 <=.5 :
        circle_size = int(etc.knob3 * max_circle)
        line_width = 0
    if etc.knob3 >.501 :
        circle_size = abs(max_circle-int(etc.knob3 * max_circle)) 
        line_width =  abs(30-int(etc.knob3 * 30))

    pygame.draw.circle(screen,color,(x + xoffset, y1),circle_size, line_width)

    image = images[0]
    image = pygame.transform.scale(image, (int(image.get_width() * etc.knob1)/4, int(image.get_height() * etc.knob1)/4) )
    screen.blit(image, (x + xoffset, y1))
