from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.geometry("1352x650+0+0")
root.title("Vehicle Trading Management System")
root.configure(background='black')


Tops = Frame(root, width=1350, height=100, bd=6, relief="raised")
Tops.pack(side=TOP)


lblInfo = Label(Tops, font=('arial', 46, 'bold'), text="Vehicle Sales Trading Management System ", bd=20, anchor="w")
lblInfo.grid(row=0, column=0)

bottom = Frame(root, width=1350, height=600, bd=10, relief="raised")
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

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set("")
    var7.set("")
    var8.set(0)
    var9.set(0)

def CarCost():
    if (var7.get() == 'Lamborghini'):
        myCar = float(98734.00)
        CostofCar.set(myCar)
    elif (var7.get() == 'Buggati Veyron'):
        myCar = float(103785.00)
        CostofCar.set(myCar)
    elif (var7.get() == 'Rolls Royce'):
        myCar = float(89757.00)
        CostofCar.set(myCar)
    elif (var7.get() == 'Aston Martin'):
        myCar = float(123785.00)
        CostofCar.set(myCar)

    if (var18.get() == '100-5000' and var7.get() == 'Buggati Veyron'):
        myCar = float(103785.00)
        iMile = float(9000.00)
        CostofCar.set(myCar)
        CarMileage.set(iMile)
    if (var18.get() == '5001-20000' and var7.get() == 'Buggati Veyron'):
        myCar = float(103785.00)
        iMile = float(7000.00)
        CostofCar.set(myCar)
        CarMileage.set(iMile)
    if (var18.get() == '20001-100000' and var7.get() == 'Buggati Veyron'):
        myCar = float(103785.00)
        iMile = float(4000.00)
        CostofCar.set(myCar)
        CarMileage.set(iMile)
    if (var18.get() == '100001-1000000' and var7.get() == 'Buggati Veyron'):
        myCar = float(103785.00)
        iMile = float(2000.00)
        CostofCar.set(myCar)
        CarMileage.set(iMile)

    if (var18.get() == '100-5000' and var7.get() == 'Lamborghini'):
        myCar = float(98734.90)
        iMile = float(10099.90)
        CostofCar.set(myCar)
        CarMileage.set(iMile)
    if (var18.get() == '5001-20000' and var7.get() == 'Lamborghini'):
        myCar = float(98734.90)
        iMile = float(7999.90)
        CostofCar.set(myCar)
        CarMileage.set(iMile)
    if (var18.get() == '20001-100000' and var7.get() == 'Lamborghini'):
        myCar = float(98734.90)
        iMile = float(4999.90)
        CostofCar.set(myCar)
        CarMileage.set(iMile)
    if (var18.get() == '100001-1000000' and var7.get() == 'Lamborghini'):
        myCar = float(98734.90)
        iMile = float(2999.90)
        CostofCar.set(myCar)
        CarMileage.set(iMile)

    if (var18.get() == '100-5000' and var7.get() == 'Rolls Royce'):
        myCar = float(89757.90)
        iMile = float(10999.90)
        CostofCar.set(myCar)
        CarMileage.set(iMile)
    if (var18.get() == '5001-20000' and var7.get() == 'Rolls Royce'):
        myCar = float(89757.90)
        iMile = float(8999.90)
        CostofCar.set(myCar)
        CarMileage.set(iMile)
    if (var18.get() == '20001-100000' and var7.get() == 'Rolls Royce'):
        myCar = float(89757.90)
        iMile = float(6999.90)
        CostofCar.set(myCar)
        CarMileage.set(iMile)
    if (var18.get() == '100001-1000000' and var7.get() == 'Rolls Royce'):
        myCar = float(89757.90)
        iMile = float(3999.90)
        CostofCar.set(myCar)
        CarMileage.set(iMile)

    if (var18.get() == '100-5000' and var7.get() == 'Aston Martin'):
        myCar = float(123785.00)
        iMile = float(10999.90)
        CostofCar.set(myCar)
        CarMileage.set(iMile)
    if (var18.get() == '5001-20000' and var7.get() == 'Aston Martin'):
        myCar = float(123785.00)
        iMile = float(8599.90)
        CostofCar.set(myCar)
        CarMileage.set(iMile)
    if (var18.get() == '20001-100000' and var7.get() == 'Aston Martin'):
        myCar = float(123785.00)
        iMile = float(5599.90)
        CostofCar.set(myCar)
        CarMileage.set(iMile)
    if (var18.get() == '100001-1000000' and var7.get() == 'Aston Martin'):
        myCar = float(123785.00)
        iMile = float(3599.90)
        CostofCar.set(myCar)
        CarMileage.set(iMile)

    if (var1.get() == 1):
        Modified.set(5000)
    elif (var1.get() == 0):
        Modified.set(0)
    if (var2.get() == 1):
        Stereo.set(350)
    elif (var2.get() == 0):
        Stereo.set(0)
    if (var3.get() == 1):
        Leather.set(4200)
    elif (var3.get() == 0):
        Leather.set(0)
    if (var4.get() == 1):
        Customized.set(10999)
    elif (var4.get() == 0):
        Customized.set(0)
    if (var5.get() == 1):
        GPS.set(500)
    elif (var5.get() == 0):
        GPS.set(0)
    if (var8.get() == 1):
        VAT.set("Yes")
    elif (var8.get() == 0):
        VAT.set("No")
    if (var9.get() == 1):
        Discount.set("Yes")
    elif (var9.get() == 0):
        Discount.set("No")

#======================================= 1 ==========================================#

CustomerName = StringVar()
CustomerAddress = StringVar()
CustomerPostcode = StringVar()
CustomerTelephone = StringVar()

lblName = Label(bottomLeftTopL, font=('arial', 16, 'bold'), text="Name", fg="black", width=15,
                bd=10, anchor='w')
lblName.grid(row=0, column=0)
txtName = Entry(bottomLeftTopL, font=('arial', 16, 'bold'), bd=2, width=24, bg="white", justify='left',
                textvariable=CustomerName)
txtName.grid(row=0, column=1)

lblAdress = Label(bottomLeftTopL, font=('arial', 16, 'bold'), text="Address", fg="black", width=15,
                  bd=10, anchor='w')
lblAdress.grid(row=1, column=0)
txtAdress = Entry(bottomLeftTopL, font=('arial', 16, 'bold'), bd=2, width=24, bg="white", justify='left',
                  textvariable=CustomerAddress)
txtAdress.grid(row=1, column=1)

lblPostcode = Label(bottomLeftTopL, font=('arial', 16, 'bold'), text="Postcode", fg="black", width=15,
                    bd=10, anchor='w')
lblPostcode.grid(row=2, column=0)
txtPostcode = Entry(bottomLeftTopL, font=('arial', 16, 'bold'), bd=2, width=24, bg="white", justify='left',
                    textvariable=CustomerPostcode)
txtPostcode.grid(row=2, column=1)

lblTelephone = Label(bottomLeftTopL, font=('arial', 16, 'bold'), text="Telephone ", fg="black", width=15,
                     bd=10, anchor='w')
lblTelephone.grid(row=3, column=0)
txtTelephone = Entry(bottomLeftTopL, font=('arial', 16, 'bold'), bd=2, width=24, bg="white", justify='left',
                     textvariable=CustomerTelephone)
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

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

lblModified = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), text="Modified", fg="black", width=20, bd=8,
                          anchor="w", onvalue=1, offvalue=0, variable=var1)
lblModified.grid(row=0, column=0)
txtModified = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), bd=2, width=14, bg="white", justify='left',
                    textvariable=Modified)
txtModified.grid(row=0, column=1)

lblStereo = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), text="Stereo System", fg="black", width=20, bd=8,
                        anchor="w", onvalue=1, offvalue=0, variable=var2)
lblStereo.grid(row=1, column=0)
txtStereo = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), bd=2, width=14, bg="white", justify='left',
                  textvariable=Stereo)
txtStereo.grid(row=1, column=1)

lblLeather = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), text="Leather Interior ", fg="black", width=20,
                         bd=8, anchor="w", onvalue=1, offvalue=0, variable=var3)
lblLeather.grid(row=2, column=0)
txtLeather = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), bd=2, width=14, bg="white", justify='left',
                   textvariable=Leather)
txtLeather.grid(row=2, column=1)

lblCustomized = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), text="Customized Details", fg="black",
                            width=20, bd=8, anchor="w", onvalue=1, offvalue=0, variable=var4)
lblCustomized.grid(row=3, column=0)
txtCustomized = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), bd=2, width=14, bg="white", justify='left',
                      textvariable=Customized)
txtCustomized.grid(row=3, column=1)

lblGPS = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), text="GPS", fg="black", width=20, anchor="w",
                     onvalue=1, offvalue=0, variable=var5)
lblGPS.grid(row=4, column=0)
txtGPS = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), bd=2, width=14, bg="white", justify='left',
               textvariable=GPS)
txtGPS.grid(row=4, column=1)

btnTotalCost = Button(bottomLeftBottomL,pady=8, bd=2, fg="black", font=('arial', 16, 'bold'), width=13, text="Total ",
                      bg='white', command=CarCost).grid(row=5, column=0)

btnReceipt = Button(bottomLeftBottomL,pady=8, bd=2, fg="black", font=('arial', 16, 'bold'), width=13, text="Receipt ",
                    bg='white').grid(row=5, column=1)

#======================================= 2 ==========================================#

var6 = StringVar()
var7 = StringVar()
var18 = StringVar()

CostofCar = StringVar()
CarMileage = StringVar()

CostofCar.set("0")
CarMileage.set("0")

lblChooseaCar = Label(bottomLeftTopR, font=('arial', 16, 'bold'), text="Choose a Car", fg="black", width=13, bd=14,
                      anchor="w")
lblChooseaCar.grid(row=0, column=0)
cboChooseaCar = ttk.Combobox(bottomLeftTopR, textvariable= var7, state='readonly', font=('arial', 20, 'bold'), width=12)
cboChooseaCar['value']=('','Lamborghini','Buggati Veyron','Rolls Royce','Aston Martin')
cboChooseaCar.current(0)
cboChooseaCar.grid(row=1, column=0)
lblCostofCar = Label(bottomLeftTopR, font=('arial', 16, 'bold'), text="Cost of a Car", fg="black", width=13, bd=14,
                     anchor="w")
lblCostofCar.grid(row=2, column=0)
txtCostofCar = Entry(bottomLeftTopR, font=('arial', 16, 'bold'), bd=2, width=16, bg='white', justify='left',
                     textvariable=CostofCar)
txtCostofCar.grid(row=3, column=0)

lblTradeInaCar = Label(bottomLeftTopR, font=('arial', 16, 'bold'), text="Trade In a Car", fg="black", width=13, bd=14,
                       anchor="w")
lblTradeInaCar.grid(row=0, column=1)
cboTradeInaCar = ttk.Combobox(bottomLeftTopR, textvariable= var18, state='readonly', font=('arial', 20, 'bold'),
                              width=12)
cboTradeInaCar['value']=('','100-5000','5001-20000','20001-100000','100001-1000000')
cboTradeInaCar.current(0)
cboTradeInaCar.grid(row=1, column=1)
lblCarMileage = Label(bottomLeftTopR, font=('arial', 16, 'bold'), text="Car Mileage", fg="black", width=13, bd=14,
                      anchor="w")
lblCarMileage.grid(row=2, column=1)
txtCarMileage = Entry(bottomLeftTopR, font=('arial', 16, 'bold'), bd=2, width=16, bg='white', justify='left',
                      textvariable=CarMileage)
txtCarMileage.grid(row=3, column=1)

#======================================= 4 ==========================================#

VAT = StringVar()
Discount = StringVar()
Tax = StringVar()
SubTotal = StringVar()
Total = StringVar()

var8 = IntVar()
var9 = IntVar()

lblVAT = Checkbutton(bottomLeftBottomR, font=('arial', 16, 'bold'), text="VAT", fg="black", width=13, bd=8,
                     anchor="w",onvalue=1, offvalue=0, variable=var8)
lblVAT.grid(row=0, column=0)
txtVAT = Entry(bottomLeftBottomR, font=('arial', 16, 'bold'), bd=2, width=17, bg="white", justify='left',
               textvariable=VAT)
txtVAT.grid(row=0, column=1)

lblDiscount = Checkbutton(bottomLeftBottomR, font=('arial', 16, 'bold'), text="Discount", fg="black", width=13,
                          bd=8, anchor='w', onvalue=1, offvalue=0, variable=var9)
lblDiscount.grid(row=1, column=0)
txtDiscount = Entry(bottomLeftBottomR, font=('arial', 16, 'bold'), bd=2, width=17, bg="white", justify='left',
                    textvariable=Discount)
txtDiscount.grid(row=1, column=1)

lblTax = Label(bottomLeftBottomR, font=('arial', 16, 'bold'), text="Tax", fg="black", width=13, bd=12, anchor='w')
lblTax.grid(row=2, column=0)
txtTax = Entry(bottomLeftBottomR, font=('arial', 16, 'bold'), bd=2, width=17, bg="white", justify='left',
               textvariable=Tax)
txtTax.grid(row=2, column=1)

lblSubTotal = Label(bottomLeftBottomR, font=('arial', 16, 'bold'), text="Sub Total", fg="black", width=13, bd=12,
                    anchor='w')
lblSubTotal.grid(row=3, column=0)
txtSubTotal = Entry(bottomLeftBottomR, font=('arial', 16, 'bold'), bd=2, width=17, bg="white", justify='left',
                    textvariable=SubTotal)
txtSubTotal.grid(row=3, column=1)

lblTotal = Label(bottomLeftBottomR, font=('arial', 16, 'bold'), text="Total", fg="black", width=13, bd=12, anchor='w')
lblTotal.grid(row=4, column=0)
txtTotal = Entry(bottomLeftBottomR, font=('arial', 16, 'bold'), bd=2, width=17, bg="white", justify='left',
                 textvariable=Total)
txtTotal.grid(row=4, column=1)

btnReset = Button(bottomLeftBottomR,pady=8, bd=2, fg="black", font=('arial', 16, 'bold'), width=13, text="Reset ",
                  bg='white', command=Reset).grid(row=6, column=0)

btnExit = Button(bottomLeftBottomR,pady=8, bd=2, fg="black", font=('arial', 16, 'bold'), width=13, text="Exit",
                 bg='white', command=iExit).grid(row=6, column=1)

#=======================================   ==========================================#

lblReceipt = Label(bottomRight, font=('arial', 16, 'bold'), text="Receipt", bd=2, anchor='w')
lblReceipt.grid(row=0, column=0, sticky=W)
txtReceipt = Text(bottomRight, font=('arial', 11, 'bold'), bd=8, width=46, height=26, bg="white")
txtReceipt.grid(row=1, column=0, sticky=W)

root.mainloop()

#1.18.07