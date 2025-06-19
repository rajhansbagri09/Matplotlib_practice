#Normalize a random array of floats (scale values between 0 and 1).
import numpy as np

arr= np.random.rand(10)*100
print(arr)

normalized_arr = (arr-arr.min())/(arr.max()-arr.min())


print("normalised array")
print(normalized_arr)

#bdi se bdi value ko 0 se 1 ke scale pr kr de but in same proportion

