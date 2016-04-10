#!/bin/python
import os
import pygame
from pygame.locals import *
from sys           import exit

current_dir          = os.path.split(os.path.realpath(__file__))[0]
bird_file            = current_dir + "/bird.png"
obstacle_file        = current_dir + "/obstacle.png"
background_file      = current_dir + "/background.png"

screen_size          = (800,400)
background_size      = (800,400)

bird_size            = (40, 30)
bird_initial_point   = (200, 200 - bird_size[1]/2)

obstacle_size        = (40, 20)
max_obstacleid       = screen_size[1] / obstacle_size[1] - 1
miss_obstacles       = 3
gap                  = 40 #between two obstacle lines



pygame.init()
screen     = pygame.display.set_mode(screen_size, 0, 32)
pygame.display.set_caption("Reinforcement Learning")
background = pygame.image.load(background_file).convert()
bird       = pygame.image.load(bird_file).convert()
obstacle   = pygame.image.load(obstacle_file).convert()      


def update_bird(x, y):
    screen.blit(bird, (x,y))

def update_obstacle(gap_x, miss_obstacleid):
    if miss_obstacleid > max_obstacleid - miss_obstacles \
       or miss_obstacleid < 0:
        raise Exception("miss_obstacleid < 0 " \
                        "or miss_obstacleid > " \
                        "max_obstacleid(%d) - miss_obstacles(%d) - 1"\
                        %(max_obstacleid, miss_obstacles))

    for i in xrange(20):
        if i >= miss_obstacleid and i < miss_obstacleid + miss_obstacles:
            continue;
        screen.blit(obstacle, (gap_x, i * obstacle_size[1]));

def init():
    screen.blit(background, (0,0))
    update_bird(bird_initial_point[0], bird_initial_point[1])
    update_obstacle(360, 9);    
    update_obstacle(360 + obstacle_size[0] + gap, 11)
    pygame.display.update()


if __name__ == "__main__":
    init();

    while True:
    
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
