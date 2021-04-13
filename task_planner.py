#!/usr/local/bin/python3

"""
create goal states
    for ea rotation:
        try each col in bounds
        enforce gravity
        store as potential goal state

choose best goal state
    priority:
        tetris
        3 lines cleared
        2 lines cleared
        1 line cleared
        min height
        min holes
"""