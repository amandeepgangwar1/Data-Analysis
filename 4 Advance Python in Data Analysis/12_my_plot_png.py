import matplotlib.pyplot as plt
import numpy as np
import matplotlib

x = np.linspace(0, 10, 100)
y = np.sin(x)

# create a plot
plt.figure(figsize=(8, 4))


plt.style.use("_mpl-gallery")             # Graph style
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.plot(x, y, label = "Sine Wave")
plt.title("Sine Wave Plot")
plt.savefig("my_plot.png")                 # for png
plt.savefig("my_plot.pdf")                 # for pdf
plt.show()