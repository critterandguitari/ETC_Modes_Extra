import os
import pygame
import random
import glob

images = []
image_index = 0
photo = pygame.Surface((1280,720))
counter = 0
trigger = False

x = 0
y = 0
height = 720
width = 1280
linelength = 50
lineAmt = 20
displace = 10
xpos = [random.randrange(-200,1280) for i in range(0, lineAmt + 2)]
xpos1 = [(xpos[i]+displace) for i in range(0, lineAmt + 2)]


def setup(screen, etc):
    global images, image_index

    image_index = 0
    
    for filepath in sorted(glob.glob(etc.mode_root + '/Images/*.png')): 
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        img = img.convert_alpha()
        images.append(img)

def draw(screen, etc):
    global trigger, x, y, height, width, xpos, lineAmt, xpos1, linelength, displace, images, image_index, counter
    
    
    #knob1 = bit count   
    #knob2 = bits length
    #knob3 = shadow color
    #knob4 = bits color
    
    
    maxcount = int(etc.knob3 * 23 + 1)
    
    image = images[image_index]
    
    photo = pygame.transform.scale(image, (1280, 720))
    #photo.set_alpha(int(etc.knob1 * 255)) # alpha level
    screen.blit(photo, (0,0)) # (0,0) = starts at top left 
    
    
    
    displace = 10
    linewidth = (height / lineAmt)
    linelength = int(etc.knob2*300+1)
    color = etc.color_picker()
    shadowColor = (etc.bg_color[0], etc.bg_color[1], etc.bg_color[2])
    
    
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
        
    if trigger == True :
        counter += 1
        lineAmt = int(etc.knob1*100 + 2)
        xpos = [random.randrange(-200,1280) for i in range(0, lineAmt + 2)]
        xpos1 = [(xpos[i]+displace) for i in range(0, lineAmt + 2)]
    
    for k in range(0, lineAmt + 2) :
        x = xpos1[k] + linelength
        y = (k * linewidth) + int(linewidth/2)- 1
        pygame.draw.line(screen, shadowColor, (xpos1[k], y+displace), (x, y+displace), linewidth)
    
    for j in range(0, lineAmt + 2) :
        x = xpos[j] + linelength
        y = (j * linewidth) + int(linewidth/2)- 1
        pygame.draw.line(screen, color, (xpos[j], y), (x, y), linewidth)        
    trigger = False  
    
    if counter >= maxcount :
        image_index+=1
        counter = 0
    if image_index == len(images) : image_index = 0
    
    
    
    
        
    
