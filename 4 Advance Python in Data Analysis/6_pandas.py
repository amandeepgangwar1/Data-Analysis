import pandas as pd
data = {
    "name" : ["Ali", "Sara", "John", "Aman", "Sanya", "Priya", "Sakshi"],
    "marks" : [85, 90, 78, 88, 68, 43, 54]
}

df = pd.DataFrame(data)
print(df)

print(df.head())
print(df.tail())
print(df.describe())
print(df["marks"])
print(df[["marks", "name"]])