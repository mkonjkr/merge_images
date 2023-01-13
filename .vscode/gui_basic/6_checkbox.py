from tkinter import *

root = Tk()
root.title("Merge Images")  # title of program
root.geometry("640x480")  # window size

chkvar = IntVar()  # will save a value to chkvar as intr
chkbox = Checkbutton(root, text="Don't show this popup today", variable=chkvar)
# chkbox.select() # auto selection
# chkbox.deselect() # uncheck
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="Don't show for a week", variable=chkvar2)
chkbox2.pack()


def btncmd():
    print(chkvar.get())  # 0: unchecked, 1: checked


btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()
