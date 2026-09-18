s1 = {1, 5, 6, 9, 12, 12}
s2 = set()  #Empty Set
print(s1)
print(type(s1))
print(s2)
print(type(s2))



print("__________Sets Method__________")

items = {"apple", "banana", "tomato"}

items.add("orange")
print(items)

items.update(["mango", "peach"])
print(items)

items.remove("tomato")
print(items)

items.discard("tomato")   # No Error
print(items)

items.pop()
print(items)

print(len(items))
items.clear()
print(items)



print("__________Sets Operation__________")

a = {1, 2, 4}
b = {3, 4, 5}

result = a.union(b)
print(result)

result = a.intersection(b)
print(result)