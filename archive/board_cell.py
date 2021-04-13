#!/usr/local/bin/python3

import colors

class BoardCell:

    is_occupied = False
    
    def __init__(self, color):
        self.color = color
        self.is_occupied = False