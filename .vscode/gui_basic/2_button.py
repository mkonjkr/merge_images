from tkinter import *

root = Tk()
root.title("Merge Images")  # title of program

btn1 = Button(root, text="Button1")
btn1.pack()  # adding the btn1 on the window

btn2 = Button(root, padx=5, pady=10, text="Button2")
btn2.pack()

# padx, pady -> kind of margin?
btn3 = Button(root, padx=10, pady=5, text="Button3")
btn3.pack()

# width, height -> fixed size
btn4 = Button(root, width=10, height=3, text="Button4")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="Button5")
btn5.pack()

""" photo = PhotoImage(file="gui_basic/img.png")
btn6 = Button(root, image=photo)
btn6.pack()
 """


def btncmd():
    print("Btn7 is clicked")


btn7 = Button(root, text="Btn7", command=btncmd)
btn7.pack()

root.mainloop()
