#!/usr/local/bin/python3

import sys
import pygame
import numpy as np
import time

from read_board_state import read_board_state

colors = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "GRAY": (128, 128, 128),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "YELLOW": (255, 255, 0),
    "MAGENTA": (255, 0, 255),
    "CYAN": (0, 255, 255)
}

res = (400, 800)

cell_dim = res[0]/12

def display_board_state(path, autoclose=-1):
    """
    Displays a given board state graphically given its filepath

    Params:
        path (string): path to file starting from this file's directory
        autoclose (int): ms delay before closing window (-1 waits on user)

    Returns:
        None: Output is a window displaying the board state
    """

    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode(res)

    # load text board into numpy array
    board = read_board_state(path)

    # display board until window closed
    done = False
    ti = int(time.time() * 1000)
    while not done:

        # check end
        delta_t = int(time.time() * 1000) - ti
        if (delta_t >= autoclose) and (autoclose > -1):
            done = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # draw background
        screen.fill(colors['WHITE'])

        # draw board state
        for row in range(20):
            for col in range(10):

                # determine how to draw cell (occupied or unoccupied)
                color = colors["GRAY"]
                no_fill = 1  # transparent rectangle
                if board[row][col] == 1:  # cell is previously occupied
                    color = colors["BLACK"]
                    no_fill = 0  # filled rectangle
                elif board[row][col] == 2:  # cell occupied by input tetromino
                    color = colors["CYAN"]
                    no_fill = 0  # filled rectangle

                # draw cell
                pygame.draw.rect(
                    screen, 
                    color, 
                    [
                        cell_dim * (col + 1), 
                        cell_dim * (row + 2), 
                        cell_dim, 
                        cell_dim
                    ], 
                    no_fill
                )

        # update drawings
        pygame.display.flip()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 display_board_state.py <path>")
        exit(-1)
    else:
        display_board_state(sys.argv[1])