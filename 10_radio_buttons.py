from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Radio Buttons")
root.iconbitmap("img/python.ico")

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]


def clicked(value):
    my_label = Label(root, text=value).pack()
    my_label.pack()


pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

my_button = Button(root, text="Click Me!", command=lambda: clicked(pizza.get())).pack()

mainloop()
