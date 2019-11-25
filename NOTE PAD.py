from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

# creating function
def new():
    global  file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def open():
   global file
   file = askopenfilename(defaultextension=".txt",
                          filetypes=[("All Files", "."),
                                     ("Text Documents", "*.txt")])
   if file == "":
       file = None
   else:
       root.title(os.path.basename(file) + " - Notepad")
       TextArea.delete(1.0, END)
       f = open(file, "r")
       TextArea.insert(1.0, f.read())
       f.close()


def save():
   global file
   if file == None:
       file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                filetypes=[("All Files", "."),
                                           ("Text Documents", "*.txt")])
       if file == "":
           file = None

       else:
           # Save as a new file
           f = open(file, "w")
           f.write(TextArea.get(1.0, END))
           f.close()

           root.title(os.path.basename(file) + " - Notepad")
           print("File Saved")
   else:
       # Save the file
       f = open(file, "w")
       f.write(TextArea.get(1.0, END))
       f.close()


def quitApp():
    root.destroy()


def cut():
    TextArea.event_generate(("<<Cut>>"))


def copy():
    TextArea.event_generate(("<<Copy>>"))


def paste():
    TextArea.event_generate(("<<Paste>>"))


def about():
    showinfo("Notepad", "Notepad by Sonu \n Panipat")


if __name__ == '__main__':
    # basic setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("notepad.ico")
    root.geometry("475x650")
    root.configure(background="white")

    # Add text area
    TextArea = Text(root, font="lucida 13", )
    file = None
    TextArea.pack(fill=BOTH, expand=True)

    # 1 Create File menu bar
    filemenu = Menu(root)

    menubar = Menu(filemenu)
    menubar.add_command(label="New", command=new)
    menubar.add_separator()
    menubar.add_command(label="Open", command=open)
    menubar.add_separator()
    menubar.add_command(label="Save", command=save)
    menubar.add_separator()
    menubar.add_command(label="Exit", command=quitApp)
    filemenu.add_cascade(label="File", menu=menubar)

    # 2 Create Edit menu bar
    editmenu = Menu(filemenu)
    editmenu.add_command(label="Cut", command=cut)
    editmenu.add_separator()
    editmenu.add_command(label="Copy", command=cut)
    editmenu.add_separator()
    editmenu.add_command(label="Paste", command=paste)
    filemenu.add_cascade(label="Edit", menu=editmenu)

    # 3 create about menu bar
    abt = Menu(filemenu)
    abt.add_command(label="About", command=about)
    filemenu.add_cascade(label="About", menu=abt)

    root.config(menu=filemenu)

    # add Scrollbar in note pad
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()
