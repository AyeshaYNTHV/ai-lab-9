from tkinter import *
from tkinter import messagebox
import re

root = Tk()
root.title("Employee Registration Form")
root.geometry("400x300")

def submit():
    first = first_name.get()
    last = last_name.get()
    email = email_address.get()
    dept = department.get()

    if first == "" or last == "" or email == "" or dept == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    if first.isnumeric() or last.isnumeric():
        messagebox.showerror("Error", "Names cannot be numbers!")
        return

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        messagebox.showerror("Error", "Invalid Email!")
        return

    messagebox.showinfo("Success", "Employee Registered!")

Label(root, text="First Name").grid(row=0, column=0)
Label(root, text="Last Name").grid(row=1, column=0)
Label(root, text="Email").grid(row=2, column=0)
Label(root, text="Department").grid(row=3, column=0)

first_name = Entry(root)
last_name = Entry(root)
email_address = Entry(root)
department = Entry(root)

first_name.grid(row=0, column=1)
last_name.grid(row=1, column=1)
email_address.grid(row=2, column=1)
department.grid(row=3, column=1)

Button(root, text="Submit", command=submit, bg="lightgreen").grid(row=4, column=1)

root.mainloop()
