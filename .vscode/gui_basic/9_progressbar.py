import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Merge Images")  # title of program
root.geometry("640x480")  # window size

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
""" progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
progressbar.start(10)  # 10ms
progressbar.pack()


def btncmd():
    progressbar.stop()


btn = Button(root, text="Stop", command=btncmd)
btn.pack() """

p_var2 = DoubleVar()
progress_bar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progress_bar2.pack()


def btncmd2():
    for i in range(1, 101):  # 1~100
        time.sleep(0.01)  # wait for 0.01s

        p_var2.set(i)  # set progress bar's value
        progress_bar2.update()  # update for every i
        print(p_var2.get())  # show percentage


btn = Button(root, text="Start", command=btncmd2)
btn.pack()


root.mainloop()
