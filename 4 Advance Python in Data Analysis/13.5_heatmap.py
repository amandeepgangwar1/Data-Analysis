import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")           # import inbulit data from seaborn
print(df.corr(numeric_only = True))

sns.heatmap(df.corr(numeric_only = True), annot = True)
plt.show()