# A simple module to import constant values into our notebooks
# Utility only - Later could be deleted

import numpy as np

C_x = np.array([5, 3, 4]) # generation costs at nodes 2, 3, 4
C_y = np.array([5, 4, 5]) # distribution line costs
c = np.concatenate([C_x, C_y]) # objective function coefficients

# Nominal demand
u_nom = np.array([22, 10, 25, 10])

# Constraint matrix
A_ineq = np.array([
    [1, 1, 1, 0, 0, 0],   # total generation >= total demand
    [0, 0, 0, 1, 1, 1],   # inflow at node 1 >= demand at node 1
    [1, 0, 0, 1, 0, 0],   # node 2: generation + inflow >= demand
    [0, 1, 0, 0, 1, 0],   # node 3: generation + inflow >= demand
    [0, 0, 1, 0, 0, 1],   # node 4: generation + inflow >= demand
    [-1, 0, 0, 1, 0, 0],  # line 1 capacity for excess at node 2
    [0, -1, 0, 0, 1, 0],  # line 2 capacity for excess at node 3
    [0, 0, -1, 0, 0, 1]   # line 3 capacity for excess at node 4
])

B = np.array([
    [1, 1, 1, 1],   # total demand
    [1, 0, 0, 0],   # demand at node 1
    [0, 1, 0, 0],   # demand at node 2
    [0, 0, 1, 0],   # demand at node 3
    [0, 0, 0, 1],   # demand at node 4
    [0, -1, 0, 0],  # negative demand at node 2
    [0, 0, -1, 0],  # negative demand at node 3
    [0, 0, 0, -1]   # negative demand at node 4
])

bounds = [(5, 100), (5, 100), (5, 100), (0, 100), (0, 100), (0, 100)]

constraints_desc = [
    "Total generation >= total demand",
    "Inflow at node 1 >= demand at node 1",
    "Node 2: x2 + y1 >= u2",
    "Node 3: x3 + y2 >= u3",
    "Node 4: x4 + y3 >= u4",
    "Line 1 excess capacity",
    "Line 2 excess capacity",
    "Line 3 excess capacity"
]