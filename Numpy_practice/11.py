#Replace all even numbers in an array with -1.

import numpy as np

arr=np.array([1,20,3,40,7,70,40,9,7])
arr1=np.random.rand(8)

arr[arr % 2==0]=-1
arr1[arr1 % 2==0]=-2

print(arr)
print()
print(arr1)