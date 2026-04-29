from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Salary Calculator")
root.geometry("500x400")
root.config(bg="#0f172a")

# ===== TITLE =====
Label(
    root,
    text="SALARY CALCULATOR",
    font=("Arial", 18, "bold"),
    bg="#0f172a",
    fg="white"
).pack(pady=20)

# ===== CARD FRAME =====
frame = Frame(root, bg="white", padx=25, pady=25)
frame.pack(pady=10)

def calculate():
    try:
        wage = float(daily_wage.get())
        days = int(working_days.get())
        total = wage * days
        result.config(text=f"Total Salary: Rs {total}")
    except:
        messagebox.showerror("Error", "Enter valid numbers")

def clear():
    daily_wage.delete(0, END)
    working_days.delete(0, END)
    result.config(text="")

# ===== INPUTS =====
Label(frame, text="Daily Wage", bg="white", font=("Arial", 11)).grid(row=0, column=0, pady=10)
Label(frame, text="Working Days", bg="white", font=("Arial", 11)).grid(row=1, column=0, pady=10)

daily_wage = Entry(frame, width=25)
working_days = Entry(frame, width=25)

daily_wage.grid(row=0, column=1)
working_days.grid(row=1, column=1)

# ===== BUTTONS =====
btn_frame = Frame(root, bg="#0f172a")
btn_frame.pack(pady=15)

Button(btn_frame, text="Calculate", command=calculate, bg="#3b82f6", fg="white", width=12).grid(row=0, column=0, padx=10)
Button(btn_frame, text="Clear", command=clear, bg="#f59e0b", fg="white", width=12).grid(row=0, column=1, padx=10)

result = Label(root, text="", font=("Arial", 14, "bold"), bg="#0f172a", fg="white")
result.pack(pady=10)

root.mainloop()