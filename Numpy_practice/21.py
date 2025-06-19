#Create a 10x10 matrix with values from 1 to 100 and extract the 2nd column

import numpy as np

ar10=np.random.randint(1,100,size=(10,10))
print("10x10 Matrix\n",ar10)

print("2nd col\n",ar10[:,1])