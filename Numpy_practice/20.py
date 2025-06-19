#Create a boolean mask from an array where values > 50.

import numpy as np

arr=np.array([[11,23,56,86,45],
             [34,2,3,55,67],
             [22,57,89,99,3]])
print("the array",arr)

mask=(arr > 50)

print("mask",mask)