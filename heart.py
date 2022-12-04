#Giáo Ộp IT
import pygame
import sys
from math import sin, cos, pi
import random
import time

from pygame.locals import *

pygame.init()
pygame.font.init()

WINDOW_SIZE = [1000, 1000]

screen_main = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE, 32)
screen_blur = pygame.Surface(WINDOW_SIZE, SRCALPHA, 32)


def heart(WINDOW_SIZE, SCALE_IN, step, clear_mid):
    list_point = []
    
    t = 0
    while t <= pi * 2:
        x = SCALE_IN * 16 * pow(sin(t), 3)
        y = -1 * SCALE_IN * (14 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t))
        
        if clear_mid:
            num = 1
            if not(int(x) < SCALE_IN * step * num and int(x) >  SCALE_IN * -1 * step * num):
                list_point.append([x + WINDOW_SIZE[0] / 2, y + WINDOW_SIZE[1] / 2])
        else:
            list_point.append([x + WINDOW_SIZE[0] / 2, y + WINDOW_SIZE[1] / 2])
        
        t += step
    
    return list_point


def draw_heart(screen_main, WINDOW_SIZE, SCALE_IN, COLOR, RADIUS, step, clear_mid = False):
    list_points = heart(WINDOW_SIZE, SCALE_IN, step, clear_mid)
    for point in list_points:
        x = point[0]
        y = point[1]
    
        pygame.draw.circle(screen_main, COLOR, (x, y), RADIUS)
    return list_points


def create_particles_in(heart_point_in, num):
    list_vecs = []
    
    for point in heart_point_in:
        point = [point[0] - WINDOW_SIZE[0] / 2, point[1] - WINDOW_SIZE[1] / 2]
        temp = []
        for _ in range(num):
            test = random.randint(3, 10)
            multi = random.randint(30, 100)

            vec = [i * test / multi for i in point]
            temp.append(vec)
        list_vecs.append(temp)
    return list_vecs


def create_particles_out(heart_point_in, num):
    list_vecs = []
    
    for point in heart_point_in:
        point = [point[0] - WINDOW_SIZE[0] / 2, point[1] - WINDOW_SIZE[1] / 2]
        temp = []
        
        for _ in range(num):
            test = random.randint(2, 7)
            multi = random.randint(30, 100)

            vec = [i * test / multi for i in point]
            temp.append(vec)
        list_vecs.append(temp)
    return list_vecs


def draw_point(screen_main, screen_blur, point, COLOR, COLOR_BLUR, RADIUS_POINT, RADIUS_BLUR):
    pygame.draw.circle(screen_blur, COLOR_BLUR, point, RADIUS_BLUR)
    pygame.draw.circle(screen_main, COLOR, point, RADIUS_POINT)

reverse = False

size_heart = [10, 12]

COLOR_IN = (255, 30, 153)
COLOR_OUT = (255, 35, 163)

SCALE_IN = 10
SCALE_OUT = SCALE_IN + 5

SPEED_SHINK = [0, 0]
PARTICLE_VEC = [0, 0]

POINT_SIZE = 2
BLUR_SIZR = 3

vec_lists_in = []
vec_lists_out = []

rgb = False
count = 0
start = time.time()

count_RGB = 0
while True:
    

    screen_main.fill((0, 0, 0))
    screen_blur.fill((0, 0, 0))
    
    if int(time.time() - start) >= 5:
       
        PARTICLE_VEC = [0.4, random.randint(15, 30)/100]
        COLOR_IN = [255, 0, 0]
        if not rgb:
            COLOR_OUT = [0, 0, 0]
            rgb = True
        SPEED_SHINK = [11, 10]
    else:
       
        SPEED_SHINK = [6, 6]
        PARTICLE_VEC = [0.3, 0.3]
    

    heart_point_in = draw_heart(screen_main, WINDOW_SIZE, SCALE_IN, COLOR_IN, 0, 0.01)
    heart_point_out = draw_heart(screen_main, WINDOW_SIZE, SCALE_OUT, COLOR_IN, 0, 0.02, True)
    
    
    if vec_lists_in == [] and vec_lists_out == []:
        vec_lists_in = create_particles_in(heart_point_in, 3)
        vec_lists_out = create_particles_out(heart_point_out, 6)
    

    BLUR_COLOR = (255, 100, 200, 80)
    for point, vecs in zip(heart_point_in, vec_lists_in):
        for vec in vecs:
            # Update particle
            point = [point[0] - vec[0], point[1] - vec[1]]
            draw_point(screen_main, screen_blur, point, COLOR_IN, BLUR_COLOR, POINT_SIZE, BLUR_SIZR)

    BLUR_COLOR = (235, 160, 220, 90)
    for point, vecs in zip(heart_point_out, vec_lists_out):
        for vec in vecs:        
            
            # Control movement of particle
            if reverse:
                if vec[0] >= 0:
                    vec[0] -= PARTICLE_VEC[0]
                else:
                    vec[0] += PARTICLE_VEC[0]

                if vec[1] >= 0:
                    vec[1] -= PARTICLE_VEC[0]
                else:
                    vec[1] += PARTICLE_VEC[0]
            else:
                if vec[0] >= 0:
                    vec[0] -= PARTICLE_VEC[1]
                else:
                    vec[0] += PARTICLE_VEC[1]

                if vec[1] >= 0:
                    vec[1] += PARTICLE_VEC[1]
                else:
                    vec[1] -= PARTICLE_VEC[1]
            
            # Update particle
            point = [point[0] - vec[0], point[1] - vec[1]]

            # Control RGB in heart_out
            if rgb:
                if count_RGB%20 == 0:
                    COLOR_OUT[2] += 1
                
                if count_RGB%40 == 0:
                    COLOR_OUT[1] += 1
                
                if count_RGB%60 == 0:
                    COLOR_OUT[0] += 1
            
                for i in range(len(COLOR_OUT)):
                    if COLOR_OUT[i] >= 255:
                        COLOR_OUT[i] = 255

                if COLOR_OUT == [255, 255, 255]:
                    COLOR_OUT = [0, 0, 0]
            
            draw_point(screen_main, screen_blur, point, COLOR_OUT, BLUR_COLOR, POINT_SIZE, BLUR_SIZR)

    # Control heart beat
    if reverse:
        SCALE_IN += SPEED_SHINK[0]/105
    else:
        SCALE_IN -= SPEED_SHINK[1]/105
    
    if SCALE_IN <= size_heart[0]:
        reverse = True
        count += 3
    elif SCALE_IN >= size_heart[1]:
        reverse = False
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen_main.blit(screen_blur, (0, 0))
    pygame.display.update()
