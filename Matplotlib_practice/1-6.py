#Plot a line graph of a company’s profit over 5 years.
#2. Label the x-axis as “Year” and y-axis as “Profit (in Lakhs)”.

import matplotlib.pyplot as plt

x=['2020','2021','2022','2023','2024']
y=[2200000,3400000,5500000,4500000,7000000]

plt.xlabel("Years")
plt.ylabel("Profits")

#5. Add a title to the graph: “Yearly Profit Trend”.
plt.title("Yearly Profit Trend")

#6. Enable grid lines on the plot.
plt.grid()

#3.Change the line color to green and style it as dashed.
# 4. Add square markers at each data point.

plt.plot(x,y, color="Green",linestyle="--", marker="s",label="Annual Profit")

plt.legend()
plt.show()