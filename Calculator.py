from tkinter import *
# pack(side = LEFT, padx = 18, pady = 12)
root = Tk()
root.title("Calculator")
root.wm_iconbitmap("calculator.ico")
root.geometry("475x650")
root.maxsize(475,650)
root.minsize(475,650)
def click(event):
    global sc
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if sc.get().isdigit():
            value = int(sc.get())
        else:
            value = eval(ent.get())
            sc.set(value)
            ent.update()
    elif text == "c":
       sc.set("")
       ent.update()
    else:
        sc.set(sc.get()+text)
        ent.update()

sc = StringVar()
sc.set("")

ent = Entry(root, textvariable = sc, font = "lucida 40 bold", fg = "orange")
ent.pack(fill = X, ipadx = 8, padx = 10, pady = 10)

f1 = Frame(root, bg = "red",borderwidth=6,relief=SUNKEN).pack()

btn = Button(f1,text = "7", padx = 15, pady = 15, fg = "blue", bg = "red", font = "lucida 20 bold")
btn.place(x = 60, y = 100)
btn.bind("<Button-1>", click)

btn = Button(f1,text = "8", padx = 15, pady = 15, fg = "blue", bg = "red", font = "lucida 20 bold")
btn.place(x = 200, y = 100)
btn.bind("<Button-1>", click)

btn = Button(f1,text = "9", padx = 15, pady = 15, fg = "blue", bg = "red", font = "lucida 20 bold")
btn.place(x = 340, y = 100)
btn.bind("<Button-1>", click)

btn = Button(f1,text = "4", padx = 15, pady = 15, fg = "blue", bg = "red", font = "lucida 20 bold")
btn.place(x = 60, y = 210)
btn.bind("<Button-1>", click)

btn = Button(f1,text = "5", padx = 15, pady = 15, fg = "blue", bg = "red", font = "lucida 20 bold")
btn.place(x = 200, y = 210)
btn.bind("<Button-1>", click)

btn = Button(f1,text = "6", padx = 15, pady = 15, fg = "blue", bg = "red", font = "lucida 20 bold")
btn.place(x = 340, y = 210)
btn.bind("<Button-1>", click)

btn = Button(f1,text = "1", padx = 15, pady = 15, fg = "blue", bg = "red", font = "lucida 20 bold")
btn.place(x = 60, y = 320)
btn.bind("<Button-1>", click)

btn = Button(f1,text = "2", padx = 15, pady = 15, fg = "blue", bg = "red", font = "lucida 20 bold")
btn.place(x = 200, y = 320)
btn.bind("<Button-1>", click)

btn = Button(f1,text = "3", padx = 15, pady = 15, fg = "blue", bg = "red", font = "lucida 20 bold")
btn.place(x = 340, y = 320)
btn.bind("<Button-1>", click)

btn = Button(f1,text = "0", padx = 15, pady = 15, fg = "blue", bg = "red", font = "lucida 20 bold")
btn.place(x = 60, y = 430)
btn.bind("<Button-1>", click)

btn = Button(f1,text = "+", padx = 1, pady = 18, fg = "blue", bg = "red", font = "lucida 17 bold")
btn.place(x = 200, y = 433)
btn.bind("<Button-1>", click)

btn = Button(f1,text = "-", padx = 2, pady = 18, fg = "blue", bg = "red", font = "lucida 17 bold")
btn.place(x = 238, y = 433)
btn.bind("<Button-1>", click)

btn = Button(f1,text = "*", padx = 2, pady = 18, fg = "blue", bg = "red", font = "lucida 17 bold")
btn.place(x = 340, y = 433)
btn.bind("<Button-1>", click)

btn = Button(f1,text = "/", padx = 2, pady = 18, fg = "blue", bg = "red", font = "lucida 17 bold")
btn.place(x = 378, y = 433)
btn.bind("<Button-1>", click)

btn = Button(f1,text = "c", padx = 15, pady = 15, fg = "blue", bg = "red", font = "lucida 20 bold")
btn.place(x = 60, y = 540)
btn.bind("<Button-1>", click)

btn = Button(f1,text = "=", padx = 15, pady = 15, fg = "blue", bg = "red", font = "lucida 20 bold")
btn.place(x = 200, y = 540)
btn.bind("<Button-1>", click)

btn = Button(f1,text = "%", padx = 10, pady = 15, fg = "blue", bg = "red", font = "lucida 20 bold")
btn.place(x = 340, y = 540)
btn.bind("<Button-1>", click)

root.mainloop()