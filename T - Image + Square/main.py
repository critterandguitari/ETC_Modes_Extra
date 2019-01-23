import os
import pygame
import time
import random
import glob

# IN THIS MODE, THE SQUARE CAN GET SMALLER THAN THE IMAGE, SQUARE IS ALWAYS PROPORTIONAL TO IMAGE ASPECT RATIO

images = []
image_index = 0

image_x=100
image_y=100
image_size_x=100
image_size_y=100

border_x = 1
border_y = 1
square_start_x = 1
square_start_y = 1
square_end_x = 1
square_end_y = 1

square_size = 50
    
trigger = False

def setup(screen, etc):
    global images, image_index
    for filepath in sorted(glob.glob(etc.mode_root + '/Images/*.png')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        images.append(img)


def draw(screen, etc):
    global trigger, image_x, image_y, image_size_x, image_size_y, images, image_index, square_size, border_x, border_y, square_start_x, square_start_y, square_end_x, square_end_y

    color = etc.color_picker()

    if etc.audio_trig or etc.midi_note_new :
        trigger = True
    
    if trigger == True : 
        image_x=(random.randrange(-50,1080))
        image_y=(random.randrange(-50,600))
        image_index += 1
        if image_index == len(images) : image_index = 0
    
    image = images[image_index]
        
    image_size_x=int(image.get_width() * etc.knob1)
    image_size_y=int(image.get_height() * etc.knob1)
    
    image = pygame.transform.scale(image,(image_size_x, image_size_y))
    
    border_x = int(etc.knob2 * image.get_width()) - (image.get_width() / 2) 
    border_y = int(etc.knob2 * image.get_height()) - (image.get_height() / 2) 
    square_start_x = image_x - border_x
    square_start_y = image_y - border_y
    square_end_x = image_size_x + (border_x*2)
    square_end_y = image_size_y + (border_y*2)
    
    pygame.draw.rect(screen, color, (square_start_x, square_start_y, square_end_x, square_end_y), 0)
    
    image.fill((255, 255, 255, etc.knob3 * 255), None, pygame.BLEND_RGBA_MULT)

    screen.blit(image, (image_x,image_y))
    
    trigger = False

