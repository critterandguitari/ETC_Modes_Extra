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

grid1 = pygame.Surface((1280,720))
grid2 = pygame.Surface((1280,720))
grid3 = pygame.Surface((1280,720))
grid4 = pygame.Surface((1280,720))

trot=0

def setup(screen, etc) :
    global images, image_index

    for filepath in sorted(glob.glob(etc.mode_root + '/Images/*.png')): #get images
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        img = img.convert_alpha()
        images.append(img)


def draw(screen, etc) :
    global trigger, images, image_index1, image_index2, image_index3, image_index4, trot
      
    image = images[image_index1] #define images
    
    scale_x=int(etc.knob1 * 319 + 9) #scale on knob1; max size = 328 x 184 px
    scale_y=int(etc.knob1 * 179 + 5)
    offset_x = int(etc.knob2 * 640) #offset images from center on knob2
    offset_y = int(offset_x * 0.5625)
    slide_x = int(etc.knob1*320)
    slide_y = int(etc.knob1*180)
    speed = (10*etc.knob3)-5 #set rotation speed on knob3
    
    #rotate images on audio trigger
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
    if trigger == True :
        trot = (trot + speed)
        
    trigger = False
    
    image = images[0]
    grid1 = pygame.transform.scale(image, (scale_x,scale_y))
    grid1.fill((255,255,255, etc.knob4*255), None, pygame.BLEND_RGBA_MULT) #transparency on knob4
    grid1rot = pygame.transform.rotate(grid1, trot)
    screen.blit(grid1rot, (640-(scale_x/2)+slide_x-offset_x, 360-(scale_y)-offset_y))
    
    image = images[1]
    grid2 = pygame.transform.scale(image, (scale_x,scale_y))
    grid2.fill((255,255,255, etc.knob4*255), None, pygame.BLEND_RGBA_MULT) #transparency on knob4
    grid2rot = pygame.transform.rotate(grid2, trot*2)
    screen.blit(grid2rot, (640-(scale_x/2)+offset_x, 360-(scale_y)+slide_y-offset_y))
    
    image = images[2]
    grid3 = pygame.transform.scale(image, (scale_x,scale_y))
    grid3.fill((255,255,255, etc.knob4*255), None, pygame.BLEND_RGBA_MULT) #transparency on knob4
    grid3rot = pygame.transform.rotate(grid3, trot*3)
    screen.blit(grid3rot, (640-(scale_x/2)-slide_x+offset_x, 360-(scale_y)+offset_y))
    
    image = images[3]
    grid4 = pygame.transform.scale(image, (scale_x,scale_y))
    grid4.fill((255,255,255, etc.knob4*255), None, pygame.BLEND_RGBA_MULT) #transparency on knob4
    grid4rot = pygame.transform.rotate(grid4, trot*4)
    screen.blit(grid4rot, (640-(scale_x/2)-offset_x, 360-(scale_y)-slide_y+offset_y))


