from tkinter import *

root = Tk()
root.title("Merge Images")  # title of program
root.geometry("640x480")

label1 = Label(root, text="Hello")
label1.pack()

# photo = PhotoImage(file="gui_basic/img.png")
# label2 = Label(root, image=photo)
# label2.pack()


def change():
    label1.config(text="Bye!")
    # global photo2
    # photo2 = PhotoImage(file="gui_basic/img2.png")
    # label2.config(image=photo2)


btn = Button(root, text="click", command=change)
btn.pack()

root.mainloop()
