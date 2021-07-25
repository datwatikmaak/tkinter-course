from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("img/python.ico")

# frame = LabelFrame(root, text="This is my frame", padx=15, pady=15)
frame = LabelFrame(root, padx=15, pady=15)
frame.pack(padx=10, pady=10)

button1 = Button(frame, text="Don’t click here!")
button2 = Button(frame, text="And don’t click here!")

button1.grid(row=0, column=0)
button2.grid(row=1, column=1)


root.mainloop()
