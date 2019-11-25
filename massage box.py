# here we learn about different element of massage box for full goto javatpoint
from tkinter import *
from tkinter import messagebox
# this is only for  drop down menu
root = Tk()
root.geometry("500x500")
root.title("Menu submenu")

def myfunc():
    print("sonu loves mango")

def box():
    messagebox.showinfo("New file", "New file created")

def qus():
    print("rate us")
    value = messagebox.askquestion("open file ??", "Are you open your file")
    print(value)

def warning():
    messagebox.showwarning("Save file ??", "Are you save your file")


mainmenu = Menu(root)
mymenu = Menu(mainmenu)
mymenu.add_command(label = "New file", command = box)
mymenu.add_command(label = "open", command = qus)
mymenu.add_separator()
mymenu.add_command(label = "save", command = warning)
mymenu.add_command(label = "print", command = myfunc)
mymenu.add_separator()
mymenu.add_command(label = "exit", command = quit)
root.config(menu = mainmenu)
mainmenu.add_cascade(label = "main menu", menu = mymenu)
root.mainloop()