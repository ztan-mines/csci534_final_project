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
    tetromino = Tetromino(shapes.shapes[int(shape_num)], 0, -2)
    end_states = _create_end_states(board, tetromino)


def _create_end_states(board, tetromino):  
    """
    Helper function for task_planner()

    Param:
        tetromino (Tetromino): shape in play with up-to-date position
        board (numpy array): current board state

    Returns:
        end_states (list): list of numpy arrays representing each possible end
                            state
    """

    end_states = []
    for rot_num in range(4):  # for each unique rotation of shape (3)
        for loc_col in range(-2, 12):  # all possible cols tetromino can be in

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
                continue

            # increment row until collision
            while True:
                tetromino.row += 1
                if _collision_exists(tetromino, board):  # row not valid
                    tetromino.row -= 1  # go back to last valid row
                    break

            # save end state to file
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

            # append to end state set
            end_states.append(outboard)

        tetromino.rotate()

    return end_states


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

                # check collision
                if (
                    # check out of bounds
                    (brow < 0) or (brow > 19)
                    or (bcol < 0) or (bcol > 9)

                    # check collision w/ existing shapes
                    or (board[brow][bcol] != 0)
                ):
                    return True
                # NOTE: cell is in valid location if this line reached
    # NOTE: all cells in valid location if this line reached
    return False
                

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("usage: python3 task_planner.py <path> <shape_num>")
        exit(-1)
    else:
        task_planner(sys.argv[1], sys.argv[2])
