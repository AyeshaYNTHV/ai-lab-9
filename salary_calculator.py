from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Salary Calculator")
root.geometry("400x250")

def calculate():
    try:
        wage = float(daily_wage.get())
        days = int(working_days.get())

        total = wage * days
        result.config(text=f"Total Salary: {total}")

    except:
        messagebox.showerror("Error", "Enter valid numbers")

def clear():
    daily_wage.delete(0, END)
    working_days.delete(0, END)
    result.config(text="")

# Labels
Label(root, text="Daily Wage").grid(row=0, column=0)
Label(root, text="Working Days").grid(row=1, column=0)

# Inputs
daily_wage = Entry(root)
working_days = Entry(root)

daily_wage.grid(row=0, column=1)
working_days.grid(row=1, column=1)

# Buttons
Button(root, text="Calculate", command=calculate).grid(row=2, column=0)
Button(root, text="Clear", command=clear).grid(row=2, column=1)

Button(root, text="Exit", command=root.destroy, bg="red").grid(row=3, column=1)

# Result
result = Label(root, text="")
result.grid(row=4, column=0, columnspan=2)

root.mainloop()
