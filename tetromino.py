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
        # N = 4
        # for i in range(0, N//2):
        #     for j in range(i, N-i-1):
        #         temp = self.shape[i][j]
        #         self.shape[i][j] = self.shape[N - 1 - j][i]
        #         self.shape[N - 1 - j][i] = self.shape[N - 1 - i][N - 1 - j]
        #         self.shape[N - 1 - i][N - 1 - j] = self.shape[j][N - 1 - i]
        #         self.shape[j][N - 1 - i] = temp
