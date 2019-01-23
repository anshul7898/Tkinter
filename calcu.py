import tkinter as Tk
import math
class Calculator:
    '''main class that constructs the calc and preforms the calculations'''

    def __init__(self, master):
        # Global variables needed throughout a single calculation
        self.top_string = ''    # string for label at top of calculator
        self.number1 = 0       # storage of first number selected
        self.number2 = 0       # storage of second number selected
        self.add = False       # + boolean
        self.subtract = False  # - boolean
        self.multiply = False  # x boolean
        self.divide = False  # / boolean
        self.square = False  # X2 boolean
        self.cube   = False  # X3 boolean
        self.root   = False  # root boolean 
        self.pi     = False  # PI boolean
        self.factorial = False # ! boolean
        self.logg   = False  # log boolean
        self.logE   = False  # log E boolean
        self.sign   = False  # Sin boolean
        self.cosign = False  # Cos boolean
        self.tann   = False  # Tan boolean
        self.signinv = False # sin-1 boolean
        self.cosinv = False  # Cos-1 boolean
        self.taninv = False  # Tan-1 boolean
        self.radian = False  #Radian boolean
        self.angle = False  # Angle boolean
        self.power = False  # Power Boolean
    

        # Top Label Layout
        self.label = Tk.Label(master, text='0', bg='blue', fg='white', height=4, width=15)
        self.label.grid(row=0, column=0, columnspan=9, sticky=Tk.N+Tk.E+Tk.S+Tk.W)
        self.label.config(font='Verdana 16 bold')

        # Button Layout
        Tk.Button(master, text='1', height=2, width=6, command=lambda: self.number_pressed(1)).grid(row=1, column=0)
        Tk.Button(master, text='2', height=2, width=6, command=lambda: self.number_pressed(2)).grid(row=1, column=1)
        Tk.Button(master, text='3', height=2, width=6, command=lambda: self.number_pressed(3)).grid(row=1, column=2)
        Tk.Button(master, text='4', height=2, width=6, command=lambda: self.number_pressed(4)).grid(row=2, column=0)
        Tk.Button(master, text='5', height=2, width=6, command=lambda: self.number_pressed(5)).grid(row=2, column=1)
        Tk.Button(master, text='6', height=2, width=6, command=lambda: self.number_pressed(6)).grid(row=2, column=2)
        Tk.Button(master, text='7', height=2, width=6, command=lambda: self.number_pressed(7)).grid(row=3, column=0)
        Tk.Button(master, text='8', height=2, width=6, command=lambda: self.number_pressed(8)).grid(row=3, column=1)
        Tk.Button(master, text='9', height=2, width=6, command=lambda: self.number_pressed(9)).grid(row=3, column=2)
        Tk.Button(master, text='0', command=lambda: self.number_pressed(0)).grid(row=4, columnspan=2, sticky=Tk.N+Tk.E+Tk.S+Tk.W)
        Tk.Button(master, text='+', height=2, width=6, command=lambda: self.sign_pressed("+")).grid(row=1, column=3)
        Tk.Button(master, text='-', height=2, width=6, command=lambda: self.sign_pressed("-")).grid(row=2, column=3)
        Tk.Button(master, text='x', height=2, width=6, command=lambda: self.sign_pressed("*")).grid(row=3, column=3)
        Tk.Button(master, text='x2', height=2, width=6, command=lambda: self.sign_pressed("x2")).grid(row=2, column=4)
        Tk.Button(master, text='x3', height=2, width=6, command=lambda: self.sign_pressed("x3")).grid(row=3, column=4)
        Tk.Button(master, text='/', height=2, width=6, command=lambda: self.sign_pressed("/")).grid(row=4, column=3)
        Tk.Button(master, text='rooot', height=2, width=6, command=lambda: self.sign_pressed("rooot")).grid(row=1, column=4)
        Tk.Button(master, text='log10', height=2, width=6, command=lambda: self.sign_pressed("log10")).grid(row=1, column=5)
        Tk.Button(master, text='logbaseE', height=2, width=6, command=lambda: self.sign_pressed("logbaseE")).grid(row=2, column=5)
        Tk.Button(master, text='pie', height=2, width=6, command=lambda: self.sign_pressed("pie")).grid(row=4, column=4)
        Tk.Button(master, text='Sin', height=2, width=6, command=lambda: self.sign_pressed("Sin")).grid(row=3, column=5)
        Tk.Button(master, text='Tan', height=2, width=6, command=lambda: self.sign_pressed("Tan")).grid(row=5, column=5)
        Tk.Button(master, text='Sin1', height=2, width=6, command=lambda: self.sign_pressed("Sin1")).grid(row=1, column=6)
        Tk.Button(master, text='Tan1', height=2, width=6, command=lambda: self.sign_pressed("Tan1")).grid(row=3, column=6)
        Tk.Button(master, text='Radian', height=2, width=6, command=lambda: self.sign_pressed("Radian")).grid(row=4, column=6)
        Tk.Button(master, text='Power', height=2, width=6, command=lambda: self.sign_pressed("Power")).grid(row=1, column=7)
        Tk.Button(master, text='Angle', height=2, width=6, command=lambda: self.sign_pressed("Angle")).grid(row=5, column=6)
        Tk.Button(master, text='Cos1', height=2, width=6, command=lambda: self.sign_pressed("Cos1")).grid(row=2, column=6)
        Tk.Button(master, text='Cos', height=2, width=6, command=lambda: self.sign_pressed("Cos")).grid(row=4, column=5)
        Tk.Button(master, text='C', height=2, width=6, command=self.clear_all).grid(row=4, column=2)
        Tk.Button(master, text='!', height=2, width=6, command=lambda: self.sign_pressed("!")).grid(row=5, column=4)
        Tk.Button(master, text='=', height=2, command=self.equals).grid(row=5, columnspan=4, sticky=Tk.N+Tk.E+Tk.S+Tk.W)

    def number_pressed(self, button_number):
        ''' This function is triggered when buttons 0 - 9 are pushed '''
        if self.number1 is 0 and not any([self.add, self.subtract, self.multiply, self.divide, self.root, self.logE, self.sign, self.cosign, self.tann, self.signinv, self.cosinv, self.taninv, self.radian, self.angle, self.power]):
            self.number1 = button_number
            self.top_string = str(button_number)
            self.label.config(text=str(button_number))

        elif self.number1 is not 0 and not any([self.add, self.subtract, self.multiply, self.divide, self.root, self.logE, self.sign, self.cosign, self.tann, self.signinv, self.cosinv, self.taninv,  self.radian, self.angle, self.power]):
            self.top_string += str(button_number)
            self.number1 = float(self.top_string)
            self.label.config(text=self.top_string)

        elif self.number2 is 0:
            self.number2 = button_number
            self.top_string = str(button_number)
            self.label.config(text=str(button_number))

        elif self.number1 is not 0:
            self.top_string += str(button_number)
            self.number2 = float(self.top_string)
            self.label.config(text=self.top_string)


    def sign_pressed(self, sign):
        ''' This function is triggered when +,-,*, or / is pushed. First check num1 and num2 are already storage.
        If so, it performs an num1 equals total, then displays num1, then resets the sign to the last on pushed.
        Which allows for multiply calculations before pushing = button '''
        if self.number2 is not 0 and self.number1 is not 0:
            self.number1 = self.equals()
            self.label.config(text=str(self.number1))
            self.top_string = ''
        if sign is "+":
            self.add = True
            self.subtract = False  # - boolean
            self.multiply = False  # x boolean
            self.divide = False
            self.square = False
            self.cube = False
            self.root = False
            self.pi = False
            self.logg = False
            self.radian = False
            self.angle = False 
            self.logE = False
            self.sign = False
            self.cosign = False
            self.power = False
            self.tann   = False
            self.signinv = False
            self.cosinv = False
            self.taninv = False
        if sign is "-":
            self.add = False
            self.subtract = True  # - boolean
            self.multiply = False  # x boolean
            self.divide = False
            self.square = False
            self.cube = False
            self.root = False
            self.power = False
            self.angle = False
            self.pi = False
            self.logg = False
            self.logE = False
            self.sign = False
            self.cosign = False
            self.radian = False
            self.signinv = False
            self.cosinv = False
            self.taninv = False
            self.tann   = False 
        if sign is "*":
            self.add = False
            self.subtract = False  # - boolean
            self.multiply = True  # x boolean
            self.divide = False
            self.square = False
            self.cube = False
            self.root = False
            self.pi = False
            self.power = False
            self.angle = False
            self.cosinv = False
            self.signinv = False
            self.logg = False
            self.radian = False
            self.logE = False
            self.taninv = False
            self.sign = False
            self.tann   = False 
            self.cosign = False 
        if sign is "/":
            self.add = False
            self.subtract = False  # - boolean
            self.multiply = False  # x boolean
            self.divide = True
            self.square = False
            self.cube = False
            self.signinv = False
            self.root = False
            self.pi = False
            self.angle = False
            self.power = False
            self.cosinv = False
            self.radian = False
            self.logE = False
            self.logg = False
            self.tann   = False
            self.taninv = False
            self.sign = False
            self.cosign = False 
        if sign is "x2":
            self.add = False
            self.subtract = False  # - boolean
            self.square = True  # x boolean
            self.divide = False
            self.multiply = False
            self.cube = False
            self.radian = False
            self.signinv = False
            self.logE = False
            self.angle = False
            self.power = False
            self.cosinv = False
            self.tann   = False
            self.taninv = False
            self.root = False
            self.pi = False
            self.logg = False
            self.sign = False
            self.cosign = False 
        if sign is "x3":
            self.add = False
            self.subtract = False  # - boolean
            self.square = False  # x boolean
            self.divide = False
            self.radian = False
            self.signinv = False
            self.multiply = False
            self.cube = True
            self.root = False 
            self.logE = False
            self.taninv = False
            self.pi = False
            self.power = False
            self.angle = False
            self.cosinv = False
            self.tann   = False 
            self.logg = False
            self.sign = False
            self.cosign = False 
        if sign is "rooot":
            self.add = False
            self.subtract = False  # - boolean
            self.square = False  # x boolean
            self.signinv = False
            self.divide = False
            self.taninv = False
            self.logE = False
            self.radian = False
            self.multiply = False
            self.tann   = False 
            self.cube = False
            self.root = True
            self.power = False
            self.cosinv = False
            self.pi = False
            self.logg = False
            self.sign = False
            self.angle = False
            self.cosign = False 

        if sign is "pie":
            self.add = False
            self.subtract = False  # - boolean
            self.square = False  # x boolean
            self.logE = False
            self.tann   = False 
            self.divide = False
            self.signinv = False
            self.multiply = False
            self.cube = False
            self.angle = False
            self.radian = False
            self.cosinv = False
            self.root = False
            self.pi = True
            self.taninv = False
            self.logg = False
            self.sign = False
            self.power = False
            self.cosign = False 
        if sign is "log":
            self.add = False
            self.subtract = False  # - boolean
            self.square = False  # x boolean
            self.divide = False
            self.signinv = False
            self.logE = False
            self.angle = False
            self.cosinv = False
            self.tann   = False
            self.radian = False
            self.multiply = False
            self.cube = False
            self.root = False
            self.pi = False
            self.logg = True
            self.power = False
            self.sign = False
            self.cosign = False
            self.taninv = False
        if sign is "logbaseE":
            self.add = False
            self.subtract = False  # - boolean
            self.square = False  # x boolean
            self.divide = False
            self.radian = False
            self.multiply = False
            self.signinv = False
            self.cube = False
            self.root = False
            self.cosinv = False
            self.pi = False
            self.angle = False
            self.tann   = False 
            self.logg = False
            self.logE = True
            self.sign = False
            self.power = False
            self.cosign = False
            self.taninv = False
        if sign is "Sin":
            self.add = False
            self.subtract = False  # - boolean
            self.multiply = False  # x boolean
            self.signinv = False
            self.divide = False
            self.square = False
            self.cosinv = False
            self.cube = False
            self.angle = False
            self.root = False
            self.pi = False
            self.radian = False
            self.logg = False
            self.power = False
            self.taninv = False
            self.logE = False
            self.tann   = False 
            self.sign = False
            self.sign = True
            self.cosign = False 
        if sign is "Cos":
            self.add = False
            self.subtract = False  # - boolean
            self.multiply = False  # x boolean
            self.divide = False
            self.square = False
            self.angle = False
            self.power = False
            self.taninv = False
            self.signinv = False
            self.cube = False
            self.radian = False
            self.cosinv = False
            self.root = False
            self.pi = False
            self.logg = False
            self.logE = False
            self.tann   = False
            self.sign = False
            self.taninv = False
            self.cosign = True
        if sign is "Tan":
            self.add = False
            self.subtract = False  # - boolean
            self.multiply = False  # x boolean
            self.divide = False
            self.angle = False
            self.square = False
            self.signinv = False
            self.cube = False
            self.power = False
            self.radian = False
            self.cosinv = False
            self.root = False
            self.pi = False
            self.logg = False
            self.logE = False
            self.tann   = True
            self.sign = False
            self.taninv = False
            self.cosign = False
            
        if sign is "Sin1":
            self.add = False
            self.subtract = False  # - boolean
            self.multiply = False  # x boolean
            self.divide = False
            self.cosinv = False
            self.angle = False
            self.square = False
            self.signinv = True
            self.taninv = False
            self.radian = False
            self.cube = False
            self.power = False
            self.root = False
            self.pi = False
            self.logg = False
            self.logE = False
            self.tann   = False
            self.sign = False
            self.cosign = False
            
        if sign is "Cos1":
            self.add = False
            self.subtract = False  # - boolean
            self.multiply = False  # x boolean
            self.divide = False
            self.square = False
            self.cube = False
            self.root = False
            self.power = False
            self.angle = False
            self.taninv = False
            self.radian = False
            self.pi = False
            self.logg = False
            self.logE = False
            self.sign = False
            self.cosign = False
            self.tann   = False
            self.signinv = False
            self.cosinv = True
            
        if sign is "Tan1":
            self.add = False
            self.subtract = False  # - boolean
            self.multiply = False  # x boolean
            self.divide = False
            self.square = False
            self.angle = False
            self.cube = False
            self.power = False
            self.root = False
            self.taninv = True
            self.radian = False
            self.pi = False
            self.logg = False
            self.logE = False
            self.sign = False
            self.cosign = False
            self.tann   = False
            self.signinv = False
            self.cosinv = False
        
        if sign is "Radian":
            self.add = False
            self.subtract = False  # - boolean
            self.multiply = False  # x boolean
            self.divide = False
            self.square = False
            self.angle = False
            self.power = False
            self.cube = False
            self.root = False
            self.taninv = False
            self.radian = True
            self.pi = False
            self.logg = False
            self.logE = False
            self.sign = False
            self.cosign = False
            self.tann   = False
            self.signinv = False
            self.cosinv = False
        
        
        if sign is "Angle":
            self.add = False
            self.subtract = False  # - boolean
            self.multiply = False  # x boolean
            self.divide = False
            self.square = False
            self.angle = True
            self.cube = False
            self.power = False
            self.root = False
            self.taninv = False
            self.radian = False
            self.pi = False
            self.logg = False
            self.logE = False
            self.sign = False
            self.cosign = False
            self.tann   = False
            self.signinv = False
            self.cosinv = False
        
        if sign is "Angle":
            self.add = False
            self.subtract = False  # - boolean
            self.multiply = False  # x boolean
            self.divide = False
            self.square = False
            self.angle = False
            self.cube = False
            self.power = True
            self.root = False
            self.taninv = False
            self.radian = False
            self.pi = False
            self.logg = False
            self.logE = False
            self.sign = False
            self.cosign = False
            self.tann   = False
            self.signinv = False
            self.cosinv = False
        
        
             
            
        else:
            if sign is "+":
                self.add = True
            if sign is "-":
                self.subtract = True
            if sign is "*":
                self.multiply = True
            if sign is "/":
                self.divide = True
            if sign is "x2":
                self.square = True
            if sign is "x3":
                self.cube = True
            if sign is "rooot":
                self.root = True
            if sign is "pie":
                self.pi = True
            if sign is "log10":
                self.logg = True
            if sign is "logbaseE":
                self.logE = True
            if sign is "Sin":
                self.sing = True
            if sign is "Cos":
                self.cosign = True
            if sign is "Tan":
                self.tann = True
            if sign is "Sin1":
                self.signinv = True
            if sign is "Cos1":
                self.cosinv = True
            if sign is "Tan1":
                self.taninv = True
            if sign is "Radian":
                self.radian = True
            if sign is "Angle":
                self.angle = True
            if sign is "Power":
                self.power = True
            
    def equals(self):
        ''' Triggers calculation then clears all vars '''
        total = 0
        if self.add is True:
            total = self.number1 + self.number2
            self.number2 = 0    # resets for next calculation if clear is not presses

        elif self.subtract is True:
            total = self.number1 - self.number2
            self.number2 = 0

        elif self.multiply is True:
            total = self.number1 * self.number2
            self.number2 = 0

        elif self.divide is True:
            total = round(self.number1 / self.number2, 3)
            total = int(total) if total.is_integer() else total
            self.number2 = 0
            
        elif self.square is True:
            total = self.number1 * self.number1
            self.number1 = 0
            
        elif self.cube is True:
            total = self.number1 * self.number1 * self.number1
            self.number1 = 0

        elif self.root is True:
            total = math.sqrt(self.number1)
            self.number1 = 0

        elif self.pi is True:
            total = math.pi*self.number1
            self.number1 = 0
        elif self.logg is True:
            total = math.log10(self.number1)
            self.number1 = 0
            
        elif self.logE is True:
            total = math.log(self.number1)
            self.number1 = 0

        elif self.sign is True:
            total = math.sin(self.number1)
            self.number1 = 0
            
        elif self.cosign is True:
            total = math.cos(self.number1)
            self.number1 = 0

        elif self.tann is True:
            total = math.tan(self.number1)
            self.number1 = 0
            
        elif self.signinv is True:
            total = math.asinh(self.number1)
            self.number1 = 0
            
        elif self.cosinv is True:
            total = math.acosh(self.number1)
            self.number1 = 0
        elif self.taninv is True:
            total = math.tanh(self.number1)
            self.number1 = 0
        elif self.radian is True:
            total = self.number1*0.017453292519943
        elif self.angle is True:
            total = self.number1*57.2957795130823
        elif self.power is True:
            total = self.number1*(self.number1*self.number2)
            
        self.top_string = ''
        self.add = False
        self.subtract = False
        self.multiply = False
        self.divide = False
        self.square = False
        self.cube = False
        self.root = False
        self.pi = False
        self.logg = False
        self.logE = False
        self.sign = False
        self.cosign = False
        self.power = False
        self.tann = False
        self.taninv = False
        self.signinv = False
        self.cosinv = False
        self.radian = False
        self.angle = False
        self.label.config(text=str(total))
        return total

    def clear_all(self):
        '''Clears all vars'''
        self.top_string = ''    # first string to appear after selecting sign ( 9 + )
        self.number1 = 0       # storage of first number selected
        self.number2 = 0       # storage of second number selected
        self.add = False       # + boolean
        self.subtract = False  # - boolean
        self.multiply = False  # x boolean
        self.divide = False    # / boolean
        self.square = False    # X2 boolean
        self.cube = False      # X3 boolean
        self.root = False      # root boolean
        self.pi = False        # PI boolen
        self.logg = False      # log boolean
        self.logE = False      # log base e boolean
        self.sign = False      # SIN boolean
        self.cosign = False    # Cos boolean
        self.tann = False      # Tan boolean
        self.signinv = False     # Sin-1 boolean
        self.cosinv = False      # Cos-1 boolean
        self.taninv = False      # Tan-1 boolean
        self.radian = False      # Radian boolean
        self.angle = False       # Angle boolean
        self.power = False       # Power boolean  
        self.label.config(text='0')  # top label

if __name__ == '__main__':
    ROOT = Tk.Tk()
    ROOT.wm_title('Calculator')
    ROOT.resizable(width=False, height=False)
    Calculator(ROOT)
    ROOT.mainloop()
