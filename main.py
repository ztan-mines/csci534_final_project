#!/usr/local/bin/python3

import numpy as np
import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

def main():
    """
    create game board
    

    while game not over:
        get new tetromino
        call task planner
        call motion planner
        perform plan
        check game over
    """
    print('hello world')
    res = (1920, 1080)
    pygame.init()
    screen = pygame.display.set_mode(res)
    done = False
    while not done:
        pygame.display.set_caption("Test")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(WHITE)
        pygame.draw.rect(screen, GRAY, pygame.Rect(100, 100, 100, 100))
        pygame.display.flip()
        # pygame.draw.rect(screen, WHITE, [1, 2, 3], 1)
        
    

if __name__ == "__main__":
    main()