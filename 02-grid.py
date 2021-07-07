import tkinter as tk

root = tk.Tk()

# creating a label widget
myLabel1 = tk.Label(root, text="Hello World!")
myLabel2 = tk.Label(root, text="My name is Leonieke")

# placing the labels with the .grid()
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

root.mainloop()
