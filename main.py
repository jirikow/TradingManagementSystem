from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("1352x650+0+0")
root.title("Vehicle Trading Management System")
root.configure(background='black')


Tops = Frame(root, width=1350, height=100, bd=4, relief="raise")
Tops.pack(side=TOP)



lblInfo = Label(Tops, font=('arial', 49, 'bold'), text="Vehicle Sales Trading Management System", bd=5, anchor='w')
lblInfo.grid(row=0, column=0)

bottom = Frame(root, width=1350, height=600, bd=4, relief="raise")
bottom .pack(side=TOP)

bottomLeft = Frame(bottom, width=1000, height=600, bd=4, relief="raise")
bottomLeft .pack(side=LEFT)
#====================================================================================#
bottomLeftTop = Frame(bottomLeft, width=1000, height=300, bd=4, relief="raise")
bottomLeftTop .pack(side=TOP)

bottomLeftTopL = Frame(bottomLeftTop, width=500, height=300, bd=4, relief="raise")
bottomLeftTopL .pack(side=LEFT)

bottomLeftTopR = Frame(bottomLeftTop, width=500, height=300, bd=4, relief="raise")
bottomLeftTopR .pack(side=RIGHT)
#====================================================================================#
bottomLeftBottom = Frame(bottomLeft, width=1000, height=300, bd=4, relief="raise")
bottomLeftBottom .pack(side=BOTTOM)

bottomLeftBottomL = Frame(bottomLeftBottom, width=500, height=300, bd=4, relief="raise")
bottomLeftBottomL .pack(side=LEFT)

bottomLeftTopR = Frame(bottomLeftBottom, width=500, height=300, bd=4, relief="raise")
bottomLeftTopR .pack(side=RIGHT)
#====================================================================================#
bottomRight = Frame(bottom, width=350, height=600, bd=4, relief="raise")
bottomRight .pack(side=RIGHT)

root.mainloop()

