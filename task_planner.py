#!/usr/local/bin/python3

from read_board_state import read_board_state

def task_planner():
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
    pass

if __name__ == '__main__':
    task_planner()
