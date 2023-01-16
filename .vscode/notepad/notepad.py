from tkinter import *

root = Tk()
root.title("Merge Images")  # title of program
root.geometry("640x480")  # window size


def create_new_file():
    print("create a new file")


menu = Menu(root)

# File menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_command(label="Open")
menu_file.add_command(label="Save All")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

menu.add_cascade(label="File", menu=menu_file)


root.config(menu=menu)
root.mainloop()
