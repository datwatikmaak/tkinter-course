from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer App")
root.iconbitmap("img/image.ico")

my_img_01 = ImageTk.PhotoImage(Image.open("img/beach-01.jpg"))
my_img_02 = ImageTk.PhotoImage(Image.open("img/beach-02.jpg"))
my_img_03 = ImageTk.PhotoImage(Image.open("img/blossom-01.jpg"))
my_img_04 = ImageTk.PhotoImage(Image.open("img/blossom-02.jpg"))
my_img_05 = ImageTk.PhotoImage(Image.open("img/blossom-03.jpg"))
my_img_06 = ImageTk.PhotoImage(Image.open("img/blossom-04.jpg"))

image_list = [my_img_01, my_img_02, my_img_03, my_img_04, my_img_05, my_img_06]

my_label = Label(image=my_img_01)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 6:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_quit = Button(root, text="Exit Program", padx=10, pady=5, command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
