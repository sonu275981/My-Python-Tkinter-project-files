# this program is use for print image in python
from tkinter import *
from PIL import Image,ImageTk
cat = Tk()
cat.geometry("400x400")
cat.minsize(300,300)
cat.maxsize(500,500)
# method no 1
# Phot = PhotoImage(file="as.png")
# pic = Label(image=Phot).pack()
# method no 2 by insalling pillow used to display jpg image
ima = Image.open("tour3.jpg")
photo = ImageTk.PhotoImage(ima)
labb = Label(image= photo).pack()


# width height
nam = Label(cat,text="sonu is good boy").place(x=140,y=60)
but = Button(text="click me",bg="pink",activebackground="blue", activeforeground="red").place(x=160,y=100)
cat.mainloop()
