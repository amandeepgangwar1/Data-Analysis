import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")           # import inbulit data from seaborn
print(df.head())

sns.boxplot(x = "day", y = "total_bill", data = df)
plt.show()