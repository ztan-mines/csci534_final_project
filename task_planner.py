#!/usr/local/bin/python3

import sys
import numpy as np

import shapes
from tetromino import Tetromino
from read_board_state import read_board_state

def task_planner(path, shape_num):
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

    tetromino = Tetromino(shapes.shapes[int(shape_num)], -4, -2)

    # create goal states
    for rot_num in range(4):  # for each unique rotation of shape (3)
        for row in tetromino.shape:
            print(row)
        for loc_col in range(-2, 12):  # all possible columns tetromino can be in
            
            tetromino.col = loc_col
            if _collision_exists(tetromino, board):
                continue

            while True:  # increment row until collision
                tetromino.row += 1
                if _collision_exists(tetromino, board):  # row not valid
                    tetromino.row -= 1  # go back to last valid row
                    break  
        tetromino.rotate()         

            # TODO: draw end state
            # TODO: append to end states
            # TODO: try left and right

def _collision_exists(tetromino, board):
    """
    Helper function for task_panner()

    Param:
        tetromino (Tetromino): shape in play with up-to-date position
        board (numpy array): current board state

    Returns:
        (boolean): if tetromino is out of bounds or overlaps an occupied cell
    """
    # (trow, tcol) represent relative location of shape in 4x4 grid
    for trow in range(len(tetromino.shape)):
        for tcol in range(trow):
            if tetromino.shape[trow][tcol] == 2:  # collision matters (cell found)

                # determine absolute location of tetris cell in board
                brow = trow + tetromino.row
                bcol = tcol + tetromino.col

                # check collision
                if (
                    # check out of bounds
                    (brow < 0) or (brow > 19)
                    or (bcol < 0) or (bcol > 9)

                    # check collision w/ existing shapes
                    or (board[brow][bcol] != 0)
                ):
                    return False
                # NOTE: cell is in valid location if this line reached
    # NOTE: all cells in valid location if this line reached
    return True
                

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("usage: python3 task_planner.py <path> <shape_num>")
        exit(-1)
    else:
        task_planner(sys.argv[1], sys.argv[2])

    """
    for each rotation of shape:
        for each valid col in board:
            place
            add to list
            if can shift right
                shift right
                place
                add to list
            elif can shift left
                shift left
                place
                add to list

    place():  # enforce gravity but preserve shape
        while True
            row = new row
            if row not valid
                break
        write shape to board at row-1

    is_valid(location):
        True iff
            in bounds &&
            board[b_row][b_col] == 0
    """