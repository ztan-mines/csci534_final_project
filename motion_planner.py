#!/usr/local/bin/python3

import numpy as np

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

    def save_path(self):
        """
        Save each element in path to its own file in Solution/ directory
        """
    

if __name__ == "__main__":
    motion_planner()