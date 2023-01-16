import os
from tkinter import *

root = Tk()
root.title("Untitled - Windows Notepad")  # title of program
root.geometry("640x480")  # window size

filename = "mynote.txt"


def open_file():
    if os.path.isfile(filename):  # if file is exist returns True if not returns False
        with open(filename, "r", encoding="utf8") as file:  # "r" => readonly
            txt.delete("1,0", END)  # ("1,0", END) -> start and end point
            txt.insert(END, file.read())


def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))  # get all values


menu = Menu(root)

# File menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save All", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

# Edit Menu, View, Help
menu.add_cascade(label="Edit")
menu.add_cascade(label="View")
menu.add_cascade(label="Help")

# Scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# Main
txt = Text(root, yscrollcommand=scrollbar.set)  # mapping text to scroll bar
txt.pack(side="left", fill="both", expand=True)  # expand=True , fill full page
scrollbar.config(command=txt.yview)  # mapping scrollbar to text

root.config(menu=menu)
root.mainloop()
