CSCI534 ROBOT PLANNING & MANIPULATION
Final Project Implementation

Zabdiyel Tan

--------------------------------------------------------------------------------
OVERVIEW

--------------------------------------------------------------------------------
BUILD INSTRUCTIONS

Install pygame via pip (https://www.pygame.org/wiki/GettingStarted)

    1. From Linux terminal:
        python3 -m pip install -U pygame


--------------------------------------------------------------------------------
TODO


    Task Planner
        test

    Motion Planner
        determine motion plan
            get start state
            translate left/right to proper column
            increase row until collision
        print steps from start state to end state

    Experiments
        Compare to previous work
            Code Bullet's algorithm
            advantages
                less complex, more computationally efficient
            disadvantages
                does not explore all possible end states


--------------------------------------------------------------------------------
NOTES

    BoardStates/random_1619712341398