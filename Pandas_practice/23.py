#How do you get the row with the maximum value in a column?
import pandas as pd

data = {
    "name": ["raj", "ashi", "shreya", "arpana"],
    "salary": [95000, 87000, 90000, 99000]
}

df = pd.DataFrame(data)

new_row=df[df["salary"]==df["salary"].max()]
print("highet salary",new_row)