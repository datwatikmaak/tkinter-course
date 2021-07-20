from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn To Code")
root.iconbitmap("img/python.ico")

my_img = ImageTk.PhotoImage(Image.open("img/tkinter.jpg"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", padx=10, pady=5, command=root.quit)
button_quit.pack()

root.mainloop()
