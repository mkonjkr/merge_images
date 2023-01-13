from tkinter import *

root = Tk()
root.title("Merge Images")  # title of program
root.geometry("640x480")  # window size

Label(root, text="select menu").pack()

burger_var = IntVar()  # save as int
btn_burger1 = Radiobutton(root, text="Hamburger", value=1, variable=burger_var)
btn_burger1.select()  # default selecting
btn_burger2 = Radiobutton(root, text="Cheese burger",
                          value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="Chicken burger",
                          value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="select a drink").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="Coke", value="Coke", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(
    root, text="Sprite", value="Sprite", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(burger_var.get())  # print a selected value
    print(drink_var.get())


btn = Button(root, text="Order", command=btncmd)
btn.pack()

root.mainloop()
