#Replace the maximum value in an array with 0
import numpy as np
ar10=np.random.randint(1,100,size=(3,3))
print(ar10)

flat=ar10.flatten()

flat[flat.argmin()]=0

arr_new= flat.reshape(ar10.shape)# arr10 ki shape me reshape hogya

print("new mat\n",arr_new)