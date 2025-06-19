#Find the maximum, minimum, and mean of a NumPy array.

import numpy as np

arr=np.random.randint(1,101,size=10)
print(arr)

print("maximum")
print(np.max(arr))

print("minimum")
print(np.min(arr))

print("mean")
print(np.mean(arr))

#Slice the first 3 elements from a NumPy array.

print(arr[:3])