import os
import pygame
import time
import random
import glob

images = []
image_index = 0
image_x=100
image_y=100
image_size_x=100
image_size_y=100
circle_x=100
circle_y=100
circle_size = 50
trigger = False

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
sizer = LFO(2,100,1)		


def setup(screen, etc):
    pass
    global images, image_index
    for filepath in sorted(glob.glob(etc.mode_root + '/Images/*.png')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        images.append(img)

def draw(screen, etc):
    global trigger, image_x, image_y, circle_x, circle_y, circle_size, image_size_x, image_size_y, images, image_index

    color = etc.color_picker()

    if etc.audio_trig or etc.midi_note_new :
        trigger = True
    
    if trigger == True : 
        image_x=(random.randrange(-50,1080))
        image_y=(random.randrange(-50,600))
        image_index += 1
        if image_index == len(images) : image_index = 0
    
    image = images[image_index]
        
    imagesizer = sizer.update()
    sizer.step = etc.knob1 * 25
    image_size_x=int(image.get_width() * imagesizer/100)
    image_size_y=int(image.get_height() * imagesizer/100)
    
    image = pygame.transform.scale(image,(abs(image_size_x), abs(image_size_y)))
        
    circle_size = abs(int(etc.knob2*image_size_x/1.5)) #you can change this number if you want max. circle size to be bigger or smaller
    pygame.draw.circle(screen,color,[image_x+(int(image.get_width()/2)),image_y+(int(image.get_height()/2))],circle_size, 0)
    
    image.fill((255, 255, 255, etc.knob3 * 255), None, pygame.BLEND_RGBA_MULT)

    screen.blit(image, (image_x,image_y))
    
    trigger = False

