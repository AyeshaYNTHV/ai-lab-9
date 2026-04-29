from tkinter import *
from tkinter import ttk

import subprocess
import sys

root = Tk()
root.title("HR Management System")
root.geometry("500x400")
root.config(bg="#1e1e2f")

# ===== TITLE =====
title = Label(
    root,
    text="Employee Registration & Salary System",
    font=("Arial", 16, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=20)

# ===== FUNCTIONS =====
def open_employee():
    subprocess.run([sys.executable, "employee_form.py"])

def open_salary():
    subprocess.run([sys.executable, "salary_calculator.py"])

def exit_app():
    root.destroy()

# ===== BUTTON STYLE =====
style = {
    "font": ("Arial", 12, "bold"),
    "width": 25,
    "pady": 10
}

# ===== BUTTONS =====
Button(root, text="Employee Registration", command=open_employee, bg="#4CAF50", fg="white", **style).pack(pady=10)
Button(root, text="Salary Calculator", command=open_salary, bg="#2196F3", fg="white", **style).pack(pady=10)
Button(root, text="Exit System", command=exit_app, bg="red", fg="white", **style).pack(pady=10)

root.mainloop()