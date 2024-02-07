from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("1352x650+0+0")
root.title("Vehicle Trading Management System")
root.configure(background='black')


Tops = Frame(root, width=1350, height=100, bd=4, relief="raise")
Tops.pack(side=TOP)


lblInfo = Label(Tops, font=('arial', 46, 'bold'), text="Vehicle Sales Trading Management System", bd=20, anchor='w')
lblInfo.grid(row=0, column=0)

bottom = Frame(root, width=1350, height=600, bd=4, relief="raise")
bottom .pack(side=BOTTOM)

bottomLeft = Frame(bottom, width=1000, height=600, bd=2, relief="raise")
bottomLeft .pack(side=LEFT)
#====================================================================================#
bottomLeftTop = Frame(bottomLeft, width=1000, height=300, bd=2, relief="raise")
bottomLeftTop .pack(side=TOP)

bottomLeftTopL = Frame(bottomLeftTop, width=500, height=200, bd=2, relief="raise")
bottomLeftTopL .pack(side=LEFT)

bottomLeftTopR = Frame(bottomLeftTop, width=500, height=200, bd=2, relief="raise")
bottomLeftTopR .pack(side=RIGHT)
#====================================================================================#bottomLeftBottom
bottomLeftBottom = Frame(bottomLeft, width=1000, height=300, bd=2, relief="raise")
bottomLeftBottom .pack(side=BOTTOM)

bottomLeftBottomL = Frame(bottomLeftBottom, width=500, height=400, bd=2, relief="raise")
bottomLeftBottomL .pack(side=LEFT)

bottomLeftBottomR = Frame(bottomLeftBottom, width=500, height=400, bd=2, relief="raise")
bottomLeftBottomR .pack(side=RIGHT)
#====================================================================================#
bottomRight = Frame(bottom, width=350, height=600, bd=2, relief="raise")
bottomRight .pack(side=RIGHT)

#======================================= 1 ==========================================#

CustomerName = StringVar()
CustomerAddress = StringVar()
CustomerPostcode = StringVar()
CustomerTelephone = StringVar()

lblName = Label(bottomLeftTopL, font=('arial', 16, 'bold'), text="Name", fg="black", width=15, bd=10, anchor='w')
lblName.grid(row=0, column=0)
txtName = Entry(bottomLeftTopL, font=('arial', 16, 'bold'), bd=2, width=24, bg="white", justify='left', textvariable=CustomerName)
txtName.grid(row=0, column=1)

lblAdress = Label(bottomLeftTopL, font=('arial', 16, 'bold'), text="Address", fg="black", width=15, bd=10, anchor='w')
lblAdress.grid(row=1, column=0)
txtAdress = Entry(bottomLeftTopL, font=('arial', 16, 'bold'), bd=2, width=24, bg="white", justify='left', textvariable=CustomerAddress)
txtAdress.grid(row=1, column=1)

lblPostcode = Label(bottomLeftTopL, font=('arial', 16, 'bold'), text="Postcode", fg="black", width=15, bd=10, anchor='w')
lblPostcode.grid(row=2, column=0)
txtPostcode = Entry(bottomLeftTopL, font=('arial', 16, 'bold'), bd=2, width=24, bg="white", justify='left', textvariable=CustomerPostcode)
txtPostcode.grid(row=2, column=1)

lblTelephone = Label(bottomLeftTopL, font=('arial', 16, 'bold'), text="Telephone ", fg="black", width=15, bd=10, anchor='w')
lblTelephone.grid(row=3, column=0)
txtTelephone = Entry(bottomLeftTopL, font=('arial', 16, 'bold'), bd=2, width=24, bg="white", justify='left', textvariable=CustomerTelephone)
txtTelephone.grid(row=3, column=1)

#======================================= 3 ==========================================#

Modified = StringVar()
Stereo = StringVar()
Customized = StringVar()
Leather = StringVar()
GPS = StringVar()

lblModified = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), text="Modified", fg="black", width=20, bd=10, anchor='w')
lblModified.grid(row=0, column=0)
txtModified = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), bd=2, width=14, bg="white", justify='left', textvariable=Modified)
txtModified.grid(row=0, column=1)

lblStereo = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), text="Stereo System", fg="black", width=20, bd=10, anchor='w')
lblStereo.grid(row=1, column=0)
txtStereo = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), bd=2, width=14, bg="white", justify='left', textvariable=Stereo)
txtStereo.grid(row=1, column=1)

lblLeather = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), text="Leather Interior ", fg="black", width=20, bd=10, anchor='w')
lblLeather.grid(row=2, column=0)
txtLeather = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), bd=2, width=14, bg="white", justify='left', textvariable=Leather)
txtLeather.grid(row=2, column=1)

lblCustomized = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), text="Customized Details", fg="black", width=20, bd=10, anchor='w')
lblCustomized.grid(row=3, column=0)
txtCustomized = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), bd=2, width=14, bg="white", justify='left', textvariable=Customized)
txtCustomized.grid(row=3, column=1)

lblGPS = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), text="Global Positioning System", fg="black", width=20, bd=10, anchor='w')
lblGPS.grid(row=4, column=0)
txtGPS = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), bd=2, width=14, bg="white", justify='left', textvariable=GPS)
txtGPS.grid(row=4, column=1)

btnTotalCost = Button(bottomLeftBottomL,pady=8, bd=2, fg="black", font=('arial', 16, 'bold'), width=13, text="Total ", bg='white').grid(row=5, column=0)

btnReceipt = Button(bottomLeftBottomL,pady=8, bd=2, fg="black", font=('arial', 16, 'bold'), width=13, text="Receipt ", bg='white').grid(row=5, column=1)

#======================================= 2 ==========================================#

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
lblChooseaCar = Label(bottomLeftTopR, font=('arial', 16, 'bold'), text="Choose a Car", fg="black", width=13, bd=14, anchor='w')
lblChooseaCar.grid(row=0, column=0)
cboChooseaCar = ttk.Combobox(bottomLeftTopR, textvariable= var1, state='readonly', font=('arial', 20, 'bold'), width=12)
cboChooseaCar['value']=('','Lamborghini','Buggati Veyron','Rolls Royce','Aston Martin')
cboChooseaCar.current(0)
cboChooseaCar.grid(row=1, column=0)
lblCostofCar = Label(bottomLeftTopR, font=('arial', 16, 'bold'), text="Cost of a Car", fg="black", width=13, bd=14, anchor='w')
lblCostofCar.grid(row=2, column=0)
txtCostofCar = Entry(bottomLeftTopR, font=('arial', 16, 'bold'), bd=2, width=16, bg='white', justify='left', textvariable=CustomerTelephone)
txtCostofCar.grid(row=3, column=0)

lblTradeInaCar = Label(bottomLeftTopR, font=('arial', 16, 'bold'), text="Trade In a Car", fg="black", width=13, bd=14, anchor='w')
lblTradeInaCar.grid(row=0, column=0)
cboTradeInaCar = ttk.Combobox(bottomLeftTopR, textvariable= var1, state='readonly', font=('arial', 20, 'bold'), width=12)
cboTradeInaCar['value']=('','100-5000','5001-20000','20001-100000','100001-1000000')
cboTradeInaCar.current(0)
cboTradeInaCar.grid(row=1, column=1)
lblCarMileage = Label(bottomLeftTopR, font=('arial', 16, 'bold'), text="Car Mileage", fg="black", width=13, bd=14, anchor='w')
lblCarMileage.grid(row=2, column=1)
txtCarMileage = Entry(bottomLeftTopR, font=('arial', 16, 'bold'), bd=2, width=16, bg='white', justify='left', textvariable=CustomerTelephone)
txtCarMileage.grid(row=3, column=1)

#======================================= 4 ==========================================#

root.mainloop()
