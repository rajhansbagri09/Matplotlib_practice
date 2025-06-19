#Multiply two matrices (dot product).

import numpy as np 
arr1=np.array([[11,34,23],
               [56,78,96],
               [33,46,87]])

arr2=np.random.randint(1,100,size=(3,3))

print(arr1)
print()
print(arr2)

print("dot product")

dot=np.dot(arr1,arr2)
print(dot)