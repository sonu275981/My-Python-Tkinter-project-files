from tkinter import *
from tkinter import messagebox
# you can make text book also by using text method
root = Tk()
root.title("List box")
root.geometry("400x400")

lst = Listbox(root)
lst.pack()
def value():
    lst.insert(END, f"{str.get()}")
    # lst.insert(ACTIVE, f"{str.get()}")
    messagebox.showinfo("value inserted", f"{str.get()} is inserted")
lst.insert(END, "python")
lst.insert(END, "java")
lst.insert(END, "javascript")
lst.insert(END, "html")
# here End means last and Active means above on selected vlaue and if you not select any value than inserted on top
str = StringVar()

Label(root, text = "Enter your value").pack()
ent = Entry(root, textvariable = str).pack()
btn = Button(root, text = "Submit", command = value).pack()
root.mainloop()