#Compute the row-wise sum of a 2D array.

import numpy as np 

arr=np.array([[2,3,5],[55,66,76]])

new_arr=arr.sum(axis=1)#row wise sum

print(new_arr)