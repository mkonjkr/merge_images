import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Merge Images")  # title of program

# Add file


def add_file():
    # askopenfilenames -> allows to user select multiple files
    files = filedialog.askopenfilenames(title="Select image files", filetypes=(("PNG file", "*.png"), ("All files", "*.*")),
                                        initialdir="C:/")  # shows C:/ at the first time
    # shows user selected files
    for file in files:
        list_file.insert(END, file)

# Delete File


def delete_file():

    for index in reversed(list_file.curselection()):
        list_file.delete(index)


# Save path(folder)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':  # when user selects cancel button
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)


# File Frame (Add file, select delete)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12,
                      text="Add File", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12,
                      text="Delete", command=delete_file)
btn_del_file.pack(side="right")

# file list frame
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

# can see 15 files at once. if there are more can scroll down
list_file = Listbox(list_frame, selectmode="extended",
                    height=15, yscrollcommand=scrollbar.set)
# fill="both" -> fill extend to all way
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# Save path
path_frame = LabelFrame(root, text="Save Path")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
# ipad -> inner padding ipady=> height
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

btn_dest_path = Button(path_frame, text="find",
                       width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# Option frame
frame_option = LabelFrame(root, text="Option")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. Width option
# width label
lbl_width = Label(frame_option, text="Width", width=8)
lbl_width.pack(side="left")

# width combo
opt_width = ["Original", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly",
                         values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. margin?
# margin option label
lbl_space = Label(frame_option, text="Space", width=8)
lbl_space.pack(side="left")


# magin option combo
opt_space = ["None", "Small", "Medium", "Large"]
cmb_space = ttk.Combobox(frame_option, state="readonly",
                         values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 3. File Format option

# file format option label
lbl_format = Label(frame_option, text="Format", width=8)
lbl_format.pack(side="left", padx=5, pady=5)


# file format option combo
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly",
                          values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# Progress bar
frame_progress = LabelFrame(root, text="Progress")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# Start and Close
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="Close",
                   width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5,
                   text="Start", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(False, False)  # can't adjust window size
root.mainloop()
