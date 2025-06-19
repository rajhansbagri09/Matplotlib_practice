#Create a checkerboard pattern 8x8 matrix using 0 and 1.


import numpy as np


checkerboard = np.zeros((8, 8), dtype=int)
checkerboard[1::2, ::2] = 1
checkerboard[::2, 1::2] = 1

print("8x8 pattern using 0 and 1\n",checkerboard)
