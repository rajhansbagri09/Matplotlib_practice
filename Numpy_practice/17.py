#Extract the diagonal of a 2D array.

import numpy as np

arr2d=np.array([[1,2,3],
               [0,9,8],
               [4,5,6]])

print(arr2d)

print("it's diagonal")

diagnl= arr2d.diagonal()
print(diagnl)
