#!/usr/local/bin/python3

import os
import shutil
import sys
import numpy as np

from task_planner import task_planner
from motion_planner import MotionPlanner
from read_board_state import read_board_state
from tetromino import Tetromino
import shapes

def main(state_in_dir, input_shapes):


    # clear old files
    dirs = ['./Output/', './Solution/', './BoardStates/result/']
    for dir in dirs:
        shutil.rmtree(dir)
        os.mkdir(dir)
    
    # solve
    i = 0
    for shape_num in input_shapes:

        # solve this shape
        state_out_dir = 'BoardStates/result/result_' + str(i).zfill(2)
        goal_state = task_planner(state_in_dir, shape_num, state_out_dir)

        board = read_board_state(state_in_dir)
        tetromino = Tetromino(shapes.shapes[int(shape_num)], 0, 4)
        motion_planner = MotionPlanner(board, goal_state[1], tetromino)
        
        path_out_dir = 'Solution/result_' + str(i).zfill(2) + '/'
        motion_planner.solve()
        motion_planner.save_path(path_out_dir)

        # set input board state to result of previous step
        state_in_dir = state_out_dir
        i += 1

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print(
            "usage: python3 main.py " 
            + "<path> "
            + "<shape_num> <shape_num> <shape_num> <shape_num> <shape_num>")
        exit(-1)
    else:
        main(sys.argv[1], sys.argv[2:])