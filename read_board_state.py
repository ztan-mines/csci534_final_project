#!/usr/local/bin/python3

import sys
import numpy as np

def read_board_state(path):
    """
    Stores board state given by file path into a numpy array

    Params:
        path (string): relative path to board state file
        board (numpy array): board state as a numpy array 
    """

    # open board state file
    board_state_file = open(path, 'r')

    # load text board into numpy array
    board = []
    while True:
        
        line = board_state_file.readline()
        if line == '':  # end of file
            break
        
        line = line.split()
        board_row = [int(i) for i in line]
        board.append(board_row)

    return np.array(board)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: python3 read_board_state.py <path>")
        exit(-1)
    else:
        read_board_state(sys.argv[1])
