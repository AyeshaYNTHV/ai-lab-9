from tkinter import *

root = Tk()
root.title("HR Notice Window")
root.geometry("600x300")

label1 = Label(root, text="NORTH", bg="red")
label1.grid(row=0, column=0, sticky=N)

label2 = Label(root, text="EAST", bg="green")
label2.grid(row=1, column=0, sticky=E)

label3 = Label(root, text="SOUTH", bg="blue")
label3.grid(row=2, column=0, sticky=S)

label4 = Label(root, text="WEST", bg="yellow")
label4.grid(row=3, column=0, sticky=W)

root.mainloop()
