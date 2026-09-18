numbers = [1, 2, 3, 4, 5]

# squared = []
# for i in numbers:
#     squared.append(i*i)

squared = [i*i for i in numbers]
print(squared)



# It also uses for filtering...

num = [1, 2, 3, 4, 5, 6]

even = [i for i in num if i%2 == 0]
print(even)



# transform data...

names = [" Aman ", " Deep ", " SANYA "]
cleaned_data = [name.strip().lower() for name in names if name]

print(cleaned_data)



# Dictationary Comprehensions....

items = ["apple", "banana", "cherry"]
prices = [0.5, 0.3, 0.2]

dict1 = {items[i] : prices[i] for i in range(len(items))}
print(dict1)



# Set Comprehensions...

values = [1, 2, 3, 4, 5, 5]

unique_squares = {x*x for x in values}
print(unique_squares)



# Nested Comprehension...

pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs)
