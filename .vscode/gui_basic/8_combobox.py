import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Merge Images")  # title of program
root.geometry("640x480")  # window size

values = [str(i) + "day" for i in range(1, 32)]  # return 1 ~ 31
combobox = ttk.Combobox(root, height=5, values=values)  # allow to typing
combobox.pack()
combobox.set("date")  # name of the combobox

readonly_combobox = ttk.Combobox(
    root, height=10, values=values, state="readonly")  # readyonly
readonly_combobox.current(0)  # select 0 index
readonly_combobox.pack()


def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())


btn = Button(root, text="Select", command=btncmd)
btn.pack()

root.mainloop()
