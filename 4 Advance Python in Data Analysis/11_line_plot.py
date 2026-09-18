import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# plt.plot(x, y)
plt.plot(x, y, color = "pink", linewidth = 2, linestyle = "--", marker = "o")
plt.title("Sample Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()