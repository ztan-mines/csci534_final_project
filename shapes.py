#!/usr/local/bin/python3

import numpy as np

I = np.array([
    [0, 2, 0, 0],
    [0, 2, 0, 0],
    [0, 2, 0, 0],
    [0, 2, 0, 0]
])

O = np.array([
    [0, 0, 0, 0],
    [0, 2, 2, 0],
    [0, 2, 2, 0],
    [0, 0, 0, 0]
])

T = np.array([
    [0, 0, 0, 0],
    [2, 2, 2, 0],
    [0, 2, 0, 0],
    [0, 0, 0, 0]
])

J = np.array([
    [0, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 2, 0],
    [0, 2, 2, 0]
])

L = np.array([
    [0, 0, 0, 0],
    [0, 2, 0, 0],
    [0, 2, 0, 0],
    [0, 2, 2, 0]
])

S = np.array([
    [0, 0, 0, 0],
    [0, 2, 2, 0],
    [2, 2, 0, 0],
    [0, 0, 0, 0]
])

Z = np.array([
    [0, 0, 0, 0],
    [2, 2, 0, 0],
    [0, 2, 2, 0],
    [0, 0, 0, 0]
])