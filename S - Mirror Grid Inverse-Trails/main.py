import os
import pygame

last_point = [320, 0]
last_point1 = [320, 0]

def setup(screen, etc):
    pass

def draw(screen, etc):
    
    global last_point, last_point1, speed, slide
    
    linewidth= int(16*etc.knob1)+1
    lines = 72
    spacehoriz = 180*etc.knob2+18
    spacevert = spacehoriz

    
    for m in range(0, lines) :
        x = m*spacehoriz
        y = 360
        auDio = etc.audio_in[m] / 35
        color = etc.color_picker()
        if auDio < 0 : auDio = 0
        pygame.draw.line(screen, color, [x,0], [x, y-auDio], linewidth)

    for i in range(0, lines) :
        x = i*spacehoriz
        y = 360
        color = etc.color_picker()
        auDio = etc.audio_in[i] / 35
        if auDio > 0 : auDio = 0
        pygame.draw.line(screen, color, [x,720], [x, y-auDio], linewidth)
        
    for j in range(0,lines) :
        
        pygame.draw.line(screen, color, (-1,j*spacevert), (1280,j*spacevert), linewidth)
    
    
    #Trails
    veil = pygame.Surface((1280,720))  
    veil.set_alpha(int(etc.knob3 * 200))
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0,0))