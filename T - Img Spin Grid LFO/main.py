import os
import pygame
import glob
import math
import random

images = []

image_index1 = 0
image_index2 = 0
image_index3 = 0
image_index4 = 0

trigger = False

grid1 = pygame.Surface((640, 360))
grid2 = pygame.Surface((640, 360))
grid3 = pygame.Surface((640, 360))
grid4 = pygame.Surface((640, 360))

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
spinner = LFO(1,360,1)

def setup(screen, etc) :
    global images, image_index

    for filepath in sorted(glob.glob(etc.mode_root + '/Images/*.png')): 
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        img = img.convert_alpha()
        images.append(img)


def draw(screen, etc) :
    global trigger, images, image_index1, image_index2, image_index3, image_index4
      
    image = images[image_index1]
    
    grid1 = pygame.transform.scale(image, (640,360))
    grid2 = pygame.transform.scale(image, (640,360))
    grid3 = pygame.transform.scale(image, (640,360))
    grid4 = pygame.transform.scale(image, (640,360))
    
    scale_x=int(etc.knob1 * 359 + 1)
    scale_y=int(etc.knob1 * 239 + 1)
    offset_x = int(etc.knob3 * 480 * etc.knob1)
    offset_y = int(offset_x * 0.5625)
    slide_x = int(etc.knob2*scale_x)
    slide_y = int(etc.knob2*scale_y)
    
    spinner.step = int(etc.knob4 * 60)
    rot =  spinner.update()
   
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
    if trigger == True :
        trigger = False
        
        image_index1 = random.randrange(0,len(images)) 
        image_index2 = random.randrange(0,len(images)) 
        image_index3 = random.randrange(0,len(images))  
        image_index4 = random.randrange(0,len(images)) 

    
    image = images[image_index1]
    grid1 = pygame.transform.scale(image, (scale_x,scale_y))
    grid1rot = pygame.transform.rotate(grid1, rot)
    screen.blit(grid1rot, (640-scale_x+slide_x-offset_x, 360-scale_y-offset_y))
    
    image = images[image_index2]
    grid2 = pygame.transform.scale(image, (scale_x,scale_y))
    grid2rot = pygame.transform.rotate(grid2, -rot)
    screen.blit(grid2rot, (640+offset_x, 360-scale_y+slide_y-offset_y))
    
    image = images[image_index3]
    grid3 = pygame.transform.scale(image, (scale_x,scale_y))
    grid3rot = pygame.transform.rotate(grid3, rot)
    screen.blit(grid3rot, (640-slide_x+offset_x, 360+offset_y))
    
    image = images[image_index4]
    grid4 = pygame.transform.scale(image, (scale_x,scale_y))
    grid4rot = pygame.transform.rotate(grid4, -rot)
    screen.blit(grid4rot, (640-scale_x-offset_x, 360-slide_y+offset_y))

