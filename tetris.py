#!/usr/local/bin/python3

import colors
from board_cell import BoardCell

class Tetris:

    board_height = 20
    board_width = 10
    grid_x = 20
    grid_y = 50
    square_width = 50
    tetrominos = []
    
    def __init__(self):

        # board is made of width * height BoardCells
        self.board = [
            [BoardCell(colors.WHITE) for _ in range(self.board_width)] 
            for _ in range(self.board_height)
        ]