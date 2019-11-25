from tkinter import *
# this is only for non drop down menu
root = Tk()
root.geometry("500x500")
root.title("Menu submenu")

def myfunc():
    print("sonu loves mango")

mymenu = Menu(root)
mymenu.add_command(label = "file" ,command = myfunc)
mymenu.add_command(label = "exit", command = quit)
root.config(menu = mymenu)
root.mainloop()