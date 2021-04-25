#!/usr/local/bin/python3

import sys
import numpy as np

from read_board_state import read_board_state

def task_planner(path):
    """
    create goal states
        for ea rotation:
            try each col in bounds
            enforce gravity
            store as potential goal state

    choose best goal state
        priority:
            tetris
            3 lines cleared
            2 lines cleared
            1 line cleared
            min height
            min holes
    """
    board = read_board_state(path)
    print(board)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: python3 task_planner.py <path>")
        exit(-1)
    else:
        task_planner(sys.argv[1])
