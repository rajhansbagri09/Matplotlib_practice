#11. Create two subplots in one figure: Top plot: y = x², Bottom plot: y = sqrt(x)
#Add titles to each subplot.
# 13. Ensure both plots share the same x-axis.
import matplotlib.pyplot as plt

# Correct: returns both fig and axes
fig, ax = plt.subplots( 2,1, figsize=(10, 5))

y = [2, 4, 6, 8, 10]
x1 = [4, 16, 36, 64, 100]
x2 = [1.414, 2, 2.44, 2.82, 3.16]

# Left subplot
ax[0].plot(y, x1, color="blue",marker="s")
ax[0].set_title("Square: y = x²")
ax[0].set_xlabel("Y")
ax[0].set_ylabel("X1 ")

# Right subplot
ax[1].plot(y, x2, color="green",marker="o")
ax[1].set_title("Square Root: y = sqrt(x)")
ax[1].set_xlabel("Y")
ax[1].set_ylabel("X2 ")

# Clean layout
# 13. Ensure both plots share the same x-axis.
plt.tight_layout(h_pad=0)
plt.show()
