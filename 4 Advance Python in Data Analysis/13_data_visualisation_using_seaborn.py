# Scatter Plot



import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")           # import inbulit data from seaborn
print(df.head())

sns.scatterplot(x = "total_bill", y = "tip", data = df, hue = "sex")
plt.show()