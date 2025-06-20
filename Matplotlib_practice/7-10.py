#7. Plot two lines on the same graph: one for sin(x) and another for cos(x).
# 8. Use different colors and styles for each line.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)  # 0 to 2π

y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin(x)", color="red", linestyle="--")
plt.plot(x, y2, label="cos(x)", color="orange", linestyle="-.")

#10. Add axis labels and a title: “Sine vs Cosine Waves”.
plt.title("Sine vs Cosine Waves")
plt.xlabel("Angle (radians)")
plt.ylabel("Value")
plt.grid()

#9. Add a legend to distinguish the two lines.
plt.legend()
plt.show()
