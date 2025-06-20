#15. Plot a bar chart showing number of students in 5 different departments.
# 17. Change the bar color to sky blue.
# 18. Rotate x-axis labels by 45 degrees.

import matplotlib.pyplot as plt

y=[10,13,17,22,4]
x=["IT","EC","CV","CSE","A.I"]

plt.xlabel("Deparetments")
plt.ylabel("No' of Students")

plt.title("Bar Chart of students")
plt.bar(x,y,color="skyblue",label="Students")

plt.xticks(rotation=45)

plt.legend()
plt.show()