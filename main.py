#!/usr/local/bin/python3

import os
import shutil
import sys
import time
import random
import numpy as np

from task_planner import task_planner
from motion_planner import MotionPlanner
from read_board_state import read_board_state
from tetromino import Tetromino
import shapes

def main(state_in_dir):


    # clear old files
    dirs = ['./Output/', './Solution/', './BoardStates/result/']
    for dir in dirs:
        shutil.rmtree(dir)
        os.mkdir(dir)
    
    # solve
    i = 0
    random.seed(int(time.time() * 1000))
    while True:

        shape_num = random.choice([0, 1, 2, 3, 4, 5, 6])

        # solve this shape
        state_out_dir = 'BoardStates/result/result_' + str(i).zfill(4)
        goal_state = task_planner(state_in_dir, shape_num, state_out_dir)
        if goal_state == 'Game Over':
            print("Game over with", str(i), "steps")
            exit()

        board = read_board_state(state_in_dir)
        tetromino = Tetromino(shapes.shapes[int(shape_num)], 0, 4)
        # print(shape_num, board, goal_state[1])
        motion_planner = MotionPlanner(board, goal_state[1], tetromino)
        
        path_out_dir = 'Solution/result_' + str(i).zfill(4) + '/'
        motion_planner.solve()
        motion_planner.save_path(path_out_dir)

        # set input board state to result of previous step
        state_in_dir = state_out_dir
        i += 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(
            "usage: python3 main.py " 
            + "<start_state_path> "
        )
        exit(-1)
    else:
        main(sys.argv[1])