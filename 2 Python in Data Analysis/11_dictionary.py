student = {
    "name" : "Amandeep",
    "city" : "Tilhar",
    "company" : "Meta"
}
print(student)
print(type(student))

print(student["company"])
# print(student["nameeee"])    # Throws an error

print(student.get("nameeee"))   # Not throws an error
print(student.get("name"))

student["city"] = "Delhi"
print(student)



print("__________Dictionary Methods__________")

stu = {
    "name" : "Aman",
    "city" : "Tilhar",
    "company" : "Meta"
}
print(stu.keys())
print(stu)

print(stu.values())
print(stu)

print(stu.items())       # Returns in form of tuple
print(stu)

stu.pop("name")
print(stu)

stu["class"] = "12th"
print(stu)

stu.popitem()
print(stu)

del stu["city"]
print(stu)

stu.clear()
print(stu)