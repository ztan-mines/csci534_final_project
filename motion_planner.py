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

    path = []
    initial_pose = [0, 5]

    def __init__(self, board, goal_pose, tetromino):
        self.board = board
        self.goal_pose = goal_pose
        self.tetromino = tetromino

    def solve(self):

        # shift left/right until in correct column
        while self.tetromino.col != self.goal_pose[1]:
            if self.tetromino.col - self.goal_pose[1] > 0:
                self.tetromino.col -= 1
            else:
                self.tetromino.col += 1
                self.save_to_path()

        # fall until in correct row
        while self.tetromino.row != self.goal_pose[0]:
            self.tetromino.row += 1
            self.save_to_path()

    def save_to_path(self):
        """
        write tetromino on board
        path.append(board)
        """
        self.update_board()

        # append to path
        path_step = np.copy(self.board)
        self.path.append(path_step)
        # np.append(self.path, path_step)          
         
    def update_board(self):
        """
        Remove previous tetromino location and replace with current location
        """
        # remove previous tetromino location
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] == 2:
                    self.board[r][c] = 0

        # write out current location to the board
        for trow in range(4):
            for tcol in range(4):
                if self.tetromino.shape[trow][tcol] == 2:  # cell found
                    brow = trow + self.tetromino.row
                    bcol = tcol + self.tetromino.col
                    self.board[brow][bcol] = 2

    def save_path(self):
        """
        Save each element in solution path to its own file in Solution/ dir
        """
        i = 0
        for path_step in self.path:
            self.path = 'Solution/step_' + str(i).zfill(2)
            write_board_state(self.path, path_step)
            i += 1
    
if __name__ == "__main__":
    motion_planner()