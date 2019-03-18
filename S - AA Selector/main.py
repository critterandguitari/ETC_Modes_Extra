import os
import pygame
import time
import random
import math

size = 400
count = 0
R = 1
avg = 0
color = (0,0,0)
A=B=C=D=E=F=G=H=I=J=K=5


def setup(screen, etc):
    pass

def draw(screen, etc):
    global size, count, avg, color
    
    for i in range(0, 100) :
        avg = abs(etc.audio_in[i]) + avg
    avg = avg / 100

    arcs = int(etc.knob1*9+1) #number of layers
    form = int(etc.knob3*6) #shape selector
    sel = int(etc.knob4*7) #color selector
    offset = etc.knob2 #layer offset on knob2, see below
    
    
    
    for i in range(arcs):
        
        if 6 <= sel : #full spectrum
            if arcs < 2 : i = 1
            color =    (int(127 + 127 * math.sin((i*36) * .1 + time.time())),
                        int(127 + 127 * math.sin((i*36) * .05+ time.time())),
                        int(127 + 127 * math.sin((i*36) * .01 + time.time())))
    
        if 1 <= sel < 2 : #red range
            red = 127
            green = 15
            blue = 5
            color =    (int(red+red * math.sin((i*6) * .01 + time.time())),
                        int(green + green * math.cos((i*6) * .03 + time.time())),
                        int(blue + blue * math.sin((i*6) * .01 + time.time())))
        
        if 2 <= sel < 3 : #yellow range
            color =    (int(127+127 * math.sin((i*6) * .01 + time.time())),
                        int(115+115 * math.sin((i*6) * .03 + time.time())),
                        int(25 + 25 * math.cos((i*6) * .01 + time.time())))
        
        if 3 <= sel < 4 : #green range
            color =    (int(35+35 * math.cos((i*6) * .01 + time.time())),
                        int(115+115 * math.sin((i*6) * .01 + time.time())),
                        int(25 + 25 * math.sin((i*6) * .01 + time.time())))
                        
        if 4 <= sel < 5 : #blue range
            color =    (int(5+5 * math.tan((i*6) * .01 + time.time()))%75,
                        int(45+45 * math.cos((i*6) * .01 + time.time())),
                        int(115 + 115 * math.sin((i*6) * .01 + time.time())))                
                        
        if 5 <= sel < 6 : #violet range
            color =     (int(100+100 * math.sin((i*6) * .01 + time.time())),
                        int(5+5 * math.sin((i*6) * .01 + time.time())),
                        int(75 + 75 * math.cos((i*6) * .01 + time.time())))
                        
        if sel < 1 : #grayscale
            color =     (int(127+127 * math.sin((i*6) * .01 + time.time())),
                        int(127+127 * math.sin((i*6) * .01 + time.time())),
                        int(127 + 127 * math.sin((i*6) * .01 + time.time())))                
    
        if form < 1 :
            A = abs(avg* 0.026) + abs(1000*offset*math.sin(i * .5 + time.time()))
            B = abs(avg* 0.05) + abs(1000*offset*math.sin(i * .5 + time.time()))    
            C = abs(avg* 0.071)   + abs(1000*offset*math.sin(i * .5 + time.time())) 
            D = abs(avg* 0.087) + abs(1000*offset*math.sin(i * .5 + time.time()))
            E = abs(avg* 0.097)+ abs(1000*offset*math.sin(i * .5 + time.time()))
            F = abs(avg* 0.1) + abs(1000*offset*math.sin(i * .5 + time.time()))
            G = abs(avg* 0.097) + abs(1000*offset*math.sin(i * .5 + time.time()))
            H = abs(avg*0.087)+ abs(1000*offset*math.sin(i * .5 + time.time()))
            I = abs(avg* 0.071)+ abs(1000*offset*math.sin(i * .5 + time.time()))
            J = abs(avg* 0.05)  + abs(1000*offset*math.sin(i * .5 + time.time()))
            K = abs(avg* 0.026)+ abs(1000*offset*math.sin(i * .5 + time.time()))
    
        if 1<=form< 2 :
        
            A = abs(avg* 0.026) + abs(1000*offset*math.sin(i * .5 + time.time()))
            B = abs(avg* 0.05) + abs(1000*offset*math.sin(i * .5 + time.time()))    
            C = abs(avg* 0.071)   + abs(1000*offset*math.sin(i * .5 + time.time())) 
            D = abs(avg* 0.087) + abs(1000*offset*math.cos(i * .5 + time.time()))
            E = abs(avg* 0.097)+ abs(1000*offset*math.sin(i * .5 + time.time()))
            F = abs(avg* 0.1) + abs(1000*offset*math.sin(i * .5 + time.time()))
            G = abs(avg* 0.097) + abs(1000*offset*math.sin(i * .5 + time.time()))
            H = abs(avg*0.087)+ abs(1000*offset*math.cos(i * .5 + time.time()))
            I = abs(avg* 0.071)+ abs(1000*offset*math.sin(i * .5 + time.time()))
            J = abs(avg* 0.05)  + abs(1000*offset*math.sin(i * .5 + time.time()))
            K = abs(avg* 0.026)+ abs(1000*offset*math.sin(i * .5 + time.time()))

        if 2 <= form < 3 :
            A = abs(avg* 0.026) + abs(1000*offset*math.tan(i * .5 + time.time()))
            B = abs(avg* 0.05) + abs(1000*offset*math.tan(i * .5 + time.time()))    
            C = abs(avg* 0.071)   + abs(1000*offset*math.tan(i * .5 + time.time())) 
            D = abs(avg* 0.087) + abs(1000*offset*math.tan(i * .5 + time.time()))
            E = abs(avg* 0.097)+ abs(1000*offset*math.tan(i * .5 + time.time()))
            F = abs(avg* 0.1) + abs(1000*offset*math.tan(i * .5 + time.time()))
            G = abs(avg* 0.097) + abs(1000*offset*math.tan(i * .5 + time.time()))
            H = abs(avg*0.087)+ abs(1000*offset*math.tan(i * .5 + time.time()))
            I = abs(avg* 0.071)+ abs(1000*offset*math.tan(i * .5 + time.time()))
            J = abs(avg* 0.05)  + abs(1000*offset*math.tan(i * .5 + time.time()))
            K = abs(avg* 0.026)+ abs(1000*offset*math.tan(i * .5 + time.time()))
    
        if 3<=form< 4 :
            A = abs(avg* 0.026) + abs(1000*offset*math.sin(i * .5 + time.time()))
            B = abs(avg* 0.05) + abs(1000*offset*math.cos(i * .5 + time.time()))    
            C = abs(avg* 0.071)   + abs(1000*offset*math.sin(i * .5 + time.time())) 
            D = abs(avg* 0.087) + abs(1000*offset*math.cos(i * .5 + time.time()))
            E = abs(avg* 0.097)+ abs(1000*offset*math.sin(i * .5 + time.time()))
            F = abs(avg* 0.1) + abs(1000*offset*math.cos(i * .5 + time.time()))
            G = abs(avg* 0.097) + abs(1000*offset*math.sin(i * .5 + time.time()))
            H = abs(avg*0.087)+ abs(1000*offset*math.cos(i * .5 + time.time()))
            I = abs(avg* 0.071)+ abs(1000*offset*math.sin(i * .5 + time.time()))
            J = abs(avg* 0.05)  + abs(1000*offset*math.cos(i * .5 + time.time()))
            K = abs(avg* 0.026)+ abs(1000*offset*math.sin(i * .5 + time.time()))
            
        if 4<=form < 5 :
            A = abs(avg* 0.026) + abs(1000*offset*math.tan(i * .5 + time.time()))
            B = abs(avg* 0.05) + abs(1000*offset*math.tan(i * .5 + time.time()))    
            C = abs(avg* 0.071)   + abs(1000*offset*math.tan(i * .5 + time.time())) 
            D = abs(avg* 0.087) + abs(1000*offset*math.tan(i * .5 + time.time()))
            E = abs(avg* 0.097)+ abs(1000*offset*math.sin(i * .5 + time.time()))
            F = abs(avg* 0.1) + abs(1000*offset*math.cos(i * .5 + time.time()))
            G = abs(avg* 0.097) + abs(1000*offset*math.sin(i * .5 + time.time()))
            H = abs(avg*0.087)+ abs(1000*offset*math.tan(i * .5 + time.time()))
            I = abs(avg* 0.071)+ abs(1000*offset*math.tan(i * .5 + time.time()))
            J = abs(avg* 0.05)  + abs(1000*offset*math.tan(i * .5 + time.time()))
            K = abs(avg* 0.026)+ abs(1000*offset*math.tan(i * .5 + time.time()))
   
        if 5<=form  :
            A = abs(avg* 0.026) + abs(1000*offset*math.cos(i * .5 + time.time()))
            B = abs(avg* 0.05) + abs(1000*offset*math.tan(i * .5 + time.time()))    
            C = abs(avg* 0.071)   + abs(1000*offset*math.cos(i * .5 + time.time())) 
            D = abs(avg* 0.087) + abs(1000*offset*math.cos(i * .5 + time.time()))
            E = abs(avg* 0.097)+ abs(1000*offset*math.cos(i * .5 + time.time()))
            F = abs(avg* 0.1) + abs(1000*offset*math.tan(i * .5 + time.time()))
            G = abs(avg* 0.097) + abs(1000*offset*math.cos(i * .5 + time.time()))
            H = abs(avg*0.087)+ abs(1000*offset*math.cos(i * .5 + time.time()))
            I = abs(avg* 0.071)+ abs(1000*offset*math.cos(i * .5 + time.time()))
            J = abs(avg* 0.05)  + abs(1000*offset*math.tan(i * .5 + time.time()))
            K = abs(avg* 0.026)+ abs(1000*offset*math.cos(i * .5 + time.time()))
            
            
        corner = abs(int(etc.audio_in[1]* (etc.knob3*2-1)/2))
    
        x = 1280
        y = 720
        
    #top arc
        pygame.draw.aalines(screen, color, False, [[0, corner], [22, A], [86, B], [187, C], [320, D], [474, E], [640, F], [806, G], [960, H], [1093, I], [1194, J], [1258, K], [x, corner]], 1)
    #bottom arc
        pygame.draw.aalines(screen, color, False, [[0, y-corner], [22, y-A], [86, y-B], [187, y-C], [320, y-D], [474, y-E], [640, y-F], [806, y-G], [960, y-H], [1093, y-I], [1194, y-J], [1258, y-K], [x,y-corner]], 1)

    #right arc
        pygame.draw.aalines(screen, color, False, [[x+corner, 0], [x-A, 12], [x-B, 48], [x-C, 105], [x-D, 180], [x-E, 267], [x-F, 360], [x-G, 453], [x-H, 540], [x-I, 615], [x-J, 672], [x-K, 708], [x-corner, y]], 1)
    
    #left arc
        pygame.draw.aalines(screen, color, False, [[corner, 0], [A, 12], [B, 48], [C, 105], [D, 180], [E, 267], [F, 360], [G, 453], [H, 540], [I, 615], [J, 672], [K, 708], [corner, y]], 1)
    
   



    
        
