import os
import pygame
import random
import glob
import pygame.gfxdraw

images = []
image_index = 0
trigger = False

num = 10
clench = 0
teeth = 1
toff = 1

last_screen = pygame.Surface((1270,710)) #pygame.Surface((1280,720))
photo = pygame.Surface((1280,720))
r=0
g=0
b=0
counter = 0

def setup(screen, etc) :
    global images, fall, bg, image_index

    image_index = 0
    
    for filepath in sorted(glob.glob(etc.mode_root + '/Images/*.png')): 
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        img = img.convert()
        images.append(img)


def draw(screen, etc) : 
    global last_screen, r, g, b, counter, images, image_index, trigger, teeth, num, clench
    
#trigger puts up photo behind sound jaws    
    image = images[image_index]
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
    if trigger == True :
        image_index += 1
    if image_index == len(images) : image_index = 0
        
    trigger = False    
    
    photo = pygame.transform.scale(image, (1280, 720))
    photo.set_alpha(int(etc.knob3* 255)) # alpha level
    screen.blit(photo, (0,0)) #starts at top left 
    
    
#CRAZY FEEDBACK
    image = last_screen
    last_screen = screen.copy()
    thing = pygame.transform.scale(image,(1270,710) )
    screen.blit(thing, (5,5)) 
    
#colorshift loop; rapid to no shift on knob4    
    if etc.knob4 < 1:
        counter+=1
        if counter > int(etc.knob4 * 75):
            r = random.randrange(0,254)
            g = random.randrange(0,254)
            b = random.randrange(0,254)
            counter = 0
    
    colorshift = 20 - int(etc.knob4 * 20)
    r= (r+colorshift)%255
    g= (g+colorshift)%255
    b= (b+colorshift)%255
    color = (r,g,b)
    
#set teeth number and shape    
    teeth = int(etc.knob1 * 10)
    teethwidth = int(1280-128*teeth)
    if teethwidth == 0 : teethwidth = 128
    shape = int(etc.knob2*3)
    clench = 100 - teethwidth/2
    if teethwidth > 640 and shape >= 1 : clench = -400
    if shape < 1 : clench = 5
    
    #top row
    for i in range(0, 10) :
        
        x = (i * teethwidth)+teethwidth/2
        y0 = 0
        y1 = y0 + abs(etc.audio_in[i] / 85) + clench
        pygame.draw.line(screen, color, [x, y0], [x, y1], teethwidth)
        if shape == 1 :
            pygame.gfxdraw.filled_trigon(screen, x-teethwidth/2, y1, x, y1+teethwidth/2, x+teethwidth/2, y1, color)
        if shape >= 2 :
            pygame.gfxdraw.filled_circle(screen, x, y1, teethwidth/2, color)    
    #bottom row
    for i in range(num, num*2) :
        x = ((i-num) * teethwidth) + teethwidth/2
        y0 = 720
        y1 = y0 - abs(etc.audio_in[i] / 85) - clench
        pygame.draw.line(screen, color, [x, y0], [x, y1], teethwidth)
        if shape == 1 :
            pygame.gfxdraw.filled_trigon(screen, x-teethwidth/2, y1, x, y1-teethwidth/2, x+teethwidth/2, y1, color)
        if shape >= 2 :
            pygame.gfxdraw.filled_circle(screen, x, y1, teethwidth/2, color)
    
    
    
    
    

    
    
  


    
    