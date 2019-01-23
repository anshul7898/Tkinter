from tkinter import*
def Temprature():
  temp = int((var.get() - 32) * 5 / 9)
  convert = str(temp) + "% Celsius"
  lable2.configure(text = convert)

root = Tk()
root.title("Temprature Converter")
root.resizable(0,0)

var = DoubleVar()

lable1 = Label(root, text = "Temprature Converter\n Fahrenheit to Celsius", padx=16,pady=16,bd=16,
               fg="#000000", font=('arial',30,'bold'),bg="sky blue", relief='raised', width = 20,
               height =3)
lable1.pack()
slider = Scale(root, variable = var,from_=-40, to = 300, length = 500,tickinterval = 20 ,orient = HORIZONTAL)
slider.pack(anchor = CENTER)
lable2 = Label(root, text = "", padx=16,pady=16,bd=16,
               fg="#000000", font=('arial',30,'bold'),bg="sky blue", relief='sunk', width = 20,
               height =3)
lable2.pack()
lable3 = Label(root, text = "")
lable3.pack()



button = Button(root, text="Convert to Celsius",padx=16,pady=16,bd=16,width=20,font=('arial',20,'bold'), command = Temprature)
button.pack(anchor = CENTER)




root.mainloop()
