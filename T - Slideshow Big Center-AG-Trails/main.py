import os
import pygame
import glob

images = []
image_index = 0

bgi = pygame.Surface((1280, 720))
bgi2 = pygame.Surface((1280, 720))
last_screen = pygame.Surface((1280,720))



def setup(screen, etc) :
    global images, fall, bg

    for filepath in sorted(glob.glob(etc.mode_root + 'Images/*.png')): 
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        img = img.convert_alpha()
        images.append(img)



def draw(screen, etc) :
    global images, image_index, last_screen, nest, bgi, bgi2
    
    above = False
    
    if etc.audio_trig or etc.midi_note_new :
        above = True
  
    if above:
        
        image_index += 1
        if image_index == len(images) : image_index = 0
        image = images[image_index]
        
        
        bgi = pygame.transform.scale(image, (1280, 720))        
        bgi2 = pygame.transform.scale(last_screen, (int(etc.knob4 * 1280), int(etc.knob4 * 720) ) ) #scales .png image
        screen.blit(bgi, (0, 0))
        screen.blit(bgi2, (int(etc.knob1 * 1280), int(etc.knob2 * 720)))
        last_screen = screen.copy()
    
    #print background color layer over entire image
    veil = pygame.Surface((1280,720))  
    veil.set_alpha(int(etc.knob3 * 200 + 1)) # adjust transparency on knob3
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0,0)) # (0,0) = starts at top left