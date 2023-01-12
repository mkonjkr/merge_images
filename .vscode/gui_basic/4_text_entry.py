from tkinter import *

root = Tk()
root.title("Merge Images")  # title of program
root.geometry("640x480")  # window size


txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "Enter your code")


e = Entry(root, width=30)  # can't enter Enter. only can type one line
e.pack()
e.insert(0, "Enter your one code")


def btncmd():
    # print values
    print(txt.get("1.0", END))  # from line 1 and column 0 to End
    print(e.get)

    # Delete values
    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()
