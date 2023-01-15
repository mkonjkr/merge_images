from tkinter import *

root = Tk()
root.title("Merge Images")  # title of program
root.geometry("640x480")  # window size

Label(root, text="Select your menu").pack(side="top")
Button(root, text="Order").pack(side="bottom")

# Burger Frame
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="Hamburger").pack()
Button(frame_burger, text="Cheese burger").pack()
Button(frame_burger, text="Chicken burger").pack()

# Drink Frame
frame_drink = LabelFrame(root, text="Drink")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="Coke").pack()
Button(frame_drink, text="Sprite").pack()


root.mainloop()
