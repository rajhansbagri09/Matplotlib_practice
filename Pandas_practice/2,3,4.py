#Create a Pandas DataFrame using a dictionary.
import pandas as pd

df={"name":["raj","ashi","shreya","arpana","raja","avishi"]
    , "age" :[23,22,22,28,23,20],
    "study":["Btech","Mjmc","Mba","nthng","Msc","Btch"],
    "city":["sard","sard",'sard',"sard","sard","gr.n"],
    "salary":[95000,87000,90000,99000,91000,83000],
    "clr":["fair","silver","much fair","sweet","white","faad"]}

new_df= pd.DataFrame(df)
print(type(new_df))

print(new_df)

# How do you display the first 5 rows of a DataFrame?

print("above 5 row\n")

print(new_df.head())

#How can you select a single column from a DataFrame?

name=new_df["name"]
print(name)