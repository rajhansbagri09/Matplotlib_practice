#Get common values between two NumPy arrays.

import numpy as np

arr1=np.array([1,2,3,4,5])
arr2=np.array([8,7,65,3,4])

print(np.intersect1d(arr1,arr2))


#Convert a NumPy array to a Python list.

l1=arr1.tolist()

print(l1)