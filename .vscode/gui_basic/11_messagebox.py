import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Merge Images")  # title of program
root.geometry("640x480")  # window size

# train booking


def info():
    msgbox.showinfo("Alert", "Your booking is completed")


def warn():
    msgbox.showwarning("Warning", "It's already sold by another user")


def error():
    msgbox.showerror("Error", "Payment Error")


def okcancel():
    msgbox.askokcancel("OK / CANCEL", "You selected a premium seat")


def retrycancel():
    msgbox.askretrycancel("RETRY / CANCEL", "Temp error, You want to retry?")


def yesno():
    msgbox.askyesno("YES / NO", "You selected a comfort seat")


def yesnocancel():
    response = msgbox.askyesnocancel(
        title=None, message="You want to save the info?")
    # yes: save and close
    # no: close without saveing
    # cancel: cancel closing
    print("Response:", response)  # True, False, None -> yes 1 no 0 etc
    if response == 1:
        print("Yes")
    elif response == 0:
        print("No")
    else:
        print("Cancel")


Button(root, command=info, text="Alert").pack()
Button(root, command=warn, text="Warning").pack()
Button(root, command=error, text="Error").pack()
Button(root, command=okcancel, text="OK Cancel").pack()
Button(root, command=retrycancel, text="Retry Cancel").pack()
Button(root, command=yesno, text="YES NO").pack()
Button(root, command=yesnocancel, text="YES NO CANCEL").pack()

root.mainloop()
