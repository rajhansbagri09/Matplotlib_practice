# How do you drop rows with any missing values?

import pandas as pd

data={"name":["aa","vv","df","ed"],
      "id":[1,2,3,None],
      "phn":[33,None,664,33]}
df=pd.DataFrame(data)
print(df)


df.dropna(axis=0,inplace=True)

print("\n",df)
