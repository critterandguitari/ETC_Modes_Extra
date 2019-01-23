import os
import pygame

y = 0
x = 0
count = 0

def setup(screen, etc):
    pass

def draw(screen, etc):
    global y, x, count

    R = 1 
    peak = 0
    
    for i in range(0,100) :
        if etc.audio_in[i] > peak:
            peak = etc.audio_in[i]
    R = (peak / 200) + 5
    
    if etc.audio_trig or etc.midi_note_new :
        y = 4 * R
        
    color = etc.color_picker()
    pygame.draw.circle(screen,color,(x,y),(int(R)+10))
   
    y = y-int(etc.knob2 * 100 + 1)
    if y <= 0 + R : y = 0 + R
    
    speed = int(etc.knob1 * 120) - 60
    x = x + speed
    if x >= 1280 + R : x = 0-R
    if (0-R) > x : x = 1280 + R
    
#TRAILS
    veil = pygame.Surface((1280,720))  
    veil.set_alpha(int(etc.knob3 * 200)) # adjust transparency on knob3
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0,0)) # (0,0) = starts at top left 