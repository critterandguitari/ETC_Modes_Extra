import os
import pygame
import time
import random
import math

lines = 20 
width = 720 / lines
offset = width / 2
xpos = 0

def setup(screen, etc):
    pass

def draw(screen, etc):
    global lines, offset, width, xpos
    
    # star distance on knob1
    # line width on knob2
    veiltrans = etc.knob3 # adjust transparency on knob3
    sel = etc.knob4*5 # select color range on knob4
    
    if 0<= sel <1 :
        for i in range(0, lines) :
        
            color2 =    (int(127 + 127 * math.sin((i*6) * .1 + time.time())),
                        int(127 + 127 * math.sin((i*6) * .05+ time.time())),
                        int(127 + 127 * math.sin((i*6) * .01 + time.time())))
        
            color1 =    (int(127 + 127 * math.cos((i*6) * .1 + time.time())),
                        int(127 + 127 * math.cos((i*6) * .05 + time.time())),
                        int(127 + 127 * math.cos((i*6) * .01 + time.time())))
        
            xpos = int(640 * math.sin(i * 1 + time.time()))
            xpos1 = int(640*(etc.knob1) * math.sin(10 * .2 + time.time()))
            ypos1 = int(300*(etc.knob1) * math.sin(10 * .1 + time.time()))
            ypos2 = int(300*(etc.knob1) * math.sin(10 * .1 + time.time()))*(etc.audio_in[i]/1000+1)
            bounce1 = int(etc.audio_in[49]/500)
            bounce2 = int(etc.audio_in[50]/500)
            thick = int(etc.knob2*19)+1
            pygame.draw.line(screen, color1, [1280/2-xpos1, 360-bounce1+ypos1], [1280/2-xpos-xpos1, (offset + (i * width)+ypos2)], thick)
            pygame.draw.line(screen, color2, [640+xpos1, 360-bounce2-ypos1], [640-xpos+xpos1, (offset + (i * width)-ypos2)], thick)

    if 1<= sel <2 :
        for i in range(0, lines) :
        
            color2 =    (int(127 + 127 * math.sin((i*6) * .01 + time.time())),
                        0,
                        0)
        
            color1 =    (0,
                        0,
                        int(127 + 127 * math.cos((i*6) * .01 + time.time())))
        
            xpos = int(640 * math.sin(i * 1 + time.time()))
            xpos1 = int(640*(etc.knob1) * math.sin(10 * .2 + time.time()))
            ypos1 = int(300*(etc.knob1) * math.sin(10 * .1 + time.time()))
            ypos2 = int(300*(etc.knob1) * math.sin(10 * .1 + time.time()))*(etc.audio_in[i]/1000+1)
            bounce1 = int(etc.audio_in[49]/500)
            bounce2 = int(etc.audio_in[50]/500)
            thick = int(etc.knob2*19)+1
            pygame.draw.line(screen, color1, [1280/2-xpos1, 360-bounce1+ypos1], [1280/2-xpos-xpos1, (offset + (i * width)+ypos2)], thick)
            pygame.draw.line(screen, color2, [640+xpos1, 360-bounce2-ypos1], [640-xpos+xpos1, (offset + (i * width)-ypos2)], thick)
        
    if 2<= sel <3 :
        for i in range(0, lines) :
        
            color2 =    (int(127 + 127 * math.sin((i*6) * .01 + time.time())),
                        255,
                        int(127 + 127 * math.sin((i*6) * .01 + time.time())))
        
            color1 =    (255,
                        abs(127+127 * math.cos((i*6) * .01 + time.time())),
                        abs(127+127 * math.cos((i*6) * .01 + time.time())))
        
            xpos = int(640 * math.sin(i * 1 + time.time()))
            xpos1 = int(640*(etc.knob1) * math.sin(10 * .2 + time.time()))
            ypos1 = int(300*(etc.knob1) * math.sin(10 * .1 + time.time()))
            ypos2 = int(300*(etc.knob1) * math.sin(10 * .1 + time.time()))*(etc.audio_in[i]/1000+1)
            bounce1 = int(etc.audio_in[49]/500)
            bounce2 = int(etc.audio_in[50]/500)
            thick = int(etc.knob2*19)+1
            pygame.draw.line(screen, color1, [1280/2-xpos1, 360-bounce1+ypos1], [1280/2-xpos-xpos1, (offset + (i * width)+ypos2)], thick)
            pygame.draw.line(screen, color2, [640+xpos1, 360-bounce2-ypos1], [640-xpos+xpos1, (offset + (i * width)-ypos2)], thick)

    if 3<= sel <4 :
        for i in range(0, lines) :
        
            color2 =    (225,
                        int(127+127 * math.cos((i*6) * .01 + time.time())),
                        255)
        
            color1 =    (255,
                        225,
                        int(127 + 127 * math.cos((i*6) * .01 + time.time())))
        
            xpos = int(640 * math.sin(i * 1 + time.time()))
            xpos1 = int(640*(etc.knob1) * math.sin(10 * .2 + time.time()))
            ypos1 = int(300*(etc.knob1) * math.sin(10 * .1 + time.time()))
            ypos2 = int(300*(etc.knob1) * math.sin(10 * .1 + time.time()))*(etc.audio_in[i]/1000+1)
            bounce1 = int(etc.audio_in[49]/500)
            bounce2 = int(etc.audio_in[50]/500)
            thick = int(etc.knob2*19)+1
            pygame.draw.line(screen, color1, [1280/2-xpos1, 360-bounce1+ypos1], [1280/2-xpos-xpos1, (offset + (i * width)+ypos2)], thick)
            pygame.draw.line(screen, color2, [640+xpos1, 360-bounce2-ypos1], [640-xpos+xpos1, (offset + (i * width)-ypos2)], thick)

    if 4<= sel :
        for i in range(0, lines) :
        
            color2 =    (int(127 + 127 * math.sin((i*6) * .01 + time.time())),
                        int(127 + 127 * math.sin((i*6) * .01+ time.time())),
                        int(127 + 127 * math.sin((i*6) * .01 + time.time())))
        
            color1 =    (int(127 + 127 * math.cos((i*6) * .01 + time.time())),
                        int(127 + 127 * math.cos((i*6) * .01 + time.time())),
                        int(127 + 127 * math.cos((i*6) * .01 + time.time())))
        
            xpos = int(640 * math.sin(i * 1 + time.time()))
            xpos1 = int(640*(etc.knob1) * math.sin(10 * .2 + time.time()))
            ypos1 = int(300*(etc.knob1) * math.sin(10 * .1 + time.time()))
            ypos2 = int(300*(etc.knob1) * math.sin(10 * .1 + time.time()))*(etc.audio_in[i]/1000+1)
            bounce1 = int(etc.audio_in[49]/500)
            bounce2 = int(etc.audio_in[50]/500)
            thick = int(etc.knob2*19)+1
            pygame.draw.line(screen, color1, [1280/2-xpos1, 360-bounce1+ypos1], [1280/2-xpos-xpos1, (offset + (i * width)+ypos2)], thick)
            pygame.draw.line(screen, color2, [640+xpos1, 360-bounce2-ypos1], [640-xpos+xpos1, (offset + (i * width)-ypos2)], thick)

#TRAILS
    veil = pygame.Surface((1280,720))  
    veil.set_alpha(int(veiltrans * 200)) 
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0,0)) # (0,0) = starts at top left 
