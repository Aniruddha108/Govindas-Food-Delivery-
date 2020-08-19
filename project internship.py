from tkinter import *
import random
import time
import datetime
import tkinter.messagebox

root = Tk()
root.title("Govindas Food Delivery")
root.configure(background="Blue")

Tops = Frame(root, bg="Red", bd=20, pady=10, padx=10, relief=RIDGE)
Tops.pack(side=TOP)

lbTitle = Label(
    Tops,
    font=("arial", 50, "bold"),
    text="Govindas Food Delivery",
    padx=350,
    bd=11,
    bg="Green",
    fg="Cornsilk",
    justify=CENTER,
)
lbTitle.grid(row=0, column=0)

ReceiptCal_F = Frame(root, bg="Red", bd=10, relief=RIDGE,)
ReceiptCal_F.pack(side=RIGHT)

Cal_F = Frame(ReceiptCal_F, bg="Yellow", bd=10, relief=RIDGE)
Cal_F.pack(side=TOP)
Buttons_F = Frame(ReceiptCal_F, bg="Yellow", bd=10, padx=5, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)
Receipt_F = Frame(ReceiptCal_F, bg="Yellow", bd=10, padx=5, relief=RIDGE)
Receipt_F.pack(side=BOTTOM)
menuFrame = Frame(root, bg="red", bd=10, relief=RIDGE)
menuFrame.pack(side=LEFT)
Cost_F = Frame(menuFrame, bg="Yellow", bd=10, padx=25, relief=RIDGE)
Cost_F.pack(side=BOTTOM)
Drinks_F = Frame(menuFrame, bg="Cadet Blue", bd=10, relief=RIDGE)
Drinks_F.pack(side=TOP)


Drinks_F = Frame(menuFrame, bg="Orange", bd=15, pady=65, padx=8, relief=RIDGE)
Drinks_F.pack(side=LEFT)
Cake_F = Frame(menuFrame, bg="Orange", bd=15, pady=65, padx=8, relief=RIDGE)
Cake_F.pack(side=RIGHT)

# Variables
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()

DateofOrder = StringVar()
Receipt = StringVar()
PT = StringVar()
SCost = StringVar()
TCost = StringVar()
ACost = StringVar()
Cost = StringVar()
SC = StringVar()

text_Input = StringVar()
operator = ""

E_Lemon_Soda = StringVar()
E_Samosa = StringVar()
E_Patties = StringVar()
E_Pani_Puri = StringVar()
E_Vada = StringVar()
E_Herbalc = StringVar()
E_Herbalt = StringVar()
E_Ice = StringVar()

E_Chole_Bhature = StringVar()
E_Pasta = StringVar()
E_Sambar = StringVar()
E_Pizza = StringVar()
E_Cake = StringVar()
E_Manchurian = StringVar()
E_Hakka = StringVar()
E_Paneer = StringVar()

E_Full = StringVar()
E_Address = StringVar()
E_Pin = StringVar()
E_Phone = StringVar()


E_Lemon_Soda.set("0")
E_Samosa.set("0")
E_Patties.set("0")
E_Pani_Puri.set("0")
E_Vada.set("0")
E_Herbalc.set("0")
E_Herbalt.set("0")
E_Ice.set("0")

E_Chole_Bhature.set("0")
E_Pasta.set("0")
E_Sambar.set("0")
E_Pizza.set("0")
E_Cake.set("0")
E_Manchurian.set("0")
E_Hakka.set("0")
E_Paneer.set("0")

E_Full.set("xxxxxxxxxx xxxxx")
E_Address.set("xxxxxx xxx xxxxx xxxxxxxxx")
E_Pin.set("xxxxxx")
E_Phone.set("xxxxxxxxxx")


DateofOrder.set(time.strftime("%d/%m/%Y"))

# Function Declared


def iExit():
    iExit = tkinter.messagebox.askyesno(
        "Exit Govindas Food Delivery", "Confirm if u want to exit"
    )
    if iExit > 0:
        root.destroy()
        return


def Reset():
    PT.set("")
    SCost.set("")
    TCost.set("")
    ACost.set("")
    Cost.set("")
    SC.set("")
    txtReceipt.delete("1.0", END)

    E_Lemon_Soda.set("0")
    E_Samosa.set("0")
    E_Patties.set("0")
    E_Pani_Puri.set("0")
    E_Vada.set("0")
    E_Herbalc.set("0")
    E_Herbalt.set("0")
    E_Ice.set("0")

    E_Chole_Bhature.set("0")
    E_Pasta.set("0")
    E_Sambar.set("0")
    E_Pizza.set("0")
    E_Cake.set("0")
    E_Manchurian.set("0")
    E_Hakka.set("0")
    E_Paneer.set("0")

    E_Full.set("xxxxxxxxxx xxxxx")
    E_Address.set("xxxxxx xxx xxxxx xxxxxxxxx")
    E_Pin.set("xxxxxx")
    E_Phone.set("xxxxxxxxxx")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)

    txtLemon_Soda.configure()
    txtSamosa.configure()
    txtPatties.configure()
    txtPani_Puri.configure()
    txtVada.configure()
    txtHerbalc.configure()
    txtHerbalt.configure()
    txtIce.configure()
    txtChole_Bhature.configure()
    txtPasta.configure()
    txtSambar.configure()
    txtPizza.configure()
    txtCake.configure()
    txtManchurian.configure()
    txtHakka.configure()
    txtPaneer.configure()
    txtFull.configure()
    txtAddress.configure()
    txtPin.configure()
    txtPhone.configure()


def CostofItem():
    Item1 = float(E_Lemon_Soda.get())
    Item2 = float(E_Samosa.get())
    Item3 = float(E_Patties.get())
    Item4 = float(E_Pani_Puri.get())
    Item5 = float(E_Vada.get())
    Item6 = float(E_Herbalc.get())
    Item7 = float(E_Herbalt.get())
    Item8 = float(E_Ice.get())

    Item9 = float(E_Chole_Bhature.get())
    Item10 = float(E_Pasta.get())
    Item11 = float(E_Sambar.get())
    Item12 = float(E_Pizza.get())
    Item13 = float(E_Cake.get())
    Item14 = float(E_Manchurian.get())
    Item15 = float(E_Hakka.get())
    Item16 = float(E_Paneer.get())

    PriceofDrinks = (
        (Item1 * 5)
        + (Item2 * 10)
        + (Item3 * 15)
        + (Item4 * 25)
        + (Item5 * 10)
        + (Item6 * 5)
        + (Item7 * 15)
        + (Item8 * 25)
    )

    PriceofCakes = (
        (Item9 * 65)
        + (Item10 * 80)
        + (Item11 * 125)
        + (Item12 * 320)
        + (Item13 * 250)
        + (Item14 * 145)
        + (Item15 * 95)
        + (Item16 * 120)
    )

    DrinksPrice = str("₹%.2f" % (PriceofDrinks))
    CakesPrice = str("₹%.2f" % (PriceofCakes))
    ACost.set(CakesPrice)
    Cost.set(DrinksPrice)
    x = str("₹%.2f" % (1.19))
    SC.set(x)

    SCostofItems = str("₹%.2f" % (PriceofDrinks + PriceofCakes + 1.19))
    SCost.set(SCostofItems)

    tax = str("₹%.2f" % ((PriceofDrinks + PriceofCakes + 1.19) * 0.11))
    PT.set(tax)
    TT = (PriceofDrinks + PriceofCakes + 1.19) * 0.11
    TC = str("₹%.2f" % (PriceofDrinks + PriceofCakes + 1.19 + TT))
    TCost.set(TC)


def chkLemon():
    if var1.get() == 1:
        txtLemon_Soda.configure(state=NORMAL)
        txtLemon_Soda.focus()
        txtLemon_Soda.delete("0", END)
        E_Lemon_Soda.set("")
    elif var1.get() == 0:
        txtLemon_Soda.configure(state=DISABLED)
        E_Lemon_Soda.set("0")


def chkSamosa():
    if var2.get() == 1:
        txtSamosa.configure(state=NORMAL)
        txtSamosa.focus()
        txtSamosa.delete("0", END)
        E_Samosa.set("")
    elif var2.get() == 0:
        txtSamosa.configure(state=DISABLED)
        E_Samosa.set("0")


def chkPatties():
    if var3.get() == 1:
        txtPatties.configure(state=NORMAL)
        txtPatties.focus()
        txtPatties.delete("0", END)
        E_Patties.set("")
    elif var3.get() == 0:
        txtPatties.configure(state=DISABLED)
        E_Patties.set("0")


def chkPani():
    if var4.get() == 1:
        txtPani_Puri.configure(state=NORMAL)
        txtPani_Puri.focus()
        txtPani_Puri.delete("0", END)
        E_Pani_Puri.set("")
    elif var4.get() == 0:
        txtPani_Puri.configure(state=DISABLED)
        E_Pani_Puri.set("0")


def chkVada():
    if var5.get() == 1:
        txtVada.configure(state=NORMAL)
        txtVada.focus()
        txtVada.delete("0", END)
        E_Vada.set("")
    elif var5.get() == 0:
        txtVada.configure(state=DISABLED)
        E_Vada.set("0")


def chkHC():
    if var6.get() == 1:
        txtHerbalc.configure(state=NORMAL)
        txtHerbalc.focus()
        txtHerbalc.delete("0", END)
        E_Herbalc.set("")
    elif var6.get() == 0:
        txtHerbalc.configure(state=DISABLED)
        E_Herbalc.set("0")


def chkHT():
    if var7.get() == 1:
        txtHerbalt.configure(state=NORMAL)
        txtHerbalt.focus()
        txtHerbalt.delete("0", END)
        E_Herbalt.set("")
    elif var7.get() == 0:
        txtHerbalt.configure(state=DISABLED)
        E_Herbalt.set("0")


def chkIce():
    if var8.get() == 1:
        txtIce.configure(state=NORMAL)
        txtIce.focus()
        txtIce.delete("0", END)
        E_Ice.set("")
    elif var8.get() == 0:
        txtIce.configure(state=DISABLED)
        E_Ice.set("0")


def chkChole():
    if var9.get() == 1:
        txtChole_Bhature.configure(state=NORMAL)
        txtChole_Bhature.focus()
        txtChole_Bhature.delete("0", END)
        E_Chole_Bhature.set("")
    elif var9.get() == 0:
        txtChole_Bhature.configure(state=DISABLED)
        E_Chole_Bhature.set("0")


def chkPasta():
    if var10.get() == 1:
        txtPasta.configure(state=NORMAL)
        txtPasta.focus()
        txtPasta.delete("0", END)
        E_Pasta.set("")
    elif var10.get() == 0:
        txtPasta.configure(state=DISABLED)
        E_Pasta.set("0")


def chkSambar():
    if var11.get() == 1:
        txtSambar.configure(state=NORMAL)
        txtSambar.focus()
        txtSambar.delete("0", END)
        E_Sambar.set("")
    elif var11.get() == 0:
        txtSambar.configure(state=DISABLED)
        E_Sambar.set("0")


def chkPizza():
    if var12.get() == 1:
        txtPizza.configure(state=NORMAL)
        txtPizza.focus()
        txtPizza.delete("0", END)
        E_Pizza.set("")
    elif var12.get() == 0:
        txtPizza.configure(state=DISABLED)
        E_Pizza.set("0")


def chkCake():
    if var13.get() == 1:
        txtCake.configure(state=NORMAL)
        txtCake.focus()
        txtCake.delete("0", END)
        E_Cake.set("")
    elif var13.get() == 0:
        txtCake.configure(state=DISABLED)
        E_Cake.set("0")


def chkManchurian():
    if var14.get() == 1:
        txtManchurian.configure(state=NORMAL)
        txtManchurian.focus()
        txtManchurian.delete("0", END)
        E_Manchurian.set("")
    elif var14.get() == 0:
        txtManchurian.configure(state=DISABLED)
        E_Manchurian.set("0")


def chkHakka():
    if var15.get() == 1:
        txtHakka.configure(state=NORMAL)
        txtHakka.focus()
        txtHakka.delete("0", END)
        E_Hakka.set("")
    elif var15.get() == 0:
        txtHakka.configure(state=DISABLED)
        E_Hakka.set("0")


def chkPanner():
    if var16.get() == 1:
        txtPaneer.configure(state=NORMAL)
        txtPaneer.focus()
        txtPaneer.delete("0", END)
        E_Paneer.set("")
    elif var16.get() == 0:
        txtPaneer.configure(state=DISABLED)
        E_Paneer.set("0")


def chkFull():
    if var17.get() == 1:
        txtFull.configure(state=NORMAL)
        txtFull.focus()
        txtFull.delete("0", END)
        E_Full.set("")
    elif var17.get() == 0:
        txtFull.configure(state=DISABLED)
        E_Full.set("xxxxxxxxxx xxxxx")


def chkAddress():
    if var18.get() == 1:
        txtAddress.configure(state=NORMAL)
        txtAddress.focus()
        txtAddress.delete("0", END)
        E_Address.set("")
    elif var18.get() == 0:
        txtAddress.configure(state=DISABLED)
        E_Address.set("xxxxxx xxx xxxxx xxxxxxxxx")


def chkPin():
    if var19.get() == 1:
        txtPin.configure(state=NORMAL)
        txtPin.focus()
        txtPin.delete("0", END)
        E_Pin.set("")
    elif var19.get() == 0:
        txtPin.configure(state=DISABLED)
        E_Pin.set("xxxxxx")


def chkPhone():
    if var20.get() == 1:
        txtPhone.configure(state=NORMAL)
        txtPhone.focus()
        txtPhone.delete("0", END)
        E_Phone.set("")
    elif var20.get() == 0:
        txtPhone.configure(state=DISABLED)
        E_Phone.set("xxxxxxxxxx")


def Reciept():
    txtReceipt.delete("1.0", END)
    x = random.randint(10903, 609235)
    randomRef = str(x)
    Receipt.set("Bill" + randomRef)

    txtReceipt.insert(END, "Date of Order\t\t\t" + DateofOrder.get() + "\n")

    txtReceipt.insert(END, "Receipt Refrence\t\t\t" + Receipt.get() + "\t" + "\n")

    txtReceipt.insert(END, "\n           Information of Items\t\t\t" + "\n")
    txtReceipt.insert(END, "Item\t\t\t" + "Cost of Items\n")
    txtReceipt.insert(END, "Lemon Soda\t\t\t" + E_Lemon_Soda.get() + "\n")
    txtReceipt.insert(END, "Samosa\t\t\t" + E_Samosa.get() + "\n")
    txtReceipt.insert(END, "Patties\t\t\t" + E_Patties.get() + "\n")
    txtReceipt.insert(END, "Pani Puri\t\t\t" + E_Pani_Puri.get() + "\n")
    txtReceipt.insert(END, "Vada Pav\t\t\t" + E_Vada.get() + "\n")
    txtReceipt.insert(END, "Herbal Cofee\t\t\t" + E_Herbalc.get() + "\n")
    txtReceipt.insert(END, "Herbal Tea\t\t\t" + E_Herbalt.get() + "\n")
    txtReceipt.insert(END, "Ice-Cream\t\t\t" + E_Ice.get() + "\n")
    txtReceipt.insert(END, "Chole Bhature\t\t\t" + E_Chole_Bhature.get() + "\n")
    txtReceipt.insert(END, "Pasta\t\t\t" + E_Pasta.get() + "\n")
    txtReceipt.insert(END, "Sambar Idli/Dosa(Plain)\t\t\t" + E_Sambar.get() + "\n")
    txtReceipt.insert(END, "Cheese Pizza\t\t\t" + E_Pizza.get() + "\n")
    txtReceipt.insert(END, "Cake\t\t\t" + E_Cake.get() + "\n")
    txtReceipt.insert(END, "Manchurian Rice\t\t\t" + E_Manchurian.get() + "\n")
    txtReceipt.insert(END, "Hakka Noodeles\t\t\t" + E_Hakka.get() + "\n")
    txtReceipt.insert(END, "Paneer 65\t\t\t" + E_Paneer.get() + "\n")

    txtReceipt.insert(END, "\n                         Bill History\t\t\t" + "\n")
    txtReceipt.insert(
        END,
        "Cost of Drinks\t\t\t"
        + str(Cost.get())
        + "\nCost of Meals\t\t\t"
        + ACost.get()
        + "\n",
    )
    txtReceipt.insert(
        END, "Service Charge\t\t\t" + SC.get() + "\nTax Paid\t\t\t" + PT.get() + "\n",
    )
    txtReceipt.insert(
        END,
        "Sub Total\t\t\t"
        + str(SCost.get())
        + "\nTotal Cost\t\t\t"
        + str(TCost.get())
        + "\n",
    )

    txtReceipt.insert(END, "\n           Information for Home Delivery\t\t\t" + "\n")
    txtReceipt.insert(END, "Full Name\t\t\t" + E_Full.get() + "\n")
    txtReceipt.insert(END, "Full Address\t\t\t" + E_Address.get() + "\n")
    txtReceipt.insert(END, "Pincode\t\t\t" + E_Pin.get() + "\n")
    txtReceipt.insert(END, "Phone no\t\t\t" + E_Phone.get() + "\n")

    txtReceipt.insert(END, "Full Address:\t\t\t" + E_Address.get() + "\n")
    txtReceipt.insert(END, "Pincode:\t\t\t" + E_Pin.get() + "\n")
    txtReceipt.insert(END, "Phone no:\t\t\t" + E_Phone.get() + "\n")


# For Drinks and Fast Food
Lemon_Soda = Checkbutton(
    Drinks_F,
    text="Lemon Soda           ",
    variable=var1,
    onvalue=1,
    offvalue=0,
    font=("arial", 16, "bold"),
    bg="Orange",
    command=chkLemon,
).grid(row=0, sticky=W)
Samosa = Checkbutton(
    Drinks_F,
    text="Samosa",
    variable=var2,
    onvalue=1,
    offvalue=0,
    font=("arial", 16, "bold"),
    bg="Orange",
    command=chkSamosa,
).grid(row=1, sticky=W)
Patties = Checkbutton(
    Drinks_F,
    text="Patties",
    variable=var3,
    onvalue=1,
    offvalue=0,
    font=("arial", 16, "bold"),
    bg="Orange",
    command=chkPatties,
).grid(row=2, sticky=W)
Pani_Puri = Checkbutton(
    Drinks_F,
    text="Pani Puri",
    variable=var4,
    onvalue=1,
    offvalue=0,
    font=("arial", 16, "bold"),
    bg="Orange",
    command=chkPani,
).grid(row=3, sticky=W)
Vada = Checkbutton(
    Drinks_F,
    text="Vada Pav",
    variable=var5,
    onvalue=1,
    offvalue=0,
    font=("arial", 16, "bold"),
    bg="Orange",
    command=chkVada,
).grid(row=4, sticky=W)
Herbalc = Checkbutton(
    Drinks_F,
    text="Herbal Coffee",
    variable=var6,
    onvalue=1,
    offvalue=0,
    font=("arial", 16, "bold"),
    bg="Orange",
    command=chkHC,
).grid(row=5, sticky=W)
Herbalt = Checkbutton(
    Drinks_F,
    text="Herbal Tea",
    variable=var7,
    onvalue=1,
    offvalue=0,
    font=("arial", 16, "bold"),
    bg="Orange",
    command=chkHT,
).grid(row=6, sticky=W)
Ice = Checkbutton(
    Drinks_F,
    text="Ice-Cream",
    variable=var8,
    onvalue=1,
    offvalue=0,
    font=("arial", 16, "bold"),
    bg="Orange",
    command=chkIce,
).grid(row=7, sticky=W)
# Entry Box For Drinks
txtLemon_Soda = Entry(
    Drinks_F,
    font=("arial", 16, "bold"),
    bd=8,
    width=12,
    justify=LEFT,
    textvariable=E_Lemon_Soda,
)
txtLemon_Soda.grid(row=0, column=2)
txtSamosa = Entry(
    Drinks_F,
    font=("arial", 16, "bold"),
    bd=8,
    width=12,
    justify=LEFT,
    textvariable=E_Samosa,
)
txtSamosa.grid(row=1, column=2)
txtPatties = Entry(
    Drinks_F,
    font=("arial", 16, "bold"),
    bd=8,
    width=12,
    justify=LEFT,
    textvariable=E_Patties,
)
txtPatties.grid(row=2, column=2)
txtPani_Puri = Entry(
    Drinks_F,
    font=("arial", 16, "bold"),
    bd=8,
    width=12,
    justify=LEFT,
    textvariable=E_Pani_Puri,
)
txtPani_Puri.grid(row=3, column=2)
txtVada = Entry(
    Drinks_F,
    font=("arial", 16, "bold"),
    bd=8,
    width=12,
    justify=LEFT,
    textvariable=E_Vada,
)
txtVada.grid(row=4, column=2)
txtHerbalc = Entry(
    Drinks_F,
    font=("arial", 16, "bold"),
    bd=8,
    width=12,
    justify=LEFT,
    textvariable=E_Herbalc,
)
txtHerbalc.grid(row=5, column=2)
txtHerbalt = Entry(
    Drinks_F,
    font=("arial", 16, "bold"),
    bd=8,
    width=12,
    justify=LEFT,
    textvariable=E_Herbalt,
)
txtHerbalt.grid(row=6, column=2)
txtIce = Entry(
    Drinks_F,
    font=("arial", 16, "bold"),
    bd=8,
    width=12,
    justify=LEFT,
    textvariable=E_Ice,
)
txtIce.grid(row=7, column=2)


# Entry Box For Meals
txtChole_Bhature = Entry(
    Cake_F,
    font=("arial", 16, "bold"),
    bd=8,
    width=12,
    justify=LEFT,
    textvariable=E_Chole_Bhature,
)

txtChole_Bhature.grid(row=0, column=2)
txtPasta = Entry(
    Cake_F,
    font=("arial", 16, "bold"),
    bd=8,
    width=12,
    justify=LEFT,
    textvariable=E_Pasta,
)
txtPasta.grid(row=1, column=2)
txtSambar = Entry(
    Cake_F,
    font=("arial", 16, "bold"),
    bd=8,
    width=12,
    justify=LEFT,
    textvariable=E_Sambar,
)
txtSambar.grid(row=2, column=2)
txtPizza = Entry(
    Cake_F,
    font=("arial", 16, "bold"),
    bd=8,
    width=12,
    justify=LEFT,
    textvariable=E_Pizza,
)
txtPizza.grid(row=3, column=2)
txtCake = Entry(
    Cake_F,
    font=("arial", 16, "bold"),
    bd=8,
    width=12,
    justify=LEFT,
    textvariable=E_Cake,
)
txtCake.grid(row=4, column=2)
txtManchurian = Entry(
    Cake_F,
    font=("arial", 16, "bold"),
    bd=8,
    width=12,
    justify=LEFT,
    textvariable=E_Manchurian,
)
txtManchurian.grid(row=5, column=2)
txtHakka = Entry(
    Cake_F,
    font=("arial", 16, "bold"),
    bd=8,
    width=12,
    justify=LEFT,
    textvariable=E_Hakka,
)
txtHakka.grid(row=6, column=2)
txtPaneer = Entry(
    Cake_F,
    font=("arial", 16, "bold"),
    bd=8,
    width=12,
    justify=LEFT,
    textvariable=E_Paneer,
)
txtPaneer.grid(row=7, column=2)

# Total Cost
lbCost = Label(
    Cost_F, font=("arial", 14, "bold"), text="Cost of Drinks\t  ", bg="Yellow"
)
lbCost.grid(row=0, column=0, sticky=W)
txtCost = Entry(
    Cost_F,
    font=("arial", 14, "bold"),
    bd=7,
    bg="White",
    insertwidth=2,
    justify=RIGHT,
    textvariable=Cost,
)
txtCost.grid(row=0, column=1)
lbACost = Label(
    Cost_F, font=("arial", 14, "bold"), text="Cost of Meals \t  ", bg="Yellow"
)
lbACost.grid(row=1, column=0, sticky=W)
txtACost = Entry(
    Cost_F,
    font=("arial", 14, "bold"),
    bd=7,
    bg="White",
    insertwidth=2,
    justify=RIGHT,
    textvariable=ACost,
)
txtACost.grid(row=1, column=1)
lbSC = Label(Cost_F, font=("arial", 14, "bold"), text="Service Charge  ", bg="Yellow")
lbSC.grid(row=2, column=0, sticky=W)
txtSC = Entry(
    Cost_F,
    font=("arial", 14, "bold"),
    bd=7,
    bg="White",
    insertwidth=2,
    justify=RIGHT,
    textvariable=SC,
)
txtSC.grid(row=2, column=1)
lbPT = Label(Cost_F, font=("arial", 14, "bold"), text="\tPaid Tax", bg="Yellow")
lbPT.grid(row=0, column=2, sticky=W)
txtPT = Entry(
    Cost_F,
    font=("arial", 14, "bold"),
    bd=7,
    bg="White",
    insertwidth=2,
    justify=RIGHT,
    textvariable=PT,
)
txtPT.grid(row=0, column=3)

lbSCost = Label(Cost_F, font=("arial", 14, "bold"), text="\tSub Total", bg="Yellow")
lbSCost.grid(row=1, column=2, sticky=W)
txtSCost = Entry(
    Cost_F,
    font=("arial", 14, "bold"),
    bd=7,
    bg="White",
    insertwidth=2,
    justify=RIGHT,
    textvariable=SCost,
)
txtSCost.grid(row=1, column=3)
lbTCost = Label(Cost_F, font=("arial", 14, "bold"), text="\tTotal Cost ", bg="Yellow")
lbTCost.grid(row=2, column=2, sticky=W)
txtTCost = Entry(
    Cost_F,
    font=("arial", 14, "bold"),
    bd=7,
    bg="White",
    insertwidth=2,
    justify=RIGHT,
    textvariable=TCost,
)
txtTCost.grid(row=2, column=3)


# Receipt
txtReceipt = Text(Receipt_F, width=59, bg="white", bd=4, font=("arial", 12, "bold"))
txtReceipt.grid(row=0, column=0)
# Buttons
btnTotal = Button(
    Buttons_F,
    padx=16,
    pady=1,
    bd=7,
    fg="Black",
    font=("arial", 12, "bold"),
    width=10,
    text="Total",
    bg="Orange",
    command=CostofItem,
).grid(row=0, column=0)
btnReceipt = Button(
    Buttons_F,
    padx=16,
    pady=1,
    bd=7,
    fg="Black",
    font=("arial", 12, "bold"),
    width=8,
    text="Receipt",
    bg="Orange",
    command=Reciept,
).grid(row=0, column=1)

btnReset = Button(
    Buttons_F,
    padx=16,
    pady=1,
    bd=7,
    fg="Black",
    font=("arial", 12, "bold"),
    width=8,
    text="Reset",
    bg="Orange",
    command=Reset,
).grid(row=0, column=2)

btnExit = Button(
    Buttons_F,
    padx=16,
    pady=1,
    bd=7,
    fg="Black",
    font=("arial", 12, "bold"),
    width=8,
    text="Exit",
    bg="Orange",
    command=iExit,
).grid(row=0, column=3)

# For Meal
Chole_Bhature = Checkbutton(
    Cake_F,
    text="Chole Bhature    ",
    variable=var9,
    onvalue=1,
    offvalue=0,
    font=("arial", 16, "bold"),
    bg="Orange",
    command=chkChole,
).grid(row=0, sticky=W)
Pasta = Checkbutton(
    Cake_F,
    text="Pasta    ",
    variable=var10,
    onvalue=1,
    offvalue=0,
    font=("arial", 16, "bold"),
    bg="Orange",
    command=chkPasta,
).grid(row=1, sticky=W)
Sambar = Checkbutton(
    Cake_F,
    text="Sambar Idli/Dosa(Plain)   ",
    variable=var11,
    onvalue=1,
    offvalue=0,
    font=("arial", 16, "bold"),
    bg="Orange",
    command=chkSambar,
).grid(row=2, sticky=W)
Pizza = Checkbutton(
    Cake_F,
    text="Cheese Pizza",
    variable=var12,
    onvalue=1,
    offvalue=0,
    font=("arial", 16, "bold"),
    bg="Orange",
    command=chkPizza,
).grid(row=3, sticky=W)
Cake = Checkbutton(
    Cake_F,
    text="Cake",
    variable=var13,
    onvalue=1,
    offvalue=0,
    font=("arial", 16, "bold"),
    bg="Orange",
    command=chkCake,
).grid(row=4, sticky=W)
Manchurian = Checkbutton(
    Cake_F,
    text="Manchurian Rice",
    variable=var14,
    offvalue=0,
    font=("arial", 16, "bold"),
    onvalue=1,
    bg="Orange",
    command=chkManchurian,
).grid(row=5, sticky=W)
Hakka = Checkbutton(
    Cake_F,
    text="Hakka Noodeles",
    variable=var15,
    onvalue=1,
    offvalue=0,
    font=("arial", 16, "bold"),
    bg="Orange",
    command=chkHakka,
).grid(row=6, sticky=W)
Panner = Checkbutton(
    Cake_F,
    text="Panner 65",
    variable=var16,
    onvalue=1,
    offvalue=0,
    font=("arial", 16, "bold"),
    bg="Orange",
    command=chkPanner,
).grid(row=7, sticky=W)

# For Home Delivery
Full = Checkbutton(
    Cal_F,
    text="Name",
    variable=var17,
    onvalue=1,
    offvalue=0,
    font=("arial", 16, "bold"),
    bg="Yellow",
    command=chkFull,
).grid(row=0, sticky=W)
Address = Checkbutton(
    Cal_F,
    text="Address",
    variable=var18,
    onvalue=1,
    offvalue=0,
    font=("arial", 16, "bold"),
    bg="Yellow",
    command=chkAddress,
).grid(row=1, sticky=W)
Pin = Checkbutton(
    Cal_F,
    text="Pincode  ",
    variable=var19,
    onvalue=1,
    offvalue=0,
    font=("arial", 16, "bold"),
    bg="Yellow",
    command=chkPin,
).grid(row=2, sticky=W)
Phone = Checkbutton(
    Cal_F,
    text="Phone no:      ",
    variable=var20,
    onvalue=1,
    offvalue=0,
    font=("arial", 16, "bold"),
    bg="Yellow",
    command=chkPhone,
).grid(row=3, sticky=W)

txtFull = Entry(
    Cal_F, font=("arial", 12, "bold"), bd=8, width=40, justify=LEFT, textvariable=E_Full
)
txtFull.grid(row=0, column=2)
txtAddress = Entry(
    Cal_F,
    font=("arial", 12, "bold"),
    bd=8,
    width=40,
    justify=LEFT,
    textvariable=E_Address,
)
txtAddress.grid(row=1, column=2)
txtPin = Entry(
    Cal_F, font=("arial", 12, "bold"), bd=8, width=40, justify=LEFT, textvariable=E_Pin
)
txtPin.grid(row=2, column=2)
txtPhone = Entry(
    Cal_F,
    font=("arial", 12, "bold"),
    bd=8,
    width=40,
    justify=LEFT,
    textvariable=E_Phone,
)
txtPhone.grid(row=3, column=2)

root.mainloop()
