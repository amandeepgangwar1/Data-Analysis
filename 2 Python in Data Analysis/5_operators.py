print("__________Arithmetic Operators__________")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2
print("Sum: ", sum)

sub = num1 - num2
print("Subtraction: ", sub)

mul = num1 * num2
print("Product: ", mul)

div = num1 / num2
print("Division: ", div)

f_div = num1 // num2
print("Floor Division: ", f_div)

rem = num1 % num2
print("Modulus: ", rem)

pow = num1 ** num2
print("Exponentiation: ", pow)



print("___________Comparision Operator__________")

num3 = int(input("Enter first number: "))
num4 = int(input("Enter second number: "))

print(num3 == num4)
print(num3 != num4)
print(num3 > num4)
print(num3 < num4)
print(num3 >= num4)
print(num3 <= num4)



print("___________Assignment Operator__________")

num5 = int(input("Enter first number: "))
num6 = int(input("Enter second number: "))

num5 += num6
print("After += :", num5)

num5 -= num6
print("After -= :", num5)

num5 *= num6
print("After *= :", num5)

num5 /= num6
print("After /= :", num5)



print("___________Logical Operator__________")

num7 = int(input("Enter first number: "))
num8 = int(input("Enter second number: "))

print((num7 > num8) and (num7 < num8))

print((num7 > num8) or (num7 < num8))

print(not (num7 < num8))



print("___________Membership Operator__________")

fruits = ["Apple", "Banana"]

print("Apple" in fruits)

print("Banana" not in fruits)



print("___________Identity Operator__________")

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
c = a

print(a == b)
print(a is b)
print(a is c)
