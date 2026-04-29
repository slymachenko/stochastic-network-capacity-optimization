# A simple module to import constant values into our notebooks
# Utility only - Later could be deleted

import numpy as np

c = np.concatenate([np.array([5, 3, 4]), np.array([5, 4, 5])])
u_nom = np.array([22, 10, 25, 10])

A_ineq = np.array([
    [ 1,  1,  1,  0,  0,  0],
    [ 0,  0,  0,  1,  1,  1],
    [ 1,  0,  0,  1,  0,  0],
    [ 0,  1,  0,  0,  1,  0],
    [ 0,  0,  1,  0,  0,  1],
    [-1,  0,  0,  1,  0,  0],
    [ 0, -1,  0,  0,  1,  0],
    [ 0,  0, -1,  0,  0,  1],
])

B = np.array([
    [ 1,  1,  1,  1],
    [ 1,  0,  0,  0],
    [ 0,  1,  0,  0],
    [ 0,  0,  1,  0],
    [ 0,  0,  0,  1],
    [ 0, -1,  0,  0],
    [ 0,  0, -1,  0],
    [ 0,  0,  0, -1],
])

bounds = [(5, 100), (5, 100), (5, 100), (0, 100), (0, 100), (0, 100)]