#How do you read a CSV file using Pandas?

import pandas as pd

fl=pd.read_csv("my1st.csv")
print(fl)

#What does the `info()` function of a DataFrame show?

print(fl.info())

#How do you get statistical summary of a DataFrame?
print("describe of numric col\n")

print(fl.describe())