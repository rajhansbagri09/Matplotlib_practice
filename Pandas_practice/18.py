import pandas as pd

d1=pd.DataFrame(
    {"name":["ra","as","sh"],
     "dep":["cs","jr","fin"],
     "id":[1,2,3]}
)

d2=pd.DataFrame(
    {"name":["av","ra","ap"],
     "dep":["ev","it","hw"],
     "id":[5,1,4]}
)

merged1=pd.merge(d1,d2, on="id",how="inner")
print(merged1)

merged2=pd.merge(d1,d2, on="id",how="outer")
print("outer\n",merged2)

merged3=pd.merge(d1,d2, on="id",how="right")
print("right\n",merged3)

merged4=pd.merge(d1,d2, on="id",how="left")
print("left\n",merged4)

merged5=pd.merge(d1,d2,how="cross")
print("cross\n",merged5)