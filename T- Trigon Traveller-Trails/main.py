import os
import pygame
import glob
import pygame.gfxdraw
import math

bkgrnd = pygame.Surface((1280, 720))
trot = 0
x1 = 640
y1 = 360
trigger = False

def setup(screen, etc):
    pass
def draw(screen, etc) :
    global bkgrnd, shape, trot, trigger, x1, y1
    
    color = etc.color_picker()
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
    if trigger == True :
        trot = (trot + 1)
    trigger = False    
    
    shape = pygame.Surface((200,400))
    pygame.gfxdraw.filled_trigon(shape, 0,400,100,0,200,400, color)    
    shape = pygame.transform.scale(shape, (200, 400))
    shape.set_colorkey ((0,0,0))

    shape = pygame.transform.rotate(shape, trot)
    new_width = shape.get_width()
    new_height = shape.get_height()
    x = (0 + new_width / 2)
    y = (0 + new_height / 2)
    speedx = etc.knob1 * 50 - 25
    speedy = etc.knob2 * 50 - 25

    screen.blit(shape, (x1-x, y1-y ))
    x1 = x1 + speedx
    y1 = y1 + speedy
    if x1 < 0 : x1 = 1280
    if x1 > 1280 : x1 = 0
    if y1 < 0 : y1 = 720
    if y1 > 720 : y1 = 0
    
    #Trails
    veil = pygame.Surface((1280,720))  
    veil.set_alpha(int(etc.knob3 * 200))
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0,0))