#Stack two arrays vertically and horizontally.

import numpy as np

arr1=np.array([1,2,3,4,5])
arr2=np.array([0,9,8,7,6])

v_arr=np.vstack((arr1,arr2))
h_arr=np.hstack((arr1,arr2))

print(v_arr)
print()
print(h_arr)

s_arr=np.vsplit(v_arr)#verticall ssplit
print(s_arr)