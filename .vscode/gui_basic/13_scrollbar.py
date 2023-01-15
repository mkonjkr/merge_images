from tkinter import *

root = Tk()
root.title("Merge Images")  # title of program
root.geometry("640x480")  # window size

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# if set doesn't exist
listbox = Listbox(frame, selectmode="extended",
                  height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32):
    listbox.insert(END, str(i) + "day")
listbox.pack(side="left")
scrollbar.config(command=listbox.yview)

root.mainloop()
