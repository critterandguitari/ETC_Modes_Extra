import os
import pygame
import glob

images = []
image_index = 0

fall = 0
scoot = 0

bg = pygame.Surface((656,416))


waiting = 0 


def setup(screen, etc) :
    global images, fall, bg
    #images = []
    
    bg = pygame.Surface((screen.get_width(),screen.get_height()))
    for filepath in sorted(glob.glob(etc.mode_root + '/Images/*.png')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
       # img = img.convert_aplha(img)
        images.append(img)



def draw(screen, etc) :
    global images, image_index, fall, bg, scoot, waiting
    
    above = False
    
    if waiting == 0 :
        for i in range(0, 100) :
            if abs(etc.audio_in[i]) > 1000 :
                above = True
                waiting = 4
    else :
        waiting -= 1
  
    if etc.audio_trig or etc.midi_note_new :
        image_index += 1
        if image_index == len(images) : image_index = 0
        img = images[image_index]
        img = pygame.transform.scale(img, (int(img.get_width() * etc.knob3), int(img.get_height() * etc.knob3)) )

        
        img.fill((255, 255, 255, etc.knob4 * 255), None, pygame.BLEND_RGBA_MULT)

        y = int(etc.knob2 * 720) - int(img.get_height() * .5)
        x = int(etc.knob1 * 1280) - int(img.get_width() * .5)
        screen.blit(img, (x,y))
