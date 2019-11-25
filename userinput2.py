from tkinter import *
root = Tk()
root.geometry("532x335")
root.title("Shivam GYM")


simple = Label(root, text="Welcome to Shivam gym",font="comicsansms 13 bold",pady=15).grid(row=0,column=2)
aname = Label(root, text="Name")
aname.grid(row=1)
aage = Label(root, text="Age ")
aage.grid(row=2)
amob = Label(root, text="Mobile No. ")
amob.grid(row=3)
ajoin = Label(root, text="Joining Moth. ")
ajoin.grid(row=4)

def values():
    print(f"{name.get(),age.get(),mob.get(),join.get(),fees.get()}")
    print("Values Subbmited")
    #file records.txt
    with open("records2.txt","a") as f:
        f.write(f"{name.get(),age.get(),mob.get(),join.get(),fees.get()}\n")


name = StringVar()
age = StringVar()
mob = StringVar()
join = StringVar()
fees = IntVar()


nameentry = Entry(root, textvariable=name)
ageentry = Entry(root,  textvariable=age)
mobentry = Entry(root, textvariable=mob)
joinentry = Entry(root, textvariable=join)

nameentry.grid(row=1,column=1)
ageentry.grid(row=2,column=1)
mobentry.grid(row=3,column=1)
joinentry.grid(row=4,column=1)

feesentry = Checkbutton(text="fees paid ?",variable=fees)
feesentry.grid(row=6, column=1)

Button(text="Submit", command=values).grid(row=8,column=1)

root.mainloop()