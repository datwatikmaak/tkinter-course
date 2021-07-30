from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Radio Buttons")
root.iconbitmap("img/python.ico")


# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

# def popup():
#     messagebox.showinfo("Info", "Hello World")
#     messagebox.showwarning("Warning", "This is a warning!")
#     messagebox.showerror("Error", "This is an error message!")
#     messagebox.askquestion("Question", "May I ask you a question?")
#     messagebox.askokcancel("Ok or Cancel", "This is a little reminder.")
#     messagebox.askyesno("Yes or No", "Do you want to run this popup again?")


def popup():
    response = messagebox.askyesno("This is a popup", "Hello World")
    if response == 1:
        Label(root, text="You clicked Yes").pack()
    else:
        Label(root, text="You clicked No").pack()


Button(root, text="Popup", command=popup).pack()

mainloop()
