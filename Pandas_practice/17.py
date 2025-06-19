#17. How do you group data using `groupby()` and get the mean?
import pandas as pd
df={"name":["raj","ashi","shreya","arpana","raja","avishi"]
    , "age" :[23,22,22,28,23,20],
    "study":["Btech","Mjmc","Mba","nthng","Msc","Btech"],
    "city":["sard","sard",'sard',"sard","sard","gr.n"],
    "salary":[95000,87000,90000,99000,91000,83000],
    "clr":["prime","silver","lovely","sweet","white","fair"]}

new_df= pd.DataFrame(df)

print(new_df)

group=new_df.groupby("age")["salary"].mean()

print("new group\n",group)

group2=new_df.groupby("study")["salary"].agg(["mean","count","max"])

print("new group\n",group2)