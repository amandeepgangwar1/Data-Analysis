import pandas as pd


# Generate a dataframe of e-commerce order
df = pd.DataFrame({
    'order_id' : [1001, 1002, 1003, 1004],
    'customer_id' : [501, 502, 503, 504],
    'order_amount' : [239.45, 89.10, 150.11, 500.12],
    'order_date' : ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18'],
    'customer_name' : ['Aman', 'Ram', 'Om', 'Sai'],
    'customer_country' : ['USA', 'Canada', 'India', 'USA']
})

# Create dataframe of products
df2 = pd.DataFrame({
    'product_id' : [1, 2, 3, 4],
    'product_name' : ['Laptop', 'Phone', 'Tablet', 'Mouse'],
    'price' : [73900.45, 89400.10, 150000.11, 500.12],
})
print(df)

# df.to_csv('ecommerce_orders.csv')                   Ek extra row add ho jati hai
df.to_csv('ecommerce_orders.csv', index = False)
df.to_excel('ecommerce_orders.xlsx', index = False)

with pd.ExcelWriter('ecommerce.xlsx') as writer:
    df.to_excel(writer,sheet_name='orders', index = False)
    df2.to_excel(writer,sheet_name='products', index = False)