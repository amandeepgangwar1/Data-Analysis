a = "Amandeep is Good"

file = open("C:/Users/amand/Desktop/Data Analysis/Python in Data Analysis/File-IO in Python/aman.txt", "w")
file.write(a)

file = open("C:/Users/amand/Desktop/Data Analysis/Python in Data Analysis/File-IO in Python/robot.txt", "r")
# content = file.read()
content = file.readlines()
print(content)

file.close()