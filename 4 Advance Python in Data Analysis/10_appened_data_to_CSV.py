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

# df.to_csv('orders.csv', mode = "a", header = True, index = False)                   # to show heading
df.to_csv('orders.csv', mode = "a", header = False, index = False)