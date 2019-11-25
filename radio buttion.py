from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("radio button")
root.geometry("400x400")
def chw():
    print(f"{sar.get()}")
    messagebox.showinfo("value submited", f"You selected {sar.get()}")

sar = StringVar()
sar.set("radio")

Label(root, text = "choose your language given below", font = "comicsons 12 bold", fg = "red").place(x = 65, y = 30)
radio = Radiobutton(root, variable = sar, value = "c", text = "C", font = "comicsons 12 bold")
radio.place(x = 120, y = 60)
radio = Radiobutton(root, variable = sar, value = "Java", text = "Java", font = "comicsons 12 bold")
radio.place(x = 120, y = 100)
radio = Radiobutton(root, variable = sar, value = "Python", text = "Python", font = "comicsons 12 bold")
radio.place(x = 120, y = 140)
radio = Radiobutton(root, variable = sar, value = "Android", text = "Android", font = "comicsons 12 bold")
radio.place(x = 120, y = 180)
btn = Button(root, text = "Submit", font = "comicsons 12 bold", fg = "blue", command = chw )
btn.place(x = 140, y = 220)

root.mainloop()