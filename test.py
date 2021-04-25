#!/usr/local/bin/python3

from os import walk
import numpy as np

from tetromino import Tetromino
from task_planner import task_planner
from display_board_state import display_board_state
import shapes


_, _, filenames = next(walk("./Output"))
print(filenames)

for file in filenames:
    display_board_state('./Output/' + file)

