CSCI534 ROBOT PLANNING & MANIPULATION
Final Project Implementation

Zabdiyel Tan | 30-Apr-2021

================================================================================
OVERVIEW
--------------------------------------------------------------------------------

This project seeks to frame the game Tetris as a task and motion planning
problem. The task planner will accept a tetromino, and a “BoardState” encoded as
a matrix of ones (occupied spaces) and zeros (free spaces). It will then use a
combination of several different greedy heuristics to judge a desired goal pose.
The motion planner will accept this pose along with the initial BoardState, and
determine a string of motion primitives (left, right, rotate, down) that takes
the input tetromino from the initial state to the goal pose.

For questions, contact Zabdiyel Tan at ztan@mines.edu

================================================================================
REQUIRED DEPENDENCIES
--------------------------------------------------------------------------------

Pygame
    Install pygame via pip (https://www.pygame.org/wiki/GettingStarted)
        From Linux terminal:
            python3 -m pip install -U pygame

================================================================================
USAGE
--------------------------------------------------------------------------------

1. Select a starting position from the BoardStates directory.
2. From terminal:
    python3 main.py <start_state_path>
3. Wait until Game Over message
4. To replay the game, run this command from terminal:
    python3 replay.py ./BoardStates/result/ <frame_delay_in_ms>

The prioritization scheme of the task planner can be modified to your liking.
Simply rearrange the code blocks in lines 78-122 of task_planner.py.

================================================================================
DOCUMENTATION
--------------------------------------------------------------------------------

Primary Files

    main.py
        Description:
            This file "plays Tetris" until game over.
        Args:
            File path of initial board state (use BoardStates directory)
        Returns:
            None
        Usage:
            python3 main.py <start_state_path>

    replay.py
        Description:
            This file replays a tetris game performed by main.py by displaying
            each result from the task planner in a window.
        Args:
            Directory path of game result (found in BoardStates directory)
            Delay (in ms) between displaying each step in the game
        Returns:
            None
        Usage:
            python3 replay.py ./BoardStates/result/ <frame_delay_in_ms>

    task_planner.py
        Description:
            Determine the best goal state for a given initial board state and
            tetromino
        Args:
            path (string): file location of initial board state
            shape_num (int): tetromino identifier
            outpath (string): file location of result board state
        Returns:
            goal_state (numpy array): array consisting of board state and pose
        Usage:
            python3 task_planner.py <path> <shape_num>

    motion_planner.py
        Description:
            Constructs a path plan given an initial board, goal_pose, and
            tetromino.
        Args:
            board (numpy array): initial board state
            goal_pose (tuple): (rotation, x, y) description of goal pose
            tetromino (Tetromino): input shape to construct path plan for
        Returns:
            None: Saves path plan to Solution/ directory
        Usage:
            Cannot be called from terminal
