#19. Create a pie chart of expenditure percentages for 4 person.
# 20. Show the percentage values inside each slice.
# 21. Make one slice explode out slightly.
# 22. Add a title: “expenditure Share”.
#28. Save any plot as a PNG file named `my_chart.png`.


import matplotlib.pyplot as plt

name=["raj","raja","giri","adii"]
khr=[650,700,300,400]
exp=[0.1,0,0,0]

plt.pie(khr,labels=name,colors=["red","blue","green","yellow"],autopct="%1.1f%%",explode=exp)
plt.title("Expenditure shares")


plt.savefig("expPie.png",dpi=300,bbox_inches='tight')
plt.show()