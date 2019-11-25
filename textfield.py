# this program used from login page
from tkinter import *
def sun():

   print(entrn.get())
   print(entrp.get())

log = Tk()

log.geometry("400x400")
log.maxsize(600,600)
log.minsize(200,200)
can = Canvas(log, bg="orange", height=400, width=400).pack()
can = Canvas(log,bg="yellow",height=100,width=100).place(x=30,y=90)
can = Canvas(log,bg="green",height=100,width=100).place(x=90,y=160)
# width height
username = Label(log,text="username",bg="pink").place(x=30,y=90)
password = Label(log,text="password",bg="pink").place(x=30,y=160)
entrn = Entry(log,bg="pink").place(x=100,y=90)
entrp = Entry(log,bg="pink").place(x=100,y=160)
button  = Button(log,text=" login ",bg="red",command=sun).place(x=150,y=200)

log.mainloop()