import tkinter as tk

# Functions
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

# Main Window
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("320x450")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

expression = ""
equation = tk.StringVar()

# Display
entry = tk.Entry(root, textvariable=equation, font=("Segoe UI", 22),
                 bg="#2d2d2d", fg="white", bd=0, justify='right')
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", ipady=15, padx=5, pady=5)

# Configure grid (IMPORTANT FIX)
for i in range(6):  # rows
    root.rowconfigure(i, weight=1)

for j in range(4):  # columns
    root.columnconfigure(j, weight=1)

# Button creator
def create_button(text, row, col, bg, command):
    tk.Button(root, text=text, font=("Segoe UI", 14),
              bg=bg, fg="white", bd=0,
              activebackground="#5a5a5a",
              command=command)\
        .grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Colors
btn_bg = "#3c3f41"
operator_bg = "#ff9500"
equal_bg = "#34c759"
clear_bg = "#ff3b30"

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

for (text, row, col) in buttons:
    if text in ['/', '*', '-', '+']:
        create_button(text, row, col, operator_bg, lambda t=text: press(t))
    elif text == '=':
        create_button(text, row, col, equal_bg, equalpress)
    else:
        create_button(text, row, col, btn_bg, lambda t=text: press(t))

# Clear Button (Full Width Properly)
tk.Button(root, text='C', font=("Segoe UI", 14),
          bg=clear_bg, fg="white", bd=0,
          activebackground="#ff5c5c",
          command=clear)\
    .grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

root.mainloop()