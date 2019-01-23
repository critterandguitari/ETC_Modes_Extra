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

xmover = LFO(-128000,256000,1)
ymover = LFO(-72000,144000,1)



def setup(screen, etc):
    global images
    #for filepath in sorted(glob.glob('../patches/scope-image/*.png')):
    for filepath in sorted(glob.glob('../*.png')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath).convert()
        images.append(img)

def draw(screen, etc):
    global last_point, owen, image_index

    for i in range(0, 100) :
        seg(screen, etc, i)   

def seg(screen, etc, i):
    global last_point, images, owen
    xoffset = 40
    y0 = screen.get_height() // 2#random.randrange(0,1920)
    y1 = (screen.get_height() // 2) + (etc.audio_in[i] / 90)#random.randrange(0,1920)
    x = i * 12#random.randrange(0,1080)
    color = etc.color_picker() #on knob4
    
    xmover.step = int(etc.knob1*127)+1
    ymover.step = int(etc.knob2*71)+1
    xpos = xmover.update()/100
    ypos = ymover.update()/100

    last_point = [(int(0+xpos)), (int(0+ypos))]
    pygame.draw.circle(screen,color,(x + xoffset, y1),int(etc.knob3 * 20) + 4, 0)
    pygame.draw.line(screen, color, last_point, [x + xoffset, y1], int(etc.knob3 * 20))


