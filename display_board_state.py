#!/usr/local/bin/python3

import sys
import pygame

color = {
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

def display_board_state(path, res=(800, 1080)):
    """
    Displays a given board state graphically given its filepath

    Params:
        path (string): path to file starting from this file's directory
        res (tuple): desired window resolution

    Returns:
        None: Output is a window displaying the board state
    """

    # initialize
    board_state_file = open(path, 'r')
    # pygame.init()
    # screen = pygame.display.set_mode(res)


    # TODO: display board
    pass


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 display_board_state.py <path>")
        exit(-1)
    else:
        display_board_state(sys.argv[1])