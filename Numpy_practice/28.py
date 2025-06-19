#Broadcast a 1D array to a 2D array (e.g., add a row vector to each row).

import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])

new=arr.reshape(3,3)

print(new)

broadcasted=np.array([10,20,30])

broad_arr=new + broadcasted 

print("broadcasted mat\n\n",broad_arr)

