#Find the unique elements in a NumPy array.

import numpy as np

arr=np.array([[3,23,2,45],[3,2,44,56]])

print(arr[1,2])#specific element

uni_el=np.unique(arr)#unique no
print(uni_el)