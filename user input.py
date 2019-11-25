from tkinter import *
# write user input data in a f string
def hiii():
 print(f"{u.get(),p.get()}")

# with open("record.txt", "a") as f:
 with open("records.txt","a") as f:
   # f.write(f"{u.get(),p.get()}\n")
  f.write(f"{u.get(),p.get()}\n")


root = Tk()
root.title("sonu user form")
root.geometry("400x400")
name = Label(root, bg = "pink", text = "username").grid()
password = Label(root, bg = "pink",  text = "password").grid(row = 2)

u = StringVar()
p = StringVar()
entrname = Entry(root,bg="pink",textvariable = u).grid(row = 0,column = 5)
passw = Entry(root,bg="pink",textvariable = p).grid(row = 2,column = 5)
btn = Button(root,bg="red",text="click me",command = hiii).grid(row = 6,column = 5)

root.mainloop()