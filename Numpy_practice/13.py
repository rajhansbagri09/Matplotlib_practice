#Create a 5x5 array and set the border elements to 1 and the inner to 0.

import numpy as np

arr=np.ones((5,5))

arr[1:-1,1:-1]=0

print(arr)