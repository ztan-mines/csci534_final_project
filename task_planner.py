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

    tetromino = Tetromino(shapes.shapes[int(shape_num)], 0, -2)

    # create goal states
    for rot_num in range(4):  # for each unique rotation of shape (3)

        print()
        print()
        for row in tetromino.shape:
            print(row)

        for loc_col in range(-2, 12):  # all possible cols tetromino can be in
        # for loc_col in range(0, 3):  # all possible cols tetromino can be in

            print()
            print("next col")
            tetromino.row = -2  # new col, start at top
            tetromino.col = loc_col

            # find first valid row
            invalid_col = False
            while _collision_exists(tetromino, board):
                if tetromino.row >= 20:
                    invalid_col = True
                    break
                tetromino.row += 1
            
            if invalid_col:
                print('invalid col')
                continue
            print('found first valid row')

            # increment row until collision
            while True:
                tetromino.row += 1
                if _collision_exists(tetromino, board):  # row not valid
                    tetromino.row -= 1  # go back to last valid row
                    break


            # TODO: draw end state
            outboard = np.copy(board)
            for trow in range(4):
                for tcol in range(4):
                    if tetromino.shape[trow][tcol] == 2:  # collision matters (cell found)

                        # determine absolute location of tetris cell in board
                        brow = trow + tetromino.row
                        bcol = tcol + tetromino.col
                        outboard[brow][bcol] = 2
            outfile = open('./Output/test_output' + str(rot_num) + '_' + str(loc_col) + '.txt', 'w')
            for row in outboard:
                for col in row:
                    outfile.write(str(col) + " ")
                outfile.write('\n')
            outfile.close()
            # TODO: append to end states
            # TODO: try left and right

        tetromino.rotate()         


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
    for trow in range(4):
        for tcol in range(4):
            if tetromino.shape[trow][tcol] == 2:  # collision matters (cell found)

                # determine absolute location of tetris cell in board
                brow = trow + tetromino.row
                bcol = tcol + tetromino.col
                # print("bcol: " + str(bcol))

                # check collision
                if (
                    # check out of bounds
                    (brow < 0) or (brow > 19)
                    or (bcol < 0) or (bcol > 9)

                    # check collision w/ existing shapes
                    or (board[brow][bcol] != 0)
                ):
                    print("invalid at {0}, {1}".format(tetromino.row, tetromino.col))
                    return True
                # NOTE: cell is in valid location if this line reached
    # NOTE: all cells in valid location if this line reached
    print("valid at {0}, {1}".format(tetromino.row, tetromino.col))
    return False
                

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