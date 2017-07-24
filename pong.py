#! /usr/bin/env python3

import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
