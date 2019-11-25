from tkinter import *
root = Tk()
root.geometry("655x333")


f2 = Frame(root,bg="red",borderwidth=6,relief=SUNKEN)
f2.pack(side =LEFT, anchor="nw")

b1 = Button(f2,text="click me",fg="blue",bg="yellow").pack(side =LEFT,padx=15)
b2 = Button(f2,text="click me",fg="blue",bg="yellow").pack(side =LEFT,padx=15)
b3 = Button(f2,text="click me",fg="blue",bg="yellow").pack(side =LEFT,padx=15)
b4 = Button(f2,text="click me",fg="blue",bg="yellow").pack(side =LEFT,padx=15)




root.mainloop()