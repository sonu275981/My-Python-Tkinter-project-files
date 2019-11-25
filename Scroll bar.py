from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("List box")
root.geometry("400x400")
Scrollbar = Scrollbar(root)
Scrollbar.pack(side = RIGHT, fill = Y)

lst = Listbox(root, yscrollcommand = Scrollbar.set )

def value():
    lst.insert(END, f"{str.get()}")
    # messagebox.showinfo("value inserted", f"{str.get()} is inserted")
lst.insert(END, "python")
lst.insert(END, "java")
lst.insert(END, "javascript")
lst.insert(END, "book")
lst.insert(END, "car")
lst.insert(END, "truck")
lst.insert(END, "rail")
lst.insert(END, "aeroplane")
lst.insert(END, "ship")
lst.pack()
str = StringVar()

Label(root, text = "Enter your value").pack()
ent = Entry(root, textvariable = str).pack()
btn = Button(root, text = "Submit", command = value).pack()
Scrollbar.config(command = lst.yview)
root.mainloop()