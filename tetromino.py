#!/usr/local/bin/python3

import numpy as np

class Tetromino:

    def __init__(self, shape, row, col):
        self.shape = shape
        self.row = row
        self.col = col

    def rotate(self):
        """
        Rotates tetromino clockwise by 90 deg.
        """
        self.shape = np.rot90(self.shape, axes=(1, 0))
