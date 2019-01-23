import os
import pygame
import glob

images = []
image_index = 0
trigger = False

bgi = pygame.Surface((1280, 720))
bgi2 = pygame.Surface((1280, 720))
last_screen = pygame.Surface((1280,720))



def setup(screen, etc) :
    global images, fall, bg, image_index

    image_index = 0
    
    for filepath in sorted(glob.glob(etc.mode_root + '/Images/*.png')): 
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        img = img.convert_alpha()
        images.append(img)



def draw(screen, etc) :
    global images, image_index, last_screen, nest, bgi, bgi2, trigger
    
    trigger = False
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
    if trigger == True :
        image_index += 1
    if image_index == len(images) : image_index = 0
    image = images[image_index]
    

    scale_x=int(etc.knob1 * 1280)
    scale_y=int(etc.knob2 * 720)
    recenter_x = 640-scale_x/2
    recenter_y = 360-scale_y/2
    
    bgi = pygame.transform.scale(image, (1280, 720))
    bgi2 = pygame.transform.scale(last_screen, (scale_x, scale_y )) #scales .png image    
    if (etc.knob4 < .25) :
        bgi2 = pygame.transform.flip(bgi2, 0,0)
    if (etc.knob4 > .25) and (etc.knob4 < .5) :
        bgi2 = pygame.transform.flip(bgi2, 0,1)
    if (etc.knob4 > .5) and (etc.knob4 < .75) :
        bgi2 = pygame.transform.flip(bgi2, 1,0)
    if (etc.knob4 > .75) :
        bgi2 = pygame.transform.flip(bgi2, 1,1)
        
    
    screen.blit(bgi2, (recenter_x, recenter_y))
    screen.blit(bgi, (0, 0))
    last_screen = screen.copy()

#print background color layer over entire image
    veil = pygame.Surface((1280,720))  
    veil.set_alpha(int(etc.knob3 * 125)) # adjust transparency on knob3
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0, 0)) # (0,0) = starts at top left
