import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")           # import inbulit data from seaborn
print(df.head())

sns.countplot(x = "day", data = df)
plt.show()