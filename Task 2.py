import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        else:
            raise ValueError("Invalid operation selected.")
        
        result_label.config(text=f"Result: {result}")
    except ValueError as e:
        messagebox.showerror("Input error", f"Invalid input: {e}")
root = tk.Tk()
root.title("Simple Calculator")

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

label1 = tk.Label(root, text="Number 1:")
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = tk.Label(root, text="Number 2:")
label2.grid(row=1, column=0, padx=10, pady=10)

operation_var = tk.StringVar(root)
operation_var.set("+")  # default value

operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=1, padx=10, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=1, padx=10, pady=10)


root.mainloop()
