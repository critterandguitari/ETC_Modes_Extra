import os
import pygame

last_point = [640, 360]
y1 = 640
x = 640
width = 25

def setup(screen, etc):
    pass

def draw(screen, etc):
    global last_point, x, y1, width
    
    for i in range(0, 10) :
        seg(screen, etc, i)   

#print background color layer over entire image
    veil = pygame.Surface((1280,720))  
    veil.set_alpha(int(etc.knob3 * 200)) # adjust transparency on knob3
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0,0)) # (0,0) = starts at top left

def seg(screen, etc, i):
    global last_point, x, y1, width
   
    y1 = int(etc.knob2 * 720) + (etc.audio_in[i] / 70)
    colorr = etc.color_picker()
    color = (0,0,0)
    width = (etc.audio_in[i] / 100)

    pygame.draw.line(screen, colorr, last_point, [x, y1], width)
    
    speed = int(etc.knob1 * 40) - 20
    x = x + speed
    if x >= 1280: x = 0
    if 0 > x : x = 1280
    last_point = [x, y1]