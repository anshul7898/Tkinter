from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime


def main():
  root1 = Tk()
  app = SalesLogin(root1)

class SalesLogin:
  def  __init__(self, master):
    self.master = master
    self.master.title("Sales management system")
    self.master.geometry("1350x750+0+0")
    self.master.config(bg = 'cadet blue')
    self.frame = Frame(self.master, bg ='cadet blue')
    self.frame.pack()

    self.Username = StringVar()
    self.Password = StringVar()
    self.lblTitle = Label(self.frame, text = 'Sales Management Login', font=('arial', 60,'bold'),
                          bg='cadet Blue', fg ='Cornsilk')
    self.lblTitle.grid(row = 0, column = 0, columnspan = 2, pady = 20)
    #====================================================FRAME=============================================
    self.LoginFrame1 = LabelFrame(self.frame , width=1350, height=300,text="Login", font=('arial',20,'bold'),relief='ridge',bg='cadet blue', bd=40)
    self.LoginFrame1.grid(row=1,column=0)
    self.LoginFrame2 = LabelFrame(self.frame, width=1000, height=200,text="Log", font=('arial',20,'bold'),relief='ridge',bg='cadet blue', bd=40)
    self.LoginFrame2.grid(row=2,column=0)


    
    #======================================================================================================
    self.lblUsername = Label(self.LoginFrame1,text='UserName',font=('arial',30,'bold'),bd=22,
                             bg='cadet Blue', fg='Cornsilk')
    self.lblUsername.grid(row=0, column=0)

    self.txtUsername = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=7,textvariable=self.Username,width=33)
    self.txtUsername.grid(row=0,column=1,padx=88)
    self.lblPassword = Label(self.LoginFrame1,text='Password',font=('arial',30,'bold'),bd=22,
                             bg='cadet Blue', fg='Cornsilk')
    self.lblPassword.grid(row=1, column=0)

    self.txtPassword = Entry(self.LoginFrame1,font=('arial',30,'bold'),show='*',bd=7,textvariable=self.Password,width=33)
    self.txtPassword.grid(row=1,column=1,columnspan=2,padx=30)
    


    #======================================================================================================
    self.btnLogin = Button(self.LoginFrame2, text='Login', width = 15, font=('arial',30,'bold'),bg='cadet Blue', fg='Cornsilk',command = self.Login_Syatem)
    self.btnLogin.grid(row=3,column=0,pady=20,padx=8)
    self.btnReset1 = Button(self.LoginFrame2, text='Reset', width = 15, font=('arial',30,'bold'),bg='cadet Blue', fg='Cornsilk',command = self.iReset)
    self.btnReset1.grid(row=3,column=1,pady=20,padx=8)
    self.btnExit1 = Button(self.LoginFrame2, text='Exit', width = 15, font=('arial',30,'bold'),bg='cadet Blue', fg='Cornsilk',command = self.iExit)
    self.btnExit1.grid(row=3,column=2,pady=20,padx=8)
   
   



    #=======================================================================================================


  def Login_Syatem(self):
    user = (self.Username.get())
    pas = (self.Password.get())
    if(user == str('anshul') and pas == str('auditt7898')):
      self.Login_window()
    else:
      tkinter.messagebox.askyesno("Sales management system", "INVALID LOGIN")
      self.Username.set("")
      self.Password.set("")

  def iExit(self):
    self.iExit = tkinter.messagebox.askyesno("Sales Login System", "Confirm if you want to Exit")
    if self.iExit > 0:
      self.master.destroy()
      return 


  def iReset(self):
    self.Username.set("")
    self.Password.set("")
    


    
  
  def Login_window(self):
    self.SalesWindow = Toplevel(self.master)
    self.app = SalesManagement(self.SalesWindow)

class SalesManagement:
  def  __init__(self, master):
    self.master = master
    self.master.title("Sales management system")
    self.master.geometry("1350x750+0+0")
    self.master.config(bg = 'cadet blue')
    self.frame = Frame(self.master, bg ='cadet blue')
    self.frame.pack()
    #===========================================================================================================
    



    #===========================================================================================================
if __name__== '__main__':
  main()
    
