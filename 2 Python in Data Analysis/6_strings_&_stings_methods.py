name = "Amandeep"

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])

poem = '''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.'''

print(poem)
print(poem[0])


# name[0] = "S" # This is not allowed


print("__________Methods in String__________")

print(len(name))
print(name.lower())
print(name.upper())
print(len(name.strip()))    # Remove white space

print(name.replace("Ama", "San"))

print(name.isalpha())
print(name.isnumeric())



print("__________String Slicing__________")

print(name[0:5])
print(name[1:4])
print(name[-1:4])
print(name[2:-3])
