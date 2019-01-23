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

grid1 = pygame.Surface((427,240))
grid2 = pygame.Surface((427,240))
grid3 = pygame.Surface((427,240))
grid4 = pygame.Surface((427,240))

x1_nudge=0
y1_nudge=0
x2_nudge=0
y2_nudge=0
x3_nudge=0
y3_nudge=0
x4_nudge=0
y4_nudge=0

def setup(screen, etc) :
    global images, image_index

    for filepath in sorted(glob.glob(etc.mode_root + '/Images/*.png')): 
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        img = img.convert_alpha()
        images.append(img)


def draw(screen, etc) :
    global trigger, images, image_index1, image_index2, image_index3, image_index4, x1_nudge, y1_nudge, x2_nudge, y2_nudge, x3_nudge, y3_nudge, x4_nudge, y4_nudge
      
    image = images[image_index1] #define image source; only 2 images
    
    scale_x= int(etc.knob3 * 426 + 1) #x scale image on knob3; maximum size = 427 px
    scale_y=int(etc.knob3 * 239 + 1) #y scale image on knob3; maximum size = 240 px
    
    x = 640-(scale_x/2) #define x,y for image placement
    y = 360-(scale_y/2)
 
    x1_speed = (80*etc.knob1)-40 #set image0 horizontal speed on knob1
    y1_speed = (80*etc.knob2)-40 #set image0 vertical speed on knob2
    x2_speed = (80*etc.knob2)-40 #set image1 horizontal speed on knob2
    y2_speed = (80*etc.knob1)-40 #set image1 vertical speed on knob1
    
    x1 = x+x1_nudge
    y1 = y+y1_nudge
    x2 = x+x2_nudge*2
    y2 = y+y2_nudge*2
    
    if etc.audio_trig or etc.midi_note_new : #move images on trigger
        trigger = True
    if trigger == True :
        x1_nudge = (x1_nudge + x1_speed)
        y1_nudge = (y1_nudge + y1_speed)
        x2_nudge = (x2_nudge + x2_speed)
        y2_nudge = (y2_nudge + y2_speed)
        
    trigger = False
    
    #bring images back onto the screen once they march off:
    image = images[1]
    grid1 = pygame.transform.scale(image, (scale_x,scale_y))
    grid1.fill((255,255,255, etc.knob4*255), None, pygame.BLEND_RGBA_MULT) #set transparency on knob4
    if x1 > 1280 : x1_nudge = -scale_x-x
    if x1 < -scale_x : x1_nudge = 1280-x
    if y1 > 720 : y1_nudge = -scale_y-y
    if y1 < -scale_y : y1_nudge = 720-y
    screen.blit(grid1, (x1, y1))
    
    
    image = images[0]
    grid2 = pygame.transform.scale(image, (scale_x,scale_y))
    grid2.fill((255,255,255, etc.knob4*255), None, pygame.BLEND_RGBA_MULT) #set transparency on knob4
    if x2 > 1280 : x2_nudge = (-scale_x-x+1)/2
    if x2 < -scale_x : x2_nudge = (1280-x)/2
    if y2 > 720 : y2_nudge = (-scale_y-y)/2
    if y2 < -scale_y : y2_nudge= (720-y)/2
    screen.blit(grid2, (x2, y2))