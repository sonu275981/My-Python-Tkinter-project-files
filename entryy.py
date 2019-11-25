from tkinter import *
# here we also learn grid
# variable classes in tkinter given below :-
# 1: booleanvar 2: doublevar 3: IntVar 4: StringVar
def hiii():
 print(u.get())
 print(p.get())

root = Tk()
root.geometry("400x400")
name = Label(root,bg="pink",text="username").grid()
password = Label(root,bg="pink",text="password").grid(row=2)

u = StringVar()
p =StringVar()
entrname = Entry(root,bg="pink",textvariable = u).grid(row = 0,column = 5)
passw = Entry(root,bg="pink",textvariable = p).grid(row = 2,column = 5)
btn = Button(root,bg="red",text="click me",command = hiii).grid(row = 6,column = 5)

root.mainloop()