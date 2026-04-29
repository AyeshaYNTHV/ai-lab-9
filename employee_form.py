from tkinter import *
from tkinter import messagebox
import re

root = Tk()
root.title("Employee Registration")
root.geometry("500x450")
root.config(bg="#1f2937")  # dark background

# ===== TITLE =====
Label(
    root,
    text="EMPLOYEE REGISTRATION",
    font=("Arial", 18, "bold"),
    bg="#1f2937",
    fg="white"
).pack(pady=20)

# ===== CARD FRAME =====
frame = Frame(root, bg="white", padx=20, pady=20)
frame.pack(pady=10)

# ===== VALIDATION =====
def submit():
    first = first_name.get()
    last = last_name.get()
    email = email_address.get()
    dept = department.get()

    if first == "" or last == "" or email == "" or dept == "":
        messagebox.showerror("Error", "All fields required")
        return

    if first.isdigit() or last.isdigit():
        messagebox.showerror("Error", "Names cannot be numbers")
        return

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        messagebox.showerror("Error", "Invalid Email")
        return

    messagebox.showinfo("Success", "Employee Registered")

def clear():
    first_name.delete(0, END)
    last_name.delete(0, END)
    email_address.delete(0, END)
    department.delete(0, END)

# ===== INPUTS =====
def create_row(text, row):
    Label(frame, text=text, bg="white", font=("Arial", 11)).grid(row=row, column=0, pady=10, sticky=W)

create_row("First Name", 0)
create_row("Last Name", 1)
create_row("Email", 2)
create_row("Department", 3)

first_name = Entry(frame, width=30)
last_name = Entry(frame, width=30)
email_address = Entry(frame, width=30)
department = Entry(frame, width=30)

first_name.grid(row=0, column=1)
last_name.grid(row=1, column=1)
email_address.grid(row=2, column=1)
department.grid(row=3, column=1)

# ===== BUTTONS =====
btn_frame = Frame(root, bg="#1f2937")
btn_frame.pack(pady=20)

Button(btn_frame, text="Submit", command=submit, bg="#22c55e", fg="white", width=12).grid(row=0, column=0, padx=10)
Button(btn_frame, text="Clear", command=clear, bg="#f59e0b", fg="white", width=12).grid(row=0, column=1, padx=10)

root.mainloop()