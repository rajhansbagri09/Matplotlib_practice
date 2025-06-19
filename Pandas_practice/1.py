#Create a Pandas Series from a Python list.

import pandas as pd

lt=[1,2,3,4,5]

sr=pd.Series(lt)

print(sr)
print(sr.dtype)
print(type(sr))