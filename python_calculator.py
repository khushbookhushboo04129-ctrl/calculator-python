import tkinter as tk
import math

root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("320x500")
root.config(bg="#f5f5f5")  # light background
root.resizable(False, False)

# Entry
entry = tk.Entry(root, font=("Arial", 22), bg="white", fg="black",
                 borderwidth=2, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=10)

# Functions
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        exp = entry.get()
        exp = exp.replace("log", "math.log10")
        exp = exp.replace("√", "math.sqrt")
        result = eval(exp)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Buttons
buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','=','+'],
    ['%','log','√','x²']
]

frame = tk.Frame(root, bg="#f5f5f5")
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame, bg="#f5f5f5")
    row_frame.pack(expand=True, fill="both")

    for btn in row:
        if btn == "=":
            action = calculate
            color = "#4CAF50"  # green
        elif btn == "C":
            action = clear
            color = "red"
        elif btn == "%":
            action = lambda: click("/100")
            color = "#2196F3"
        elif btn == "x²":
            action = lambda: click("**2")
            color = "#2196F3"
        else:
            action = lambda x=btn: click(x)
            color = "#e0e0e0"

        tk.Button(
            row_frame, text=btn, font=("Arial", 14),
            bg=color, fg="black",
            command=action
        ).pack(side="left", expand=True, fill="both", padx=3, pady=3)

# Clear button
tk.Button(root, text="C", font=("Arial", 16),
          bg="red", fg="white",
          command=clear).pack(fill="both", padx=10, pady=5)

root.mainloop()
