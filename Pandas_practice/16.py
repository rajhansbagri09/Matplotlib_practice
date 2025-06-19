#How do you sort a DataFrame by a specific column?

import pandas as pd

data={"name":["aa","vv","df","ed"],
      "id":[1,4,2,3],
      "phn":[39,76,664,33]}
df=pd.DataFrame(data)
print(df)

df.sort_values(by="id",ascending=True, inplace=True)

print("soreted data\n",df)