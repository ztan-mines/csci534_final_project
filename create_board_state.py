#!/usr/local/bin/python3

import time
import random
import numpy as np

from write_board_state import write_board_state

def create_board_state():
    """
    Randomly generate an initial board state and save it to a file.
    """

    # randomly fill board grid
    board_height = 20
    board_width = 10
    board = np.zeros([board_width, board_height])  # start sideways for easier
                                                    # generation
    random.seed(int(time.time() * 1000))
    fill_chance = 0.125
    first_row_fill_chance = 1
    first_pass = True
    for row in range(1, len(board)):
        for col in range(len(board[row]) - 1):
            if random.random() <= fill_chance:
                board[row][col] = 1
            if first_pass:
                if random.random() <= first_row_fill_chance:
                    board[0][col] = 1
                first_pass = False

    board = _enforce_gravity(board)

    while True:
        should_continue, board = _clear_complete_rows(board, board_width)
        if not should_continue:
            break;

    # create new file
    path = "./BoardStates/random_" + str(int(time.time() * 1000))
    write_board_state(path, board)

def _enforce_gravity(board):
    """
    Helper function for create_board_state()

    Lets all occupied spaces "fall" in-clolumn towards bottom row and stack on
    top of each other.

    Params:
        board (numpy array): sideways game board

    Returns:
        board.T (numpy array): upright game board with gravity enforced
    """
    for row in range(len(board)):
        height = sum(board[row])
        for col in range(len(board[row])-1, -1, -1):
            board[row][col] = 0
            if height != 0:
                board[row][col] = 1
                height -= 1
    return board.T

def clear_complete_rows(board, board_width=10):
    """
    Helper function for create_board_state()
    
    Removes rows that are completely occupied (as per Tetris rules), and
    replaces them with a row of zeros at the top.

    Params:
        board (numpy array): initial board state
        board_width: number of spaces in a row

    Returns:
        (boolean): whether complete rows were found
        board (numpy array): final board state with complete rows removed
    """
    did_clear = False
    for row in range(len(board)):
        if sum(board[row]) == board_width:
            # row is complete, remove and replace at top
            board = np.delete(board, row, 0)
            board = np.insert(board, 0, np.zeros([board_width]), 0)
            did_clear = True
    return did_clear, board
    
if __name__ == "__main__":
    create_board_state()
