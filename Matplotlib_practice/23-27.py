#23. Plot a histogram showing the distribution of marks in a class.
# 24. Use 8 bins in the histogram.
#25. Set color to light green and add black edges to each bar.

#27. Set x-axis limits to 0–100 and y-axis limits to 0–50.

import matplotlib.pyplot as plt

Marks=[29,22,34,56,63,25,67,34,57,87,43,22,88,89,90,23,77,45,32,33,67,54,45]

plt.hist(Marks,bins=8,color="lightgreen",edgecolor="black")

plt.xlim(right=100)
plt.ylim(top=50)

plt.show()
