from tkinter import *
# this is only for  drop down menu
root = Tk()
root.geometry("500x500")
root.title("Menu submenu")

def myfunc():
    print("sonu loves mango")

mainmenu = Menu(root)
mymenu = Menu(mainmenu)
mymenu.add_command(label = "New file", command = myfunc)
mymenu.add_command(label = "open", command = myfunc)
mymenu.add_separator()
mymenu.add_command(label = "save", command = myfunc)
mymenu.add_command(label = "print", command = myfunc)
mymenu.add_separator()
mymenu.add_command(label = "exit", command = quit)
root.config(menu = mainmenu)
mainmenu.add_cascade(label = "main Tmenu", menu = mymenu)
root.mainloop()