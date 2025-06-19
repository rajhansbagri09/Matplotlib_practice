#How do you check for missing values in a DataFrame?

import pandas as pd

data={"name":["aa","vv","df","ed"],
      "id":[1,2,3,None],
      "phn":[33,None,664,33]}
df=pd.DataFrame(data)
print(df)

print("any NAN\n")
print(df.isna())#df.isnull()

print("kitne Null hai:",df.isna().sum())

#How do you fill missing values in a column with the mean?

df["id"]=df["id"].fillna(df["id"].mean())
df["phn"]=df["phn"].fillna(df["phn"].mean())
#df[col] = df[col].method(value)
print("update df",df)

# How do you drop rows with any missing values?

df.drop(axis=0,inplace=True,index=False)

print("\n",df)

