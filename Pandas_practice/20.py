import pandas as pd

data = {
    "name": ["raj", "ashi", "shreya", "arpana"],
    "salary": [95000, 87000, 90000, 99000]
}

df = pd.DataFrame(data)
df = df.sort_values(by="salary", ascending=True)
print("After sorting:\n", df)
df = df.reset_index(drop=True)
print("\nAfter reset_index:\n", df)
