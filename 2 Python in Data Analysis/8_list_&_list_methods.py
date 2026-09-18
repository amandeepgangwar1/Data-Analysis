names = ["Amandeep", "Anand", "Anjul", "Manas"]
elements = [1, 2, 3, 4, True, False]

print(names)
print(type(names))

print(elements[0])
print(elements[1])

print(elements[1:4])
print(elements[1:-1])
print(type(elements))
print(len(elements))

elements[2] = 69
print(elements)



print("__________List Methods__________")

items = ["apple", "banana", "orange", "banana"]
print(items)
items[1] = "lichi"
print(items)

print(len(items))

items.append("stawberries")
print(items)

items.insert(1, "guava")
print(items)

items.extend(["more bananas", "pineapple"])
print(items)

items.remove("orange")
print(items)

items.pop(4)
print(items)

print(items.index("lichi"))
print(items)

print(items.count("banana"))
print(items)

items.clear()
print(items)


num = [11, 1, 4, 5, 55, 78, 2, 9]
num.sort()
print(num)

num.sort(reverse=True)
print(num)

print(11 in num)
print(22 in num)
