import os
import pygame
import time
import random
import glob
import math

last_point = [0, 360]


lx = 0
ly = 0

images = []
image_index = 0

def setup(screen, etc):
    global images
    for filepath in sorted(glob.glob(etc.mode_root + '/Images/*.png')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath).convert_alpha()
        images.append(img)

def draw(screen, etc):
    global last_point
    

    for i in range(0, 100) :
        seg(screen, etc, i)   
    

def seg(screen, etc, i):
    global last_point, images, lx, ly
    
    xoffset = 0
    y1 = int(etc.knob2 * 720) + (etc.audio_in[i] / 35)
    x = i * 13
    color = etc.color_picker()

    R = etc.knob2*400-200
    R = R + (etc.audio_in[i] / 100)
    x = R * math.cos((i /  100.) * 6.28) + 640
    y = R * math.sin((i /  100.) * 6.28) + 320
    
    pygame.draw.line(screen, color, [lx, ly], [x, y], int(etc.knob3*10)+1)
    ly = y
    lx = x

    image = images[0]
    image = pygame.transform.scale(image, (int(image.get_width() * etc.knob1), int(image.get_height() * etc.knob1)) )
    screen.blit(image, (x, y))
