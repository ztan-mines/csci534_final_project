#!/usr/local/bin/python3

import numpy as np
import pygame
import random

TETRIS_VALS = {
    "board_height": 20,
    "board_width": 10,
    "board_ul_x": 20,
    "board_ul_y": 50,
    "space_width": 50
}
GUI_VALS = {
    "resolution": (800, 1080)
}
COLORS = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "gray": (128, 128, 128)
}

def main():
    res = (800, 1000)  # TODO: global var
    pygame.init()
    screen = pygame.display.set_mode(GUI_VALS["resolution"])
    done = False
    while not done:

        # check end conditions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        # draw background
        screen.fill(COLORS["white"])

        # draw grid
        for i in range(TETRIS_VALS["board_height"]):
            for j in range(TETRIS_VALS["board_width"]):
                pygame.draw.rect(
                    screen, 
                    COLORS["gray"], 
                    [
                        TETRIS_VALS["board_ul_x"] + TETRIS_VALS["space_width"] * j, 
                        TETRIS_VALS["board_ul_x"] + TETRIS_VALS["space_width"] * i, 
                        TETRIS_VALS["space_width"], 
                        TETRIS_VALS["space_width"]
                    ], 
                    1
                )

        # draw set tetrominos

        # draw active tetromino

        # update drawings
        pygame.display.flip()
        

    # """
    # create game board
    

    # while game not over:
    #     get new tetromino
    #     call task planner
    #     call motion planner
    #     perform plan
    #     check game over
    # """
    # print('hello world')
    # res = (800, 1000)
    # pygame.init()
    # screen = pygame.display.set_mode(res)
    # done = False
    # while not done:
    #     pygame.display.set_caption("Test")
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             done = True
    #     screen.fill(WHITE)
    #     pygame.draw.rect(screen, GRAY, pygame.Rect(100, 100, 100, 100))
    #     pygame.display.flip()
    #     # pygame.draw.rect(screen, WHITE, [1, 2, 3], 1)
        
    

if __name__ == "__main__":
    main()