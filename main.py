#!/usr/local/bin/python3

import os
import sys
import numpy as np

from task_planner import task_planner
from motion_planner import MotionPlanner
from read_board_state import read_board_state
from tetromino import Tetromino
import shapes

def main(path, shape_num):


    # clear old files
    dirs = ['./Output/', './Solution/']
    for dir in dirs:
        _, _, files = next(os.walk(dir))
        for file in files:
            os.remove(dir+file)

    board = read_board_state(path)
    tetromino = Tetromino(shapes.shapes[int(shape_num)], 0, 4)
    goal_state = task_planner(path, shape_num)
    motion_planner = MotionPlanner(board, goal_state[1], tetromino)
    motion_planner.solve()
    motion_planner.save_path()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python3 main.py <path> <shape_num>")
        exit(-1)
    else:
        main(sys.argv[1], sys.argv[2])