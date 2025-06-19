#How can you add a new column to an existing DataFrame?

import pandas as pd

df={"name":["raj","ashi","shreya","arpana","raja","avishi"]
    , "age" :[23,22,22,28,23,20],
    "study":["Btech","Mjmc","Mba","nthng","Msc","Btch"],
    "city":["sard","sard",'sard',"sard","sard","gr.n"],
    "salary":[95000,87000,90000,99000,91000,83000],
    "clr":["prime","silver","lovely","sweet","white","fair"]}

new_df= pd.DataFrame(df)

print(new_df)

new_df.insert(6,"phNo",[123,456,765,347,864,567])

print("added col\n",new_df)



#How do you write a DataFrame to a CSV file

new_df.to_csv("my1st.csv")
