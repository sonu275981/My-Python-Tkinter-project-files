from  tkinter import *

root = Tk()
root.title("tips & tricks")
root.geometry("400x400")
# we can set logo of our GUI given below
root.wm_iconbitmap("plat.ico")
# we can set background color of our GUI given below
root.configure(background = "red")
# To check resolation of your moniter given below
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(f"{width}x{height}")
# To close GUI window we can use distroy function given below same as quit method
Button(root, text = "CLOSE ME", command = root.destroy, bg = "yellow", fg = "blue").pack()
root.mainloop()
