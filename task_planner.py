#!/usr/local/bin/python3

import sys
import numpy as np
import random

import shapes
from tetromino import Tetromino
from read_board_state import read_board_state
from write_board_state import write_board_state
from create_board_state import clear_complete_rows


def task_planner(path, shape_num, outpath):
    """
    Determine the best goal state for a given initial board state and tetromino

    Params:
        path (string): file location of initial board state
        shape_num (int): tetromino identifier
        outpath (string): file location of result board state
    """
    board = read_board_state(path)
    board[board > 1] = 1
    _, board = clear_complete_rows(board)
    tetromino = Tetromino(shapes.shapes[int(shape_num)], 0, -2)
    end_states = _create_end_states(board, tetromino)

    all_stats = []
    for item in end_states:

        state = item[0]

        # count lines cleared
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
                height = 20 - i
                break

        # count holes (any space below a block is a hole)
        num_holes = 0
        for c in range(len(state[0])):

            start_counting_holes = False
            for r in range(len(state)):

                if not start_counting_holes:
                    if state[r][c] > 0:  # potential ceiling block found
                        start_counting_holes = True
                else:
                    if state[r][c] == 0:  # zero found below nonzero
                        num_holes += 1

        # count empty spaces in bottom row
        num_empty = 0
        for space in state[len(state)-1]:
            if space == 0:
                num_empty += 1

        all_stats.append(
            (item, num_lines_cleared, height, num_holes, num_empty)
        )

    best_stats = all_stats

    # prioritize filling bottom row
    min_empty_spaces = 10
    for stats in best_stats:
        if stats[4] <= min_empty_spaces:
            min_empty_spaces = stats[4]
    temp_best = []
    for stats in best_stats:
        if stats[4] <= min_empty_spaces:
            temp_best.append(stats)
    best_stats = temp_best

    # prioritize smallest height
    min_height = 20
    for stats in best_stats:
        if stats[2] <= min_height:
            min_height = stats[2]
    temp_best = []
    for stats in best_stats:
        if stats[2] <= min_height:
            temp_best.append(stats)
    best_stats = temp_best
    if min_height >= 20:
        return 'Game Over'
    
    # prioritize fewest holes
    min_holes = 200
    for stats in best_stats:
        if stats[3] <= min_holes:
            min_holes = stats[3]
    temp_best = []
    for stats in best_stats:
        if stats[3] <= min_holes:
            temp_best.append(stats)
    best_stats = temp_best

    # prioritize most lines cleared
    max_lines_cleared = 0
    for stats in best_stats:
        if stats[1] >= max_lines_cleared:
            max_lines_cleared = stats[1]
    temp_best = []
    for stats in best_stats:
        if stats[1] >= max_lines_cleared:
            temp_best.append(stats)
    best_stats = temp_best

    goal_state = random.choice(best_stats)[0]
    write_board_state(outpath, goal_state[0])

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
            end_pose = [0, 0, 0]

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
            end_pose[0] = tetromino.row
            end_pose[1] = tetromino.col
            end_pose[2] = rot_num
            outboard = np.copy(board)
            for trow in range(4):
                for tcol in range(4):
                    if tetromino.shape[trow][tcol] == 2:  # collision matters 
                                                            # (cell found)

                        # determine absolute location of tetris cell in board
                        brow = trow + tetromino.row
                        bcol = tcol + tetromino.col
                        outboard[brow][bcol] = 2
            path = str(
                './Output/possible_state' 
                + str(rot_num) 
                + '_' + str(loc_col) + '.txt'
            )
            write_board_state(path, outboard)

            # append to end state set
            end_states.append((outboard, end_pose))

        tetromino.rotate()


    return end_states


def _collision_exists(tetromino, board):
    """
    Helper function for task_planner()

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
