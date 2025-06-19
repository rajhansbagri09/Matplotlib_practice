#Find the indices of non-zero elements in an array.

import numpy as np
arr= np.array([1,2,0,3,0,4,50,0,5])

index=np.nonzero(arr)
print(index)