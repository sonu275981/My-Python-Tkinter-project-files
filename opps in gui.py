from tkinter import *
# incomplete program

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")

if __name__ == '__main__':
    sam = GUI()
    sam.createbuttion("click me")
    sam.mainloop()

