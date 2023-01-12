from tkinter import *

root = Tk()
root.title("Merge Images")  # title of program
root.geometry("640x480")  # window size

# "extended": can select multiple items, "single": only can select one item
# height = 0 : shows all lists, height = 2 : shows only 2 items
listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "Apple")
listbox.insert(1, "Strawberry")
listbox.insert(2, "Banana")
listbox.insert(END, "Watermelon")
listbox.insert(END, "Grape")
listbox.pack()


def btncmd():
    # delete the last item
    # listbox.delete(END)

    # item qty
    # print("we have ", listbox.size(), "items in the list")

    # check item (start, end)
    # print("from 1 to 3 items", listbox.get(0, 2))

    # check selected item
    print("Selected: ", listbox.curselection())


btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()
