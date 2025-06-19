# How do you create a new column based on conditions in other columns?
import pandas as pd

data = {
    "name": ["raj", "ashi", "shreya", "arpana"],
    "salary": [95000, 87000, 90000, 99000]
}

df = pd.DataFrame(data)

df["bounus"]=df["salary"]*15/100

print("added bonus\n",df)
print()
#27. How do you count unique values in a column?
count=df["salary"].count()
print("total count\n",count)