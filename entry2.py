from tkinter import *

def sk():
 s1 = s.get()
 print(s1)
root = Tk()
s = StringVar()

en = Entry(root,variable= s).pack()
s.set("sonu")
button = Button(root,text="click me",command = sk).pack()
root.geometry("400x400")
root.mainloop()
