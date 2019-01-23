import os
import pygame
import glob
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
        img = img.convert_alpha()
        images.append(img)

def draw(screen, etc) :
    global trigger, images, image_index1, image_index2, image_index3, image_index4
    
    image = images[image_index1]
    
    grid1 = pygame.transform.scale(image, (640,360))
    grid2 = pygame.transform.scale(image, (640,360))
    grid3 = pygame.transform.scale(image, (640,360))
    grid4 = pygame.transform.scale(image, (640,360))
    
    dropshadow = etc.knob4
    offset = int(etc.knob4 * 20)
    scale_x=int(etc.knob1 * 640)
    scale_y=int(etc.knob1 * 360)
    recenter_x = 320-scale_x/2
    recenter_y = 180-scale_y/2
    slide_x = int(etc.knob2*640)
    slide_y = int(etc.knob2*360)

    
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
    if (etc.knob3 < .25) :
        grid1 = pygame.transform.flip(grid1, 0,0)
    if (etc.knob3 >= .25) and (etc.knob3 < .5) :
        grid1 = pygame.transform.flip(grid1, 0,1)
    if (etc.knob3 >= .5) and (etc.knob3 < .75) :
        grid1 = pygame.transform.flip(grid1, 1,0)
    if (etc.knob3 >= .75) :
        grid1 = pygame.transform.flip(grid1, 1,1)
    pygame.draw.rect(screen, (etc.bg_color[0]*dropshadow,etc.bg_color[1]*dropshadow, etc.bg_color[2]*dropshadow), [recenter_x+offset+slide_x,recenter_y+offset,scale_x+offset,scale_y+offset], 0)
    screen.blit(grid1, (recenter_x+slide_x, recenter_y))
    
    image = images[image_index2]
    grid2 = pygame.transform.scale(image, (scale_x,scale_y))
    if (etc.knob3 < .25) :
        grid2 = pygame.transform.flip(grid2, 0,0)
    if (etc.knob3 >= .25) and (etc.knob3 < .5) :
        grid2 = pygame.transform.flip(grid2, 0,1)
    if (etc.knob3 >= .5) and (etc.knob3 < .75) :
        grid2 = pygame.transform.flip(grid2, 1,0)
    if (etc.knob3 >= .75) :
        grid2 = pygame.transform.flip(grid2, 1,1)
    pygame.draw.rect(screen, (etc.bg_color[0]*dropshadow,etc.bg_color[1]*dropshadow, etc.bg_color[2]*dropshadow), [640+recenter_x+offset,recenter_y+offset+slide_y,scale_x+offset,scale_y+offset], 0)
    screen.blit(grid2, (640+recenter_x, recenter_y+slide_y))

    image = images[image_index3]
    grid3 = pygame.transform.scale(image, (scale_x,scale_y))
    if (etc.knob3 < .25) :
        grid3 = pygame.transform.flip(grid3, 0,0)
    if (etc.knob3 >= .25) and (etc.knob3 < .5) :
        grid3 = pygame.transform.flip(grid3, 0,1)
    if (etc.knob3 >= .5) and (etc.knob3 < .75) :
        grid3 = pygame.transform.flip(grid3, 1,0)
    if (etc.knob3 >= .75) :
        grid3 = pygame.transform.flip(grid3, 1,1)
    pygame.draw.rect(screen, (etc.bg_color[0]*dropshadow,etc.bg_color[1]*dropshadow, etc.bg_color[2]*dropshadow), [recenter_x+offset,360+recenter_y+offset-slide_y,scale_x+offset,scale_y+offset], 0)
    screen.blit(grid3, (recenter_x, 360+recenter_y-slide_y))
    
    image = images[image_index4]
    grid4 = pygame.transform.scale(image, (scale_x,scale_y))
    if (etc.knob3 < .25) :
        grid4 = pygame.transform.flip(grid4, 0,0)
    if (etc.knob3 >= .25) and (etc.knob3 < .5) :
        grid4 = pygame.transform.flip(grid4, 0,1)
    if (etc.knob3 >= .5) and (etc.knob3 < .75) :
        grid4 = pygame.transform.flip(grid4, 1,0)
    if (etc.knob3 >= .75) :
        grid4 = pygame.transform.flip(grid4, 1,1)
    pygame.draw.rect(screen, (etc.bg_color[0]*dropshadow,etc.bg_color[1]*dropshadow, etc.bg_color[2]*dropshadow), [640+recenter_x+offset-slide_x,360+recenter_y+offset,scale_x+offset,scale_y+offset], 0)
    screen.blit(grid4, (640+recenter_x-slide_x, 360+recenter_y))

