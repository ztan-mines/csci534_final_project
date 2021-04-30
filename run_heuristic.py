#!/usr/local/bin/python3

from os import walk
import numpy as np
import sys

from tetromino import Tetromino
from task_planner import task_planner
from display_board_state import display_board_state
import shapes

dir_name = sys.argv[1]

_, _, filenames = next(walk(dir_name))
filenames.sort()

for file in filenames:
    print()
    print(file)
    print()
    display_board_state(dir_name + file, int(sys.argv[2]))

