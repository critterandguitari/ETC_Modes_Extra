import os
import pygame
import time
import random
import glob
import math

last_point = [0, 360]
i = 0
images = []
image_index = 0
lx = 0
ly = 0

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

circlesizer = LFO(2,300,1)
imagesizer = LFO(2, 400, 1)

def setup(screen, etc):
    global images
    for filepath in sorted(glob.glob(etc.mode_root + '/Images/*.png')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath).convert_alpha()
        images.append(img)

def draw(screen, etc):
    global last_point, images, i, lx, ly
    
    #knob1 = image size LFO rate     
    #knob2 = radius
    #knob3 = circle size LFO rate
    #knob4 = circle color
    
    imagesizer.step = int(etc.knob1 * 25)
    
    xoffset = 0
    y1 = int(etc.knob2 * 720) + (etc.audio_in[i] / 35)
    x = i * 13
    color = etc.color_picker()

    R = etc.knob2*400-200
    R = R + (etc.audio_in[i] / 100)
    x = R * math.cos((i /  100.) * 6.28) + 640
    y = (R * math.sin((i /  100.) * 6.28) + 360) + int((etc.knob2-.5)*720)
    
    image_size = 1
    circle_size = 0
    line_width = 0
    circlesizer.step = int(etc.knob3*50)
    circle_size = abs(circlesizer.update()) * int(100-etc.knob3*100)/100
    line_width = 0
    
    pygame.draw.circle(screen,color,(int(x),int(y)), abs(circle_size), line_width)
    image = images[0]
    image = pygame.transform.scale(image, (abs(int(image.get_width() * imagesizer.update()/200)), abs(int(image.get_height() * imagesizer.update()/200))) )
    screen.blit(image, (x-image.get_width()/2, y-image.get_height()/2))
    
    i = (i + 1) % 100

    
