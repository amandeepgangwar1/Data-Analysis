print("Initializing...")

a = int(input("Enter a: \n"))
b = int(input("Enter b: \n"))
try:
    print("The value of a/b is: ", a/b)
except Exception as e:
    print("Some error occured! - ", e)
print("Thank You...")



try:
    x = int(input("Enter a number: \n"))
    y = 10 / x
except ValueError:
    print("Please enter valid number")
except ZeroDivisionError:
    print("Division by zero is not allowed")
finally:
    print("I will always run...")