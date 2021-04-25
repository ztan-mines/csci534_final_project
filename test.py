#!/usr/local/bin/python3

import numpy as np

from tetromino import Tetromino
import shapes

test = Tetromino(shapes.J, 0, 0)
test.rotate()
test.rotate()
test.rotate()
test.rotate()
for row in test.shape:
    print(row)

