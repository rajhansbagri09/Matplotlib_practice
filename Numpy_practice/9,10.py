#Create an array of 10 linearly spaced points between 0 and 1.
import numpy as np

arr=np.array(np.arange(0,1,0.1))
print(arr)
print()
#correct

arr1=np.linspace(0,1,10)# linear spaced element
print(arr1)

#Reverse a NumPy array.
print("reverse of both array")
print()
print(arr[::-1])
print()
print(arr1[::-1])