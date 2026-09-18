print("__________Local Variable__________")

def show_value():
    x = 11          # Local Variable
    print(x)
show_value()

x = 78              # Global Variable
show_value()



print("__________Global Variable__________")

y = 78              # Global Variable
def show_val():
    # global y
    y = 22
    print(y)
show_val()
show_val()
print(y)