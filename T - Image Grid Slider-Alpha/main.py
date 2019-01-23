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


def setup(screen, etc) :
    global images, image_index

    for filepath in sorted(glob.glob(etc.mode_root + '/Images/*.png')): 
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        images.append(img)


def draw(screen, etc) :
    global trigger, images, image_index1, image_index2, image_index3, image_index4
    
    image = images[image_index1]
    
    grid1 = pygame.transform.scale(image, (640,360))
    grid2 = pygame.transform.scale(image, (640,360))
    grid3 = pygame.transform.scale(image, (640,360))
    grid4 = pygame.transform.scale(image, (640,360))
    
    scale_x=int(etc.knob1 * 310 + 10)
    scale_y=int(etc.knob1 * 170 + 10)
    offset_x = int(etc.knob3 * 320 * etc.knob1)
    offset_y = int(offset_x * 0.5625)
    slide_x = int(1.5*etc.knob2*(scale_x))
    slide_y = int(1.5*etc.knob2*(scale_y))
    
    
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
    grid1.fill((255, 255, 255, etc.knob4 * 255), None, pygame.BLEND_RGBA_MULT)# alpha level
    screen.blit(grid1, (640-scale_x+slide_x-offset_x, 360-scale_y-offset_y))
    
    image = images[image_index2]
    grid2 = pygame.transform.scale(image, (scale_x,scale_y))
    grid2.fill((255, 255, 255, etc.knob4 * 255), None, pygame.BLEND_RGBA_MULT)# alpha level
    screen.blit(grid2, (640+offset_x, 360-scale_y+slide_y-offset_y))
    
    image = images[image_index3]
    grid3 = pygame.transform.scale(image, (scale_x,scale_y))
    grid3.fill((255, 255, 255, etc.knob4 * 255), None, pygame.BLEND_RGBA_MULT)# alpha level
    screen.blit(grid3, (640-slide_x+offset_x, 360+offset_y))
    
    image = images[image_index4]
    grid4 = pygame.transform.scale(image, (scale_x,scale_y))
    grid4.fill((255, 255, 255, etc.knob4 * 255), None, pygame.BLEND_RGBA_MULT)# alpha level
    screen.blit(grid4, (640-scale_x-offset_x, 360-slide_y+offset_y))
