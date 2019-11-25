from tkinter import *
# write user input data in a f string incomplete program

def hiii(event):
     print("you")

root = Tk()
root.title("Event")
root.geometry("400x400")

Widget = Button(root, text = "click me")
Widget.pack()

Widget.bind('<Button-1>', hiii)

root.mainloop()