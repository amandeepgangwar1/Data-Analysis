import pandas as pd

df = pd.DataFrame({
    "Product Name": [" iPhone 14 ", "Samsung Galaxy", " OnePlus 11", "Pixel 7 ", None] * 200,
    "price": ["499", "799", "1199", "899", None] * 200,
    "category": ["Mobile", " mobile ", "ELECTRONICS", "Electronics ", None] * 200,
    "rating": [5, 4, None, 3, 2] * 200,
    "reviews": [1200, 3400, 560, 780, 150] * 200,
    "in_stock": ["Yes", "No", "yes ", " no", None] * 200,
    "launch_year": ["2023", "2022", "2021", "2020", None] * 200
})

# print(df)
# print(df["price"])
# print(df[["price", "reviews", "in_stock"]])
# print(df[df['in_stock']== "Yes"])
# print(df[df['reviews'] > 500])
# print(df[(df['reviews'] > 500) & (df['in_stock']== "Yes")])
# print(df.isna())
# print(df.isna().sum())
# print(df.dropna())
# df["rating"] = df["rating"].fillna(df["rating"].mean())
# print(df)
# print(df.dtypes)
# df["price"] = df["price"].astype(float)
df["category"] = df["category"].str.lower().str.strip()
print(df.head())