# canvas and component
from tkinter import *
root = Tk()
root.title("my canvas")
root.geometry("600x600")
can = Canvas(root, height = "550", width = "550", bg = "yellow").pack()
can.create_line(0, 200, 800, 0)
can.create_arc((5,10,150,200),start = 0,extent = 150, fill= "white")
root.mainloop()