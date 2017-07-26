#! /usr/bin/env python3

import sys
import pygame

FPS = 60

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
while True:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
