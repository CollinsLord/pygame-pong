#! /usr/bin/env python3

import sys
import pygame
import random

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60

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
    def __init__(self, x, upkey, downkey):
        self.group = all_sprites
        pygame.sprite.Sprite.__init__(self, self.group)
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, HEIGHT / 2)
        self.y_speed = 0
        self.upkey = upkey
        self.downkey = downkey

    def update(self):
        self.y_speed = 0
        keys = pygame.key.get_pressed()
        if keys[self.upkey]:
            self.y_speed = -5
        if keys[self.downkey]:
            self.y_speed = 5
        self.rect.y += self.y_speed
        #self.rect.center = (self.x, self.y)
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > HEIGHT - PADDLE_HEIGHT:
            self.rect.y = HEIGHT - PADDLE_HEIGHT

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.y_speed = 0

    def update(self):
        self.rect.x += 3
        if self.rect.left > WIDTH:
            self.rect.right = 0
        
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
left_paddle = Paddle(30, pygame.K_q, pygame.K_z)
right_paddle = Paddle(WIDTH - 30, pygame.K_UP, pygame.K_DOWN)
all_sprites.add(left_paddle)
all_sprites.add(right_paddle)
ball = Ball()
all_sprites.add(ball)
while True:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    screen.fill(BLACK)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
