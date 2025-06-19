#Reshape a 1D array of 9 elements into a 3x3 matrix.

import numpy as np 

arr=np.array([1,2,3,4,5,6,7,8,2.9])

arrRe=arr.reshape(3,3)

print(arrRe)

print(type(arr))#class

print(arr.dtype)#type