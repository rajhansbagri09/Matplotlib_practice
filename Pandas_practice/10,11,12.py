#How can you rename columns in a DataFrame?

import pandas as pd

fl=pd.read_csv("my1st.csv")
print(fl)

fl.rename(columns={"phNo":"ID"},inplace=True)
print("updated dataframe\n",fl)

#How do you filter rows based on a condition?

filtrrow=fl[fl["age"]==22]
print("22 age\n",filtrrow)

# How do you filter rows using multiple conditions?

mult=fl[(fl["age"]==22) & (fl["study"]=="Mba")]
print("pursing MBA\n",mult)