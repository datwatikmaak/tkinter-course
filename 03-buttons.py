import tkinter as tk

root = tk.Tk()


def my_click():
    my_label = tk.Label(root, text="Look! I clicked a button!")
    my_label.pack()


my_button = tk.Button(root, text="Click Me!", padx=50, pady=10, command=my_click, fg="blue", bg="green")
my_button.pack()

root.mainloop()
