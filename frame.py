from tkinter import *
root = Tk()
root.geometry("655x333")
f1 = Frame(root,bg="red",borderwidth=6,relief=SUNKEN)
f1.pack(side =LEFT, fill="y")

f2 = Frame(root,bg="red",borderwidth=6,relief=SUNKEN)
f2.pack(side =TOP, fill="x")


l2 = Label(f1,text="how r u - sonu don",font="Helvetica 10 bold",bg="yellow",fg="blue").pack(pady=145)

l3 = Label(f2,text="welcom to python",font="Helvetica 15 bold",bg="yellow",fg="blue").pack()


root.mainloop()