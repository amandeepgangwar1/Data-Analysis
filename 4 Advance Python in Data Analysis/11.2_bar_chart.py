import matplotlib.pyplot as plt

categories = ['A', 'B' , 'C', 'D']
values = [10, 13, 15, 25]

plt.title("Sample Bar Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.bar(categories, values)
plt.show()