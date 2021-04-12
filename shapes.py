#!/usr/local/bin/python3

import colors
from board_cell import BoardCell

class Shapes:
    I = [
        [BoardCell(colors.RED) for _ in range(4)] 
        for _ in range(4)
    ]
    I[0][1].is_occupied = True
    I[1][1].is_occupied = True
    I[2][1].is_occupied = True
    I[3][1].is_occupied = True
    # O = [
    #     [BoardCell for _ in range(4)] 
    #     for _ in range(4)
    # ]
    # T = [
    #     [BoardCell for _ in range(4)] 
    #     for _ in range(4)
    # ]
    # S = [
    #     [BoardCell for _ in range(4)] 
    #     for _ in range(4)
    # ]
    # Z = [
    #     [BoardCell for _ in range(4)] 
    #     for _ in range(4)
    # ]
    # J = [
    #     [BoardCell for _ in range(4)] 
    #     for _ in range(4)
    # ]