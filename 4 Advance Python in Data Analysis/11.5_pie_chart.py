import matplotlib.pyplot as plt
import numpy as np

sizes = [40, 36, 28, 32]
labels = ["XXL", "XL", "XS", "L"]
plt.pie(sizes, labels = labels, autopct = "%1.1f%%")
plt.show()