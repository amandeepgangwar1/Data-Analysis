def greet(fname, lname):
    print("Good Morning!", fname, lname)
    print("How are you!")
    print("Thank You!")
greet("Amandeep", "Gangwar")
greet("Anjul", "Verma")


def add (a, b):
    # print(a+b)
    return a+b
c = add(4, 6)
print(c)



print("__________Default Value Function__________")

def greet(name = "User"):
    print("Hello!", name)
greet()
greet("Aman")



print("__________Keyword Value Function__________")

def greet(name = "User", city = "Delhi"):
    print("Hello!", name, city)
greet()
greet("Amandeep")
greet(city = "Delhi", name= "Amandeep")
