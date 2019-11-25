from tkinter import *



root = Tk()
root.title("window resize")
root.geometry("400x400")

def resize():
    hgt = height.get()
    wdt = width.get()
    root.geometry(f"{wdt}x{hgt}")
Label(root, text = "Enter lenght of window", font = "comicsansms 11").place(x = 120, y = 20)
Label(root, text = "width:", font = "comicsansms 11").place(x = 110, y = 80)
Label(root, text = "Height:", font = "comicsansms 11").place(x = 110, y = 120)

height = StringVar()
width = StringVar()

Entry(root, bg = "yellow", textvariable = height).place(x = 190, y = 123)
Entry(root, bg = "yellow", textvariable = width).place(x = 190, y = 83)
Button(root, text = "click me", bg = "red", command = resize).place(x = 180, y = 180)
root.mainloop()