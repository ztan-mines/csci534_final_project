#!/usr/local/bin/python3

import sys
import numpy as np
import random

import shapes
from tetromino import Tetromino
from read_board_state import read_board_state
from write_board_state import write_board_state



def task_planner(path, shape_num):
    """
    Determine the best goal state for a given initial board state and tetromino

    Params:
        path (string): file location of initial board state
        shape_num (int): tetromino identifier
    """
    board = read_board_state(path)
    tetromino = Tetromino(shapes.shapes[int(shape_num)], 0, -2)
    end_states = _create_end_states(board, tetromino)

    all_stats = []
    for state in end_states:

        # calc num lines cleared
        num_lines_cleared = 0
        state_copy = np.copy(state)
        state_copy[state_copy > 1] = 1
        row_sums = state_copy.sum(axis=1)
        for sum in row_sums:
            assert sum < 11  # row cannot be overfull
            assert sum >= 0  # row cannot have negative numbers
            if sum == 10:
                num_lines_cleared += 1

        # calc height
        height = 0
        for i in range(len(row_sums)):
            if row_sums[i] > 0:
                height = 20 - (i + 1)
                break

        # TODO: calc num holes
        num_holes = 0
        """
        for each col
            for each row
                if cell is 1
                    count all zeros below
        """


        all_stats.append((state, num_lines_cleared, height, num_holes))

    # prioritize most lines cleared
    max_lines_cleared = 0
    best_lines_cleared = []
    for stats in all_stats:
        if stats[1] >= max_lines_cleared:
            max_lines_cleared = stats[1]
            best_lines_cleared.append(stats)

    # next, prioritize smallest height
    min_height = 20
    best_height = []
    for stats in best_lines_cleared:
        if stats[2] <= min_height:
            min_height = stats[2]
            best_height.append(stats)
    
    # finally, prioritize fewest holes
    min_holes = 200
    best = []
    for stats in best_height:
        if stats[3] <= min_holes:
            min_holes = stats[3]
            best.append(stats)

    goal_state = random.choice(best)[0]

    return goal_state


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
            path = './Output/test_output' + str(rot_num) + '_' + str(loc_col) + '.txt'
            write_board_state(outboard, path)

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
