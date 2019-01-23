import random
import time;
import datetime
import random
import tkinter.messagebox
from tkinter import*
root = Tk()
root.geometry("1350x750+0+0")
root.title("HOTEL MANAGEMENT SYSTEM")
root.configure(background = 'Cadet Blue')
def iExit():
  iExit =tkinter.messagebox.askyesno("Exit Restaurant","CONFIRM if you want to EXIT")
  if iExit > 0:
    root.destroy()
    return
def Reset():
    
  E_Latta.set("0") 
  E_Espresso.set("0") 
  E_Iced_Latta.set("0") 
  E_Vale_Coffee.set("0") 
  E_Cappuccino.set("0") 
  E_Africen_Coffee.set("0")  
  E_American_Coffee.set("0") 
  E_Iced_Cappuccino.set("0")
  DateofOrder.set("0") 
  Recipt_Ref.set("0") 
  PaidTax.set("0") 
  SubTotal.set("0")
  TotalCost.set("0")
  CostofCakes.set("0")
  CostofDrinks.set("0")
  ServiceCharge.set("0")
  text_Input.set("0")
  E_School_Cake.set("0") 
  E_Sunney_AO_Cake.set("0")
  E_Jonathan_YO_Cake.set("0")
  E_West_African_Cake.set("0")
  E_Lagos_Chocolate_Cake.set("0")
  E_kilburn_Chocolate_Cake.set("0")
  E_Carlton_Hill_Chocolate_Cake.set("0")
  E_Queen_Park_Chocolate_Cake.set("0")
  Recipt_Ref.set("0")
  
  
  
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

  txtLatta.configure(state = DISABLED)
  txtEspresso.configure(state = DISABLED)
  txtIced_Latta.configure(state = DISABLED)
  txtVale_Coffee.configure(state = DISABLED)
  txtCappuccino.configure(state = DISABLED)
  txtAfrican_Coffee.configure(state = DISABLED)
  txtAmerican_Coffee.configure(state = DISABLED)
  txtIced_Cappuccino.configure(state = DISABLED)
  txtSchool_Cake.configure(state = DISABLED)
  txtSunny_AO_Cake.configure(state = DISABLED)
  txtJhonathan_YO_Cake.configure(state = DISABLED)
  txtWest_African_Cake.configure(state = DISABLED)
  txtLagos_Chocolate_Cake.configure(state = DISABLED)
  txtKilburn_Chocolate_Cake.configure(state = DISABLED)
  txtCarlton_Hill_Chocolate_Cake.configure(state = DISABLED)
  txtQueen_Park_Chocolate_Cake.configure(state = DISABLED)

def CostofItem():
  Item1=float(E_Latta.get())
  Item2=float(E_Espresso.get())
  Item3=float(E_Iced_Latta.get())
  Item4=float(E_Vale_Coffee.get())
  Item5=float(E_Cappuccino.get())
  Item6=float(E_Africen_Coffee.get())
  Item7=float(E_American_Coffee.get())
  Item8=float(E_Iced_Cappuccino.get())
  Item9=float(E_School_Cake.get())
  Item10=float(E_Sunney_AO_Cake.get())
  Item11=float(E_Jonathan_YO_Cake.get())
  Item12=float(E_West_African_Cake.get())
  Item13=float(E_Lagos_Chocolate_Cake.get())
  Item14=float(E_kilburn_Chocolate_Cake.get())
  Item15=float(E_Carlton_Hill_Chocolate_Cake.get())
  Item16=float(E_Queen_Park_Chocolate_Cake.get())
  PriceofDrinks = (Item1 * 1.2) + (Item2 * 1.99) + (Item3 * 2.05) + (Item4 * 1.89) + (Item5 * 2.99) + (Item6 * 1.99) + (Item7 * 2.39) + (Item8 * 1.29)
  PriceofCakes = (Item9 * 1.35) +(Item10 * 2.2) +(Item11 * 1.99) +(Item12 * 1.49) +(Item13 * 1.8) +(Item14 * 1.67) +(Item15 * 1.6) +(Item16 * 1.99)
  DrinksPrice = "$", str('%.2f'%(PriceofDrinks))
  CakesPrice = "$", str('%.2f'%(PriceofCakes))
  CostofCakes.set(CakesPrice)
  CostofDrinks.set(DrinksPrice)
  SC="$", str('%.2f'%(1.59))
  ServiceCharge.set(SC)
  SubTotalofITEMS = "$", str('%.2f'%(PriceofDrinks + PriceofCakes + 1.59))
  SubTotal.set(SubTotalofITEMS)
  Tax ="$", str('%.2f'%((PriceofDrinks + PriceofCakes + 1.59)*0.15))
  PaidTax.set(Tax)
  TT = ((PriceofDrinks + PriceofCakes + 1.59)*0.15)
  TC ="$", str('%.2f'%(PriceofDrinks + PriceofCakes + 1.59 + TT))
  TotalCost.set(TC)

def chkLatta():
  if(var1.get() == 1):
    txtLatta.configure(state = NORMAL)
    txtLatta.focus()
    txtLatta.delete('0',END)
    E_Latta.set("")
  elif(var1.get()== 0):
    txtLatta.configure(state = DISABLED)
    E_Latta.set("0")

def chkEspresso():
  if(var2.get() == 1):
    txtEspresso.configure(state = NORMAL)
    txtEspresso.focus()
    txtEspresso.delete('0',END)
    E_Espresso.set("")
  elif(var2.get()==0):
    txtEspresso.configure(state = DISABLED)
    E_Espresso.set("0")

def chkIced_Latta():
  if(var3.get() == 1):
    txtIced_Latta.configure(state = NORMAL)
    txtIced_Latta.focus()
    txtIced_Latta.delete('0',END)
    E_Iced_Latta.set("")
  elif(var3.get()==0):
    txtIced_Latta.configure(state = DISABLED)
    E_Iced_Latta.set("0")

def chkVale_Coffee():
  if(var4.get() == 1):
    txtVale_Coffee.configure(state = NORMAL)
    txtVale_Coffee.focus()
    txtVale_Coffee.delete('0',END)
    E_Vale_Coffee.set("")
  elif(var4.get() == 0):
    txtVale_Coffee.configure(state = DISABLED)
    E_Vale_Coffee.set("0")

def chkCappuccino():
  if(var5.get() == 1):
    txtCappuccino.configure(state = NORMAL)
    txtCappuccino.focus()
    txtCappuccino.delete('0',END)
    E_Cappuccino.set("")
  elif(var5.get()==0):
    txtCappuccino.configure(state = DISABLED)
    E_Cappuccino.set("0")

def chkAfrican_Coffee():
  if(var6.get() == 1):
    txtAfrican_Coffee.configure(state = NORMAL)
    txtAfrican_Coffee.focus()
    txtAfrican_Coffee.delete('0',END)
    E_Africen_Coffee.set("")
  elif(var6.get() == 0):
    txtAfrican_Coffee.configure(state = DISABLED)
    E_Africen_Coffee.set("0")

def chkAmerican_Coffee():
  if(var7.get() == 1):
    txtAmerican_Coffee.configure(state = NORMAL)
    txtAmerican_Coffee.focus()
    txtAmerican_Coffee.delete('0',END)
    E_American_Coffee.set("")
  elif(var7.get() == 0):
    txtAmerican_Coffee.configure(state = DISABLED)
    E_American_Coffee.set("0")

def chkIced_Cappuccino():
  if(var8.get() == 1):
    txtIced_Cappuccino.configure(state = NORMAL)
    txtIced_Cappuccino.focus()
    txtIced_Cappuccino.delete('0',END)
    E_Iced_Cappuccino.set("")
  elif(var8.get() == 0):
    txtIced_Cappuccino.configure(state = DISABLED)
    E_Iced_Cappuccino.set("0")

def chkSchool_Cake():
  if(var9.get() == 1):
    txtSchool_Cake.configure(state = NORMAL)
    txtSchool_Cake.focus()
    txtSchool_Cake.delete('0',END)
    E_School_Cake.set("")
  elif(var9.get() == 0):
    txtSchool_Cake.configure(state = DISABLED)
    E_School_Cake.set("0")

def chkSunney_AO_Cake():
  if(var10.get() == 1):
    txtSunny_AO_Cake.configure(state = NORMAL)
    txtSunny_AO_Cake.focus()
    txtSunny_AO_Cake.delete('0',END)
    E_Sunney_AO_Cake.set("")
  elif(var10.get() == 0):
    txtSunny_AO_Cake.configure(state = DISABLED)
    E_Sunney_AO_Cake.set("0")

def chkJonathan_YO_Cake():
  if(var11.get() == 1):
    txtJhonathan_YO_Cake.configure(state = NORMAL)
    txtJhonathan_YO_Cake.focus()
    txtJhonathan_YO_Cake.delete('0',END)
    E_Jonathan_YO_Cake.set("")
  elif(var11.get() == 0):
    txtJhonathan_YO_Cake.configure(state = DISABLED)
    E_Jonathan_YO_Cake.set("0")

def chkWest_African_Cake():
  if(var12.get() == 1):
    txtWest_African_Cake.configure(state = NORMAL)
    txtWest_African_Cake.focus()
    txtWest_African_Cake.delete('0',END)
    E_West_African_Cake.set("")
  elif(var12.get() == 0):
    txtWest_African_Cake.configure(state = DISABLED)
    E_West_African_Cake.set("0")

def chkLagos_Chocolate_Cake():
  if(var13.get() == 1):
    txtLagos_Chocolate_Cake.configure(state = NORMAL)
    txtLagos_Chocolate_Cake.focus()
    txtLagos_Chocolate_Cake.delete('0',END)
    E_Lagos_Chocolate_Cake.set("")
  elif(var13.get() == 0):
    txtLagos_Chocolate_Cake.configure(state = DISABLED)
    E_Lagos_Chocolate_Cake.set("0")

def chkKilburn_Chocolate_Cake():
  if(var14.get() == 1):
    txtKilburn_Chocolate_Cake.configure(state = NORMAL)
    txtKilburn_Chocolate_Cake.focus()
    txtKilburn_Chocolate_Cake.delete('0',END)
    E_kilburn_Chocolate_Cake.set("")
  elif(var14.get() == 0):
    txtKilburn_Chocolate_Cake.configure(state = DISABLED)
    E_kilburn_Chocolate_Cake.set("0")

def chkCarlton_Hill_Chocolate_Cake():
  if(var15.get() == 1):
    txtCarlton_Hill_Chocolate_Cake.configure(state = NORMAL)
    txtCarlton_Hill_Chocolate_Cake.focus()
    txtCarlton_Hill_Chocolate_Cake.delete('0',END)
    E_Carlton_Hill_Chocolate_Cake.set("")
  elif(var15.get() == 0):
    txtCarlton_Hill_Chocolate_Cake.configure(state = DISABLED)
    E_Carlton_Hill_Chocolate_Cake.set("0")

def chkQueen_Park_Chocolate_Cake():
  if(var16.get() == 1):
    txtQueen_Park_Chocolate_Cake.configure(state = NORMAL)
    txtQueen_Park_Chocolate_Cake.focus()
    txtQueen_Park_Chocolate_Cake.delete('0',END)
    E_Queen_Park_Chocolate_Cake.set("")
  elif(var16.get() == 0):
    txtQueen_Park_Chocolate_Cake.configure(state = DISABLED)
    E_Queen_Park_Chocolate_Cake.set("0")
   
    
def Recipt():
  txtReceipt.delete("1.0",END)
  x = random.randint(10903, 609235)
  randomRef = str(x)
  Recipt_Ref.set("BILL" + randomRef)
  txtReceipt.insert(END, 'RECIPT REF:\t\t\t' +Recipt_Ref.get()+'\t'+DateofOrder.get()+"\n")
  txtReceipt.insert(END, 'ITEM:\t\t\t'+ "COST OF ITEM""\n")
  txtReceipt.insert(END, 'LATTA:\t\t\t'+ E_Latta.get()+"\n")
  txtReceipt.insert(END, 'Espresso:\t\t\t'+E_Espresso.get()+"\n")
  txtReceipt.insert(END, 'Iced Latta:\t\t\t'+E_Iced_Latta.get()+"\n")
  txtReceipt.insert(END, 'Vale Coffee:\t\t\t'+E_Vale_Coffee.get()+"\n")
  txtReceipt.insert(END, 'Cappuccino:\t\t\t'+E_Cappuccino.get()+"\n")
  txtReceipt.insert(END, 'African Coffee:\t\t\t'+E_Africen_Coffee.get()+"\n")
  txtReceipt.insert(END, 'American Coffee:\t\t\t'+E_American_Coffee.get()+"\n")
  txtReceipt.insert(END, 'Iced Cappuccino:\t\t\t'+E_Iced_Cappuccino.get()+"\n")
  txtReceipt.insert(END, 'School Cake:\t\t\t'+ E_School_Cake.get()+"\n")
  txtReceipt.insert(END, 'Sunny AO Cake:\t\t\t'+ E_Sunney_AO_Cake.get()+"\n")
  txtReceipt.insert(END, 'Jonathan O Cake:\t\t\t'+E_Jonathan_YO_Cake.get()+"\n")
  txtReceipt.insert(END, 'West Africa Chocolate Cake:\t\t\t'+ E_West_African_Cake.get()+"\n")
  txtReceipt.insert(END, 'Lagos Chocolate Cake:\t\t\t'+E_Lagos_Chocolate_Cake.get()+"\n")
  txtReceipt.insert(END, 'Kilburn Chocolate Cake:\t\t\t'+ E_kilburn_Chocolate_Cake.get()+"\n")
  txtReceipt.insert(END, 'Carlton Hill Chocolate Cake:\t\t\t'+E_Carlton_Hill_Chocolate_Cake.get()+"\n")
  txtReceipt.insert(END, 'Queens Park Chocolate Cake:\t\t\t'+E_Queen_Park_Chocolate_Cake.get()+"\n")
  txtReceipt.insert(END, 'Cost of Drinks:\t\t\t'+CostofDrinks.get()+'\nTax Paid:\t\t\t\t' + PaidTax.get()+"\n")
  txtReceipt.insert(END, 'Cost of Cakes:\t\t\t'+ CostofCakes.get()+'\nSubTotal:\t\t\t\t' + str(SubTotal.get()) + "\n")
  txtReceipt.insert(END, 'SerVice Charge:\t\t\t'+ServiceCharge.get()+'\nTotal Cost:\t\t\t\t' +str(TotalCost.get()))
      

def btnClick(numbers):
  global operator
  operator = operator + str(numbers)
  text_Input.set(operator)

def btnClearDisplay():
  global operator
  operator=""
  text_Input.set("")


Tops = Frame(root, bg ='Cadet Blue',bd = 20, pady=5, relief=RIDGE)
Tops.pack(side=TOP)

MenueFrame = Frame(root, bg ='Cadet Blue',bd = 10,relief=RIDGE)
MenueFrame.pack(side=LEFT)

ReciptCal_F = Frame(root, bg ='powder Blue',bd = 10,relief=RIDGE)
ReciptCal_F.pack(side=RIGHT)

lblTitle = Label(Tops, font=('arial',60,'bold'),text="HOTEL MANAGEMENT SYSTEM", bd=21,bg='Cadet Blue',
                 fg='Cornsilk', justify=CENTER)
lblTitle.grid(row=0,column=0)

Buttons_F = Frame(ReciptCal_F, bg='powder Blue', bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)


Cal_F = Frame(ReciptCal_F, bg='powder Blue', bd=6, relief=RIDGE )
Cal_F.pack(side=TOP)


Recipt_F = Frame(ReciptCal_F, bg='powder Blue', bd=4, relief=RIDGE )
Recipt_F.pack(side=BOTTOM)


MenueFrame = Frame(root, bg ='Cadet Blue',bd = 10,relief=RIDGE)
MenueFrame.pack(side=LEFT)
Drinks_F = Frame(MenueFrame, bg='Cadet Blue', bd=10)
Drinks_F.pack(side=TOP)
Cost_F = Frame(MenueFrame, bg='powder Blue', bd=4)
Cost_F.pack(side=BOTTOM)



Drinks_F = Frame(MenueFrame, bg='powder Blue', bd=10,relief=RIDGE)
Drinks_F.pack(side=LEFT)


Cakes_F = Frame(MenueFrame, bg='powder Blue', bd=10, relief=RIDGE)
Cakes_F.pack(side=RIGHT)
#===============================================Variables========================================
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

DateofOrder = StringVar()
Recipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakes = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator =""

E_Latta = StringVar()
E_Espresso = StringVar()
E_Iced_Latta = StringVar()
E_Vale_Coffee = StringVar()
E_Cappuccino = StringVar()
E_Africen_Coffee = StringVar()
E_American_Coffee = StringVar()
E_Iced_Cappuccino = StringVar()

E_School_Cake = StringVar()
E_Sunney_AO_Cake = StringVar()
E_Jonathan_YO_Cake = StringVar()
E_West_African_Cake = StringVar()
E_Lagos_Chocolate_Cake = StringVar()
E_kilburn_Chocolate_Cake = StringVar()
E_Carlton_Hill_Chocolate_Cake = StringVar()
E_Queen_Park_Chocolate_Cake = StringVar()


E_Latta.set("0") 
E_Espresso.set("0") 
E_Iced_Latta.set("0") 
E_Vale_Coffee.set("0") 
E_Cappuccino.set("0") 
E_Africen_Coffee.set("0")
E_American_Coffee.set("0") 
E_Iced_Cappuccino.set("0")

E_School_Cake.set("0") 
E_Sunney_AO_Cake.set("0")
E_Jonathan_YO_Cake.set("0")
E_West_African_Cake.set("0")
E_Lagos_Chocolate_Cake.set("0")
E_kilburn_Chocolate_Cake.set("0")
E_Carlton_Hill_Chocolate_Cake.set("0")
E_Queen_Park_Chocolate_Cake.set("0")



DateofOrder.set(time.strftime("%d/%m/%Y"))

#===============================================================Drinks=============
Latta = Checkbutton(Drinks_F, text="Latta", variable = var1, onvalue = 1, offvalue=0, font=('arial',18,'bold'),
                    bg='powder Blue',command = chkLatta).grid(row=0, sticky=W)

Espresso = Checkbutton(Drinks_F, text="Espresso", variable = var2, onvalue = 1, offvalue=0, font=('arial',18,'bold'),
                    bg='powder Blue',command = chkEspresso).grid(row=1, sticky=W)

Iced_Latta = Checkbutton(Drinks_F, text="Iced Latta", variable = var3, onvalue = 1, offvalue=0, font=('arial',18,'bold'),
                    bg='powder Blue',command = chkIced_Latta).grid(row=2, sticky=W)

Vale_Coffee = Checkbutton(Drinks_F, text="Vale Coffee", variable = var4, onvalue = 1, offvalue=0, font=('arial',18,'bold'),
                    bg='powder Blue',command = chkVale_Coffee).grid(row=3, sticky=W)

Cappuccino = Checkbutton(Drinks_F, text=" Cappuccino", variable = var5, onvalue = 1, offvalue=0, font=('arial',18,'bold'),
                    bg='powder Blue',command = chkCappuccino).grid(row=4, sticky=W)

African_Coffee = Checkbutton(Drinks_F, text="African Coffee", variable = var6, onvalue = 1, offvalue=0, font=('arial',18,'bold'),
                    bg='powder Blue',command = chkAfrican_Coffee).grid(row=5, sticky=W)

American_Coffee = Checkbutton(Drinks_F, text="American Coffee", variable = var7, onvalue = 1, offvalue=0, font=('arial',18,'bold'),
                    bg='powder Blue',command =chkAmerican_Coffee).grid(row=6, sticky=W)

Iced_Cappuccino = Checkbutton(Drinks_F, text="Iced Cappuccino", variable = var8, onvalue = 1, offvalue=0, font=('arial',18,'bold'),
                    bg='powder Blue',command = chkIced_Cappuccino).grid(row=7, sticky=W)





#===============================================================Entry Box for Drinks=============
txtLatta = Entry(Drinks_F,font=('arial',16,'bold'), bd=8, width=6, justify=LEFT, textvariable = E_Latta,state= DISABLED)
txtLatta.grid(row=0,column=1)
txtEspresso = Entry(Drinks_F,font=('arial',16,'bold'), bd=8, width=6, justify=LEFT, state= DISABLED,textvariable = E_Espresso)
txtEspresso.grid(row=1,column=1)
txtIced_Latta = Entry(Drinks_F,font=('arial',16,'bold'), bd=8, width=6, justify=LEFT, state= DISABLED,textvariable = E_Iced_Latta )
txtIced_Latta.grid(row=2,column=1)


txtVale_Coffee = Entry(Drinks_F,font=('arial',16,'bold'), bd=8, width=6, justify=LEFT, state= DISABLED,textvariable = E_Vale_Coffee)
txtVale_Coffee.grid(row=3,column=1)

txtCappuccino = Entry(Drinks_F,font=('arial',16,'bold'), bd=8, width=6, justify=LEFT, state= DISABLED,textvariable = E_Cappuccino)
txtCappuccino.grid(row=4,column=1)


txtAfrican_Coffee = Entry(Drinks_F,font=('arial',16,'bold'), bd=8, width=6, justify=LEFT, state= DISABLED,textvariable = E_Africen_Coffee)
txtAfrican_Coffee.grid(row=5,column=1)



txtAmerican_Coffee = Entry(Drinks_F,font=('arial',16,'bold'), bd=8, width=6, justify=LEFT, state= DISABLED,textvariable = E_American_Coffee)
txtAmerican_Coffee.grid(row=6,column=1)

txtIced_Cappuccino = Entry(Drinks_F,font=('arial',16,'bold'), bd=8, width=6, justify=LEFT, state= DISABLED,textvariable = E_Iced_Cappuccino)
txtIced_Cappuccino.grid(row=7,column=1)

#===============================================================Cakes==========================================

SchoolCake = Checkbutton(Cakes_F, text="School Cake\t\t\t", variable = var9, onvalue = 1, offvalue=0, font=('arial',18,'bold'),
                    bg='powder Blue',command = chkSchool_Cake).grid(row=0, sticky=W)

Sunny_AO_Cake = Checkbutton(Cakes_F, text="Sunday AO Cake", variable = var10, onvalue = 1, offvalue=0, font=('arial',18,'bold'),
                    bg='powder Blue',command = chkSunney_AO_Cake).grid(row=1, sticky=W)

Jonathan_Yo_Cake = Checkbutton(Cakes_F, text="Jonathan o Cake", variable = var11, onvalue = 1, offvalue=0, font=('arial',18,'bold'),
                    bg='powder Blue',command = chkJonathan_YO_Cake).grid(row=2, sticky=W)

West_African_Cake = Checkbutton(Cakes_F, text="West African cake", variable = var12, onvalue = 1, offvalue=0, font=('arial',18,'bold'),
                    bg='powder Blue',command = chkWest_African_Cake).grid(row=3, sticky=W)

Lagos_Chocolate_Cake = Checkbutton(Cakes_F, text="Lagos Chocolate Cake", variable = var13, onvalue = 1, offvalue=0, font=('arial',18,'bold'),
                    bg='powder Blue',command = chkLagos_Chocolate_Cake).grid(row=4, sticky=W)

Kilburn_Chocolate_Cake = Checkbutton(Cakes_F, text="Kilburn Chocolate Cake", variable = var14, onvalue = 1, offvalue=0, font=('arial',18,'bold'),
                    bg='powder Blue',command = chkKilburn_Chocolate_Cake).grid(row=5, sticky=W)

Carlton_Hill_Cake = Checkbutton(Cakes_F, text="Carlton Hill Cake", variable = var15, onvalue = 1, offvalue=0, font=('arial',18,'bold'),
                    bg='powder Blue',command = chkCarlton_Hill_Chocolate_Cake).grid(row=6, sticky=W)

Queen_Park_Cake = Checkbutton(Cakes_F, text="Queen Park Cake", variable = var16, onvalue = 1, offvalue=0, font=('arial',18,'bold'),
                    bg='powder Blue',command = chkQueen_Park_Chocolate_Cake).grid(row=7, sticky=W)

#===============================================================Entry Box for Cakes=========================================================
txtSchool_Cake = Entry(Cakes_F,font=('arial',16,'bold'), bd=8, width=4, justify=LEFT, state= DISABLED,textvariable = E_School_Cake)
txtSchool_Cake.grid(row=0,column=1)
txtSunny_AO_Cake = Entry(Cakes_F,font=('arial',16,'bold'), bd=8, width=4, justify=LEFT, state= DISABLED,textvariable = E_Sunney_AO_Cake)
txtSunny_AO_Cake.grid(row=1,column=1)
txtJhonathan_YO_Cake = Entry(Cakes_F,font=('arial',16,'bold'), bd=8, width=4, justify=LEFT, state= DISABLED,textvariable = E_Jonathan_YO_Cake)
txtJhonathan_YO_Cake.grid(row=2,column=1)


txtWest_African_Cake = Entry(Cakes_F,font=('arial',16,'bold'), bd=8, width=4, justify=LEFT, state= DISABLED,textvariable = E_West_African_Cake)
txtWest_African_Cake.grid(row=3,column=1)

txtLagos_Chocolate_Cake = Entry(Cakes_F,font=('arial',16,'bold'), bd=8, width=4, justify=LEFT, state= DISABLED,textvariable = E_Lagos_Chocolate_Cake)
txtLagos_Chocolate_Cake.grid(row=4,column=1)


txtKilburn_Chocolate_Cake= Entry(Cakes_F,font=('arial',16,'bold'), bd=8, width=4, justify=LEFT, state= DISABLED,textvariable = E_kilburn_Chocolate_Cake)
txtKilburn_Chocolate_Cake.grid(row=5,column=1)



txtCarlton_Hill_Chocolate_Cake = Entry(Cakes_F,font=('arial',16,'bold'), bd=8, width=4, justify=LEFT, state= DISABLED,textvariable = E_Carlton_Hill_Chocolate_Cake)
txtCarlton_Hill_Chocolate_Cake.grid(row=6,column=1)

txtQueen_Park_Chocolate_Cake = Entry(Cakes_F,font=('arial',16,'bold'), bd=8, width=4, justify=LEFT, state= DISABLED,textvariable = E_Queen_Park_Chocolate_Cake)
txtQueen_Park_Chocolate_Cake.grid(row=7,column=1)



#==============================================TOTAL COST============================================================
lblCostofDrinks = Label(Cost_F, font=('arial',14,'bold'),text="Cost of Drinks\t  ",bg='powder Blue',fg='black')
lblCostofDrinks.grid(row=0,column=0,sticky=W)
txtCostofDrinks = Entry(Cost_F,font=('arial',14,'bold'),bd=7,bg="white",
                        insertwidth=2,justify=RIGHT,textvariable = CostofDrinks)
txtCostofDrinks.grid(row=0,column=1)

lblCostofCakes = Label(Cost_F, font=('arial',14,'bold'),text="Cost of Cakes",bg='powder Blue',fg='black')
lblCostofCakes.grid(row=1,column=0,sticky=W)
txtCostofCakes = Entry(Cost_F,font=('arial',14,'bold'),bd=7,bg="white",
                        insertwidth=2,justify=RIGHT,textvariable = CostofCakes)
txtCostofCakes.grid(row=1,column=1)



lblServiceCharge = Label(Cost_F, font=('arial',14,'bold'),text="SERVICE CHARGE",bg='powder Blue',fg='black')
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge = Entry(Cost_F,font=('arial',14,'bold'),bd=7,bg="white",
                        insertwidth=2,justify=RIGHT,textvariable = ServiceCharge)
txtServiceCharge.grid(row=2,column=1)

#==============================================PAYMENT INFO=================================================================
lblPaidTax = Label(Cost_F, font=('arial',14,'bold'),text="Paid TAX\t  ",bg='powder Blue',fg='black')
lblPaidTax.grid(row=0,column=2,sticky=W)
txtPaidTax = Entry(Cost_F,font=('arial',14,'bold'),bd=7,bg="white",
                        insertwidth=2,justify=RIGHT,textvariable = PaidTax)
txtPaidTax.grid(row=0,column=3)

lblSubTotal = Label(Cost_F, font=('arial',14,'bold'),text="Sub-Total",bg='powder Blue',fg='black')
lblSubTotal.grid(row=1,column=2,sticky=W)
txtSubTotal = Entry(Cost_F,font=('arial',14,'bold'),bd=7,bg="white",
                        insertwidth=2,justify=RIGHT,textvariable = SubTotal)
txtSubTotal.grid(row=1,column=3)

lblTotalCost = Label(Cost_F, font=('arial',14,'bold'),text="Total-Cost",bg='powder Blue',fg='black')
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost = Entry(Cost_F,font=('arial',14,'bold'),bd=7,bg="white",
                        insertwidth=2,justify=RIGHT,textvariable = TotalCost)
txtTotalCost.grid(row=2,column=3)

#==============================================RECIPT=======================================================================
txtReceipt = Text(Recipt_F, width=43, height=12, bg="white",bd=4,font=('arial',12,'bold'))
txtReceipt.grid(row=0,column=0)

#==============================================BUTTONS======================================================================

btn7 = Button(Cal_F, padx=16, pady=1, bd= 7, fg="black",font=('arial',16,'bold'),width = 4, text="7", command=lambda: btnClick(7)).grid(row=2,column=0)
btn8 = Button(Cal_F, padx=16, pady=1, bd= 7, fg="black",font=('arial',16,'bold'),width = 4, text="8",command=lambda: btnClick(8)).grid(row=2,column=1)
btn9 = Button(Cal_F, padx=16, pady=1, bd= 7, fg="black",font=('arial',16,'bold'),width = 4, text="9",command=lambda: btnClick(9)).grid(row=2,column=2)
btnAdd = Button(Cal_F, padx=16, pady=1, bd= 7, fg="black",font=('arial',16,'bold'),width = 4, text="+",bg="powder blue",command=lambda: btnClick("+")).grid(row=2,column=3)
btn4 = Button(Cal_F, padx=16, pady=1, bd= 7, fg="black",font=('arial',16,'bold'),width = 4, text="4",command=lambda: btnClick(4)).grid(row=3,column=0)
btn5 = Button(Cal_F,padx=16,pady=1,bd= 7,fg="black",font=('arial',16,'bold'),width=4,text="5",command=lambda: btnClick(5)).grid(row=3,column=1)
btn6 = Button(Cal_F, padx=16, pady=1, bd= 7, fg="black",font=('arial',16,'bold'),width = 4, text="6",command=lambda: btnClick(6)).grid(row=3,column=2)
btnSub = Button(Cal_F, padx=16, pady=1, bd= 7, fg="black",font=('arial',16,'bold'),width = 4, text="-",bg="powder blue",command=lambda: btnClick("-")).grid(row=3,column=3)
btn1 = Button(Cal_F, padx=16, pady=1, bd= 7, fg="black",font=('arial',16,'bold'),width = 4, text="1",command=lambda: btnClick(1)).grid(row=4,column=0)
btn2 = Button(Cal_F, padx=16, pady=1, bd= 7, fg="black",font=('arial',16,'bold'),width = 4, text="2",command=lambda: btnClick(2)).grid(row=4,column=1)
btn3 = Button(Cal_F, padx=16, pady=1, bd= 7, fg="black",font=('arial',16,'bold'),width = 4, text="3",command=lambda: btnClick(3)).grid(row=4,column=2)
btnMul = Button(Cal_F, padx=16, pady=1, bd= 7, fg="black",font=('arial',16,'bold'),width = 4, text="*",bg="powder blue",command=lambda: btnClick("*")).grid(row=4,column=3)
btn0 = Button(Cal_F, padx=16, pady=1, bd= 7, fg="black",font=('arial',16,'bold'),width = 4, text="0",command=lambda: btnClick(0)).grid(row=5,column=0)
btnClear = Button(Cal_F, padx=16, pady=1, bd= 7, fg="black",font=('arial',16,'bold'),width = 4, text="C",bg="powder blue",command=btnClearDisplay).grid(row=5,column=1)
btnDivide = Button(Cal_F, padx=16, pady=1, bd= 7, fg="black",font=('arial',16,'bold'),width = 4, text="/",bg="powder blue",command=lambda: btnClick("/")).grid(row=5,column=3)
btnEquals = Button(Cal_F,padx=16,pady=1,bd=7, fg="black", font=('arial',16,'bold'),width = 4,
            text="=", bg="powder blue").grid(row=5, column=2)

#====================================CALCULATOR DISP============================================
txtDisplay = Entry(Cal_F,width=46,bg="white",bd=4,font=('arial',12,'bold'),justify=RIGHT)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")
#====================================CALCULATOR BUTTONS============================================
btnTotal = Button(Buttons_F, padx=10, pady=1, bd= 7, fg="black",font=('arial',16,'bold'),width = 4,height=1,text="TOTAL",bg="powder blue",command = CostofItem).grid(row=0,column=0)
btnRecipt = Button(Buttons_F, padx=10, pady=1, bd= 7, fg="black",font=('arial',16,'bold'),width = 4,height=1,text="RECIPT",bg="powder blue",command = Recipt).grid(row=0,column=1)
btnReset = Button(Buttons_F, padx=10, pady=1, bd= 7, fg="black",font=('arial',16,'bold'),width = 4,height=1,text="RESET",bg="powder blue",command = Reset).grid(row=0,column=2)
btnExit = Button(Buttons_F, padx=10, pady=1, bd= 7, fg="black",font=('arial',16,'bold'),width = 4,height=1,text="EXIT",bg="powder blue",command = iExit).grid(row=0,column=3)

root.mainloop()
