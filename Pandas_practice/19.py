#19. How do you concatenate two DataFrames vertically?
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

con=pd.concat([d1,d2],axis=0,ignore_index=True)
print("row wise concatenate\n\n",con)

con2=pd.concat([d1,d2],axis=1,ignore_index=True)
print("col.. wise concatenate\n\n",con2)