import pandas as pd

# df = pd.read_csv('data.csv', skiprows = 2)              # to skip the unwanted rows from the data
# df = pd.read_csv('data.csv', skipcols = 2)              # to skip the unwanted columns from the data

df = pd.read_csv('data.csv')
print(df)

# Select all delivered order
delivered_orders = df[df['order_status'] == 'Delivered']
print(delivered_orders)

delivered_orders = df[(df['order_status'] == 'Delivered') & (df['city'] == 'Bangalore')]
print(delivered_orders)



df2 = pd.read_excel('Random Data Generator.xlsx', sheet_name='Sheet2')    #, usecols=['ID', 'Name', 'Country'])
print(df2)
print(pd.ExcelFile('Random Data Generator.xlsx').sheet_names)