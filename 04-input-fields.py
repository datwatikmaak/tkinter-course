import tkinter as tk

root = tk.Tk()

e = tk.Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name: ")


def my_click():
    message = f"Hello, {e.get()}"
    my_label = tk.Label(root, text=message)
    my_label.pack()


my_button = tk.Button(root, text="Get your message", command=my_click)
my_button.pack()

root.mainloop()
