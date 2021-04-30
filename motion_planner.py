#!/usr/local/bin/python3

import numpy as np
from write_board_state import write_board_state

class MotionPlanner:
    """
    load board state
    get tetromino
    find possible goals
    find best goal
    pass best goal to motion planner
    print plan
    pass plan to demonstrator (shows plan step by step)
    """

    path = np.array([])

    def __init__(self, board, goal_pose, tetromino)
        # TODO
        pass

    def solve(self):

        # shift left/right until in correct column
        while self.tetromino.col != goal_pose[1]:
            if self.tetromino.col - goal_pose[1] > 0:
                self.tetromino.col -= 1
            else:
                self.tetromino.col += 1
                save_to_path()

        # fall until in correct row
        while self.tetromino.row != goal_pose[0]:
            self.tetromino.row += 1
            save_to_path()

    def save_to_path(self):
        """
        write tetromino on board
        path.append(board)
        """
        self.update_board()

        # append to path
        path_step = np.copy(board)
        self.path.append(path_step)           
         
    def update_board(self):
        """
        Remove previous tetromino location and replace with current location

        """
        # remove previous tetromino location
        for r in range(len(self.board)):
            for c in range(r):
                if self.board[r][c] == 2:
                    self.board[r][c] == 0

        # write out current location to the board
        for trow in range(4):
            for tcol in range(4):
                if tetromino.shape[trow][tcol] == 2:  # cell found
                    self.brow = trow + tetromino.row
                    self.bcol = tcol + tetromino.col
                    self.board[brow][bcol] = 2

    def save_path(self):
        """
        Save each element in solution path to its own file in Solution/ dir
        """
        i = 0
        for path_step in path:
            path = 'Solution/step_' + str(i)
            write_board_state(path, path_step)
            i += 1
    
if __name__ == "__main__":
    motion_planner()