import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.style.use('ggplot')
plt.title("Sample Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# plt.scatter(x, y)
plt.scatter(x, y, s = 300, color = "green", alpha = 0.3)
plt.show()