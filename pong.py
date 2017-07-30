#! /usr/bin/env python3

import sys
import pygame

WIDTH = 800
HEIGHT = 600
FPS = 60

# define some colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x):
        self.group = all_sprites
        pygame.sprite.Sprite.__init__(self, self.group)
        self.x = x
        self.y = HEIGHT / 2
        self.image = pygame.Surface((20,100))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, HEIGHT / 2)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
left_paddle = Paddle(30)
right_paddle = Paddle(WIDTH - 30)
all_sprites.add(left_paddle)
all_sprites.add(right_paddle)
while True:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
