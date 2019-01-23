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
width = 1340
linelength = 50
lineAmt = 20
displace = 10
ypos = [random.randrange(-200,720) for i in range(0, lineAmt + 2)]
ypos1 = [(ypos[i]+displace) for i in range(0, lineAmt + 2)]


def setup(screen, etc):
    global images, image_index

    image_index = 0
    
    for filepath in sorted(glob.glob(etc.mode_root + '/Images/*.png')): 
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        img = img.convert()
        images.append(img)

def draw(screen, etc):
    global trigger, x, y, height, width, ypos, lineAmt, ypos1, linelength, displace, images, image_index, counter
    
    #knob 1 number of bits
    #knob 2 bits length
    #knob 3 maxcount
    #knob 4 color
    
    
    maxcount = int(etc.knob3 * 23 + 1)
    
    image = images[image_index]
    
    photo = pygame.transform.scale(image, (1280, 720))
    #photo.set_alpha(int(etc.knob1 * 255)) # alpha level
    screen.blit(photo, (0,0)) # (0,0) = starts at top left 
    
    displace = 10
    linewidth = (width / lineAmt)
    linelength = int(etc.knob2*300+1)
    color = etc.color_picker()
    #minus = (etc.knob3*0.5)+0.5
    #shadowColor = (etc.bg_color[0]*minus, etc.bg_color[1]*minus, etc.bg_color[2]*minus)
    shadowColor = (etc.bg_color[0], etc.bg_color[1], etc.bg_color[2])
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
        
    if trigger == True :
        counter += 1
        lineAmt = int(etc.knob1*100 + 2)
        ypos = [random.randrange(-200,720) for i in range(0, lineAmt + 2)]
        ypos1 = [(ypos[i]+displace) for i in range(0, lineAmt + 2)]
    
    for k in range(0, lineAmt + 2) :
        
        y = ypos1[k] + linelength
        x = (k * linewidth) + int(linewidth/2)- 1
        pygame.draw.line(screen, shadowColor, (x+displace, ypos1[k]), (x+displace, y), linewidth)
    
    for j in range(0, lineAmt + 2) :
       
        y = ypos[j] + linelength
        x = (j * linewidth) + int(linewidth/2)- 1
        pygame.draw.line(screen, color, (x, ypos[j]), (x, y), linewidth)        
    
    trigger = False  
    
    
    if counter >= maxcount :
        image_index+=1
        counter = 0
    if image_index == len(images) : image_index = 0
    
        
    
