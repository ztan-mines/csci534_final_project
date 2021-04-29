#!/usr/local/bin/python3

import sys
import numpy as np

def write_board_state(board, path):
    """
    Saves board to file specified by path.

    Params:
        board (numpy array): array representation of the board to save
        path (string): where to save the board, including the filename

    Returns:
        None
    """
    outfile = open(path, 'w')
    for row in board:
        for col in row:
            outfile.write(str(int(col)) + ' ')
        outfile.write('\n')
    outfile.close()