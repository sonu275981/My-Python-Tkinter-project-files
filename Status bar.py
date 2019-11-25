from tkinter import *

root = Tk()
root.title("Status bar")
root.geometry("400x400")
status = StringVar()
status.set("ready")
sbar = Label(root,textvariable = status, relief = SUNKEN, anchor = W)
sbar.pack(side = BOTTOM, fill = X)

root.mainloop()