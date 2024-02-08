from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.geometry("1352x650+0+0")
root.title("Vehicle Trading Management System")
root.configure(background='black')


Tops = Frame(root, width=1350, height=100, bd=4, relief="raised")
Tops.pack(side=TOP)


lblInfo = Label(Tops, font=('arial', 46, 'bold'), text="Vehicle Sales Trading Management System", bd=20, anchor='w')
lblInfo.grid(row=0, column=0)

bottom = Frame(root, width=1350, height=600, bd=4, relief="raised")
bottom .pack(side=BOTTOM)

bottomLeft = Frame(bottom, width=1000, height=600, bd=2, relief="raised")
bottomLeft .pack(side=LEFT)
#====================================================================================#
bottomLeftTop = Frame(bottomLeft, width=1000, height=300, bd=2, relief="raised")
bottomLeftTop .pack(side=TOP)

bottomLeftTopL = Frame(bottomLeftTop, width=500, height=200, bd=2, relief="raised")
bottomLeftTopL .pack(side=LEFT)

bottomLeftTopR = Frame(bottomLeftTop, width=500, height=200, bd=2, relief="raised")
bottomLeftTopR .pack(side=RIGHT)
#====================================================================================#bottomLeftBottom
bottomLeftBottom = Frame(bottomLeft, width=1000, height=300, bd=2, relief="raised")
bottomLeftBottom .pack(side=BOTTOM)

bottomLeftBottomL = Frame(bottomLeftBottom, width=500, height=400, bd=2, relief="raised")
bottomLeftBottomL .pack(side=LEFT)

bottomLeftBottomR = Frame(bottomLeftBottom, width=500, height=400, bd=2, relief="raised")
bottomLeftBottomR .pack(side=RIGHT)
#====================================================================================#
bottomRight = Frame(bottom, width=350, height=600, bd=2, relief="raised")
bottomRight .pack(side=RIGHT)

#======================================EXIT=========================================#
def iExit():
    iExit = messagebox.askyesno("Vehicle Trading System", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

#======================================RESET=========================================#
def Reset():
    Modified.set("0")
    Stereo.set("0")
    Customized.set("0")
    Leather.set("0")
    GPS.set("0")
    CostofCar.set("0")
    CarMileage.set("0")

    CustomerName.set("")
    CustomerAddress.set("")
    CustomerPostcode.set("")
    CustomerTelephone.set("")

    VAT.set("")
    Discount.set("")
    Tax.set("")
    SubTotal.set("")
    Total.set("")
    txtReceipt.delete("1.0",END)

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

Modified.set("0")
Stereo.set("0")
Customized.set("0")
Leather.set("0")
GPS.set("0")

lblModified = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), text="Modified", fg="black", width=20, bd=8, anchor="w")
lblModified.grid(row=0, column=0)
txtModified = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), bd=2, width=14, bg="white", justify='left', textvariable=Modified)
txtModified.grid(row=0, column=1)

lblStereo = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), text="Stereo System", fg="black", width=20, bd=8, anchor="w")
lblStereo.grid(row=1, column=0)
txtStereo = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), bd=2, width=14, bg="white", justify='left', textvariable=Stereo)
txtStereo.grid(row=1, column=1)

lblLeather = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), text="Leather Interior ", fg="black", width=20, bd=8, anchor="w")
lblLeather.grid(row=2, column=0)
txtLeather = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), bd=2, width=14, bg="white", justify='left', textvariable=Leather)
txtLeather.grid(row=2, column=1)

lblCustomized = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), text="Customized Details", fg="black", width=20, bd=8, anchor="w")
lblCustomized.grid(row=3, column=0)
txtCustomized = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), bd=2, width=14, bg="white", justify='left', textvariable=Customized)
txtCustomized.grid(row=3, column=1)

lblGPS = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), text="GPS", fg="black", width=20, anchor="w")
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
CostofCar = StringVar()
CarMileage = StringVar()

CostofCar.set("0")
CarMileage.set("0")

lblChooseaCar = Label(bottomLeftTopR, font=('arial', 16, 'bold'), text="Choose a Car", fg="black", width=13, bd=14, anchor="w")
lblChooseaCar.grid(row=0, column=0)
cboChooseaCar = ttk.Combobox(bottomLeftTopR, textvariable= var1, state='readonly', font=('arial', 20, 'bold'), width=12)
cboChooseaCar['value']=('','Lamborghini','Buggati Veyron','Rolls Royce','Aston Martin')
cboChooseaCar.current(0)
cboChooseaCar.grid(row=1, column=0)
lblCostofCar = Label(bottomLeftTopR, font=('arial', 16, 'bold'), text="Cost of a Car", fg="black", width=13, bd=14, anchor="w")
lblCostofCar.grid(row=2, column=0)
txtCostofCar = Entry(bottomLeftTopR, font=('arial', 16, 'bold'), bd=2, width=16, bg='white', justify='left', textvariable=CostofCar)
txtCostofCar.grid(row=3, column=0)

lblTradeInaCar = Label(bottomLeftTopR, font=('arial', 16, 'bold'), text="Trade In a Car", fg="black", width=13, bd=14, anchor="w")
lblTradeInaCar.grid(row=0, column=0)
cboTradeInaCar = ttk.Combobox(bottomLeftTopR, textvariable= var2, state='readonly', font=('arial', 20, 'bold'), width=12)
cboTradeInaCar['value']=('','100-5000','5001-20000','20001-100000','100001-1000000')
cboTradeInaCar.current(0)
cboTradeInaCar.grid(row=1, column=1)
lblCarMileage = Label(bottomLeftTopR, font=('arial', 16, 'bold'), text="Car Mileage", fg="black", width=13, bd=14, anchor="w")
lblCarMileage.grid(row=2, column=1)
txtCarMileage = Entry(bottomLeftTopR, font=('arial', 16, 'bold'), bd=2, width=16, bg='white', justify='left', textvariable=CarMileage)
txtCarMileage.grid(row=3, column=1)

#======================================= 4 ==========================================#

VAT = StringVar()
Discount = StringVar()
Tax = StringVar()
SubTotal = StringVar()
Total = StringVar()

lblVAT = Checkbutton(bottomLeftBottomR, font=('arial', 16, 'bold'), text="VAT", fg="black", width=13, bd=8, anchor="w")
lblVAT.grid(row=0, column=0)
txtVAT = Entry(bottomLeftBottomR, font=('arial', 16, 'bold'), bd=2, width=17, bg="white", justify='left', textvariable=VAT)
txtVAT.grid(row=0, column=1)

lblDiscount = Checkbutton(bottomLeftBottomR, font=('arial', 16, 'bold'), text="Discount", fg="black", width=13, bd=8, anchor='w')
lblDiscount.grid(row=1, column=0)
txtDiscount = Entry(bottomLeftBottomR, font=('arial', 16, 'bold'), bd=2, width=17, bg="white", justify='left', textvariable=Discount)
txtDiscount.grid(row=1, column=1)

lblTax = Label(bottomLeftBottomR, font=('arial', 16, 'bold'), text="Tax", fg="black", width=13, bd=12, anchor='w')
lblTax.grid(row=2, column=0)
txtTax = Entry(bottomLeftBottomR, font=('arial', 16, 'bold'), bd=2, width=17, bg="white", justify='left', textvariable=Tax)
txtTax.grid(row=2, column=1)

lblSubTotal = Label(bottomLeftBottomR, font=('arial', 16, 'bold'), text="Sub Total", fg="black", width=13, bd=12, anchor='w')
lblSubTotal.grid(row=3, column=0)
txtSubTotal = Entry(bottomLeftBottomR, font=('arial', 16, 'bold'), bd=2, width=17, bg="white", justify='left', textvariable=SubTotal)
txtSubTotal.grid(row=3, column=1)

lblTotal = Label(bottomLeftBottomR, font=('arial', 16, 'bold'), text="Total", fg="black", width=13, bd=12, anchor='w')
lblTotal.grid(row=4, column=0)
txtTotal = Entry(bottomLeftBottomR, font=('arial', 16, 'bold'), bd=2, width=17, bg="white", justify='left', textvariable=Total)
txtTotal.grid(row=4, column=1)

btnReset = Button(bottomLeftBottomR,pady=8, bd=2, fg="black", font=('arial', 16, 'bold'), width=13, text="Reset ", bg='white', command=Reset).grid(row=6, column=0)

btnExit = Button(bottomLeftBottomR,pady=8, bd=2, fg="black", font=('arial', 16, 'bold'), width=13, text="Exit", bg='white', command=iExit).grid(row=6, column=1)

#=======================================   ==========================================#
lblReceipt = Label(bottomRight, font=('arial', 16, 'bold'), text="Receipt", bd=2, anchor='w')
lblReceipt.grid(row=0, column=0, sticky=W)
txtReceipt = Text(bottomRight, font=('arial', 11, 'bold'), bd=8, width=46, height=26, bg="white")
txtReceipt.grid(row=1, column=0, sticky=W)

root.mainloop()