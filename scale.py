# here we lean about scale and take the output of scale
from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("scale in tkinter")

def take():
    print(f"{value.get()}")

#  for vertical slider default value is vertical
# scal = Scale(root, from_=0, to=100).pack()
# for horizental slider
# ***if you want to run scale in your format like 1,2,3,4 or 5,10,15,20,25 or 1,3,7,9 so use tickinterval it just show value below***
value = Scale(root, from_=0, to=100, bg = "yellow", orient = HORIZONTAL, tickinterval = 25)
value.pack()
# ******if you want to change initial value of scale means taking value than use than we use set()******
# value.set(35)
btn = Button(root, text = "Get money", pady = 5, bg = "red", font = "comicsansms 11", command = take).pack()
root.mainloop()