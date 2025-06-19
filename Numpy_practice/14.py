#Create a random 4x4 matrix and compute its transpose.

import numpy as np

mat=np.random.randint(1,446,size=(4,4))
print(mat)

print()

new_mat=np.transpose(mat)

print(new_mat)