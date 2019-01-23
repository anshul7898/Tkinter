from tkinter import*
import tkinter.messagebox
#import  LibBksDatabase


class Library:
  def __init__(self,root):
    
    self.root = root
    self.root.title("Library Database Management System")
    self.root.geometry("1350x750+0+0")


    MTy = StringVar()
    Ref = StringVar()
    Tit = StringVar()
    fna = StringVar()
    sna = StringVar()
    Adr1 = StringVar()
    Adr2 = StringVar()
    pcd = StringVar()
    MNo = StringVar()
    BkID = StringVar()
    Bkt = StringVar()
    BkT = StringVar()
    Atr = StringVar()
    DBo = StringVar()
    Ddu = StringVar()
    sPr = StringVar()
    LrF = StringVar()
    DoD = StringVar()
    DonL = StringVar()

    
    #=======================================FN declareation=====================================
    def iExit():
      iExit = tkinter.messagebox.askyesno("Library Database Management System",
                                          "Confirm if you want to Exit")
      if iExit > 0:
        root.destroy()
        return

    def ClaearData():
      self.txtMType.delete(0,END)
      self.txtBkID.delete(0,END)
      self.txtRef.delete(0,END)
      self.txtTit.delete(0,END)
      self.txtfna.delete(0,END)
      self.txtsna.delete(0,END)
      self.txtAdr1.delete(0,END)
      self.txtAdr2.delete(0,END)
      self.txtpcd.delete(0,END)
      self.txtMNo.delete(0,END)
      self.txtBkID.delete(0,END)
      self.txtBkt.delete(0,END)
      self.txtAtr.delete(0,END)
      self.txtDBo.delete(0,END)
      self.txtDdu.delete(0,END)
      self.txtsPr.delete(0,END)
      self.txtLrF.delete(0,END)
      self.txtDoD.delete(0,END)
      self.txtDonL.delete(0,END)

    def addData():
      if(len(MTy.get())!=0):
        LibBksDatabase.addDataRec(MTy.get(), Ref.get(), Tit.get(), fna.get(),sna.get(),Adr1.get(),Adr2.get(),pcd.get(),MNo.get(),BkID.get(),
                                  Bkt.get(),MType.get(),BkT.get(), Atr.get(),DBo.get(),Ddu.get(),sPr.get(),LrF.get(),DoD.get(),DonL.get())
        booklist.delete(0,END)
        booklist.insert(END,(MTy.get(), Ref.get(), Tit.get(), fna.get(),sna.get(),Adr1.get(),Adr2.get(),pcd.get(),MNo.get(),BkID.get(),
                             Bkt.get(),MType.get(),BkT.get(), Atr.get(),DBo.get(),Ddu.get(),sPr.get(),LrF.get(),DoD.get(),DonL.get()))
      
      


    
    #=======================================FRAMES=====================================
    MainFrame = Frame(self.root)
    MainFrame.grid()

    TitFrame = Frame(MainFrame, bd=2, padx = 40, pady=8, bg="Cadet blue", relief = RIDGE)
    TitFrame.pack(side = TOP)

    self.lblTit = Label(TitFrame, font=('arial',46,'bold'),text="Library Database Management System")
    self.lblTit.grid(sticky=W)

    ButtonFrame = Frame(MainFrame, bd = 2, width=1350, height = 100, padx=20, bg = "Cadet Blue",relief=RIDGE)
    ButtonFrame.pack(side=BOTTOM)

    FrameDetail = Frame(MainFrame, bd=0, width=1350, height = 50, padx=20, relief=RIDGE)
    FrameDetail.pack(side=BOTTOM)

    DataFrame = Frame(MainFrame, bd=1, width = 1300, height = 400, padx=20, pady=20, relief=RIDGE)
    DataFrame.pack(side=BOTTOM)

    DataFrameLEFT = LabelFrame(DataFrame, bd=1, width = 800 , height = 300, padx=20, relief=RIDGE, font=('arial',12,'bold'), text="Library Management Info:",bg="Cadet Blue")
    DataFrameLEFT.pack(side=LEFT)

    DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width = 450, height = 300, padx=20, pady=3, relief=RIDGE,font=('arial',12,'bold'),bg="Cadet Blue",text="Book Details:")
    DataFrameRIGHT.pack(side=RIGHT)

    
 #=======================================LABLES and Entry=====================================
    self.lblMemberType = Label(DataFrameLEFT, font=('arial',12,'bold'),text="Member Type", padx=2, pady=2,bg="Cadet Blue")
    self.lblMemberType.grid(row=0, column=0,sticky=W)
    self.txtMType = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=MTy,width=25)
    self.txtMType.grid(row=0, column=1)

    self.lblBkID = Label(DataFrameLEFT, font=('arial',12,'bold'),text="BOOK ID", padx=2, pady=2,bg="Cadet Blue")
    self.lblBkID.grid(row=0, column=2,sticky=W)
    self.txtBkID = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=BkID,width=25)
    self.txtBkID.grid(row=0, column=3)

    self.lblRef = Label(DataFrameLEFT, font=('arial',12,'bold'),text="Refrence No:", padx=2, pady=2,bg="Cadet Blue")
    self.lblRef.grid(row=1, column=0,sticky=W)
    self.txtRef = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=Ref,width=25)
    self.txtRef.grid(row=1, column=1)

    self.lblBkt = Label(DataFrameLEFT, font=('arial',12,'bold'),text="Book Title:", padx=2, pady=2,bg="Cadet Blue")
    self.lblBkt.grid(row=1, column=2,sticky=W)
    self.txtBkt = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable = Bkt,width=25)
    self.txtBkt.grid(row=1, column=3)

    self.lblTit = Label(DataFrameLEFT, font=('arial',12,'bold'),text="Title:", padx=2, pady=2,bg="Cadet Blue")
    self.lblTit.grid(row=2, column=0,sticky=W)
    self.txtTit = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable = Tit,width=25)
    self.txtTit.grid(row=2, column=1)

    self.lblAtr = Label(DataFrameLEFT, font=('arial',12,'bold'),text="Author", padx=2, pady=2,bg="Cadet Blue")
    self.lblAtr.grid(row=2, column=2,sticky=W)
    self.txtAtr = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable = Atr,width=25)
    self.txtAtr.grid(row=2, column=3)

    self.lblfna = Label(DataFrameLEFT, font=('arial',12,'bold'),text="FirstName:", padx=2, pady=2,bg="Cadet Blue")
    self.lblfna.grid(row=3, column=0,sticky=W)
    self.txtfna = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable = fna,width=25)
    self.txtfna.grid(row=3, column=1)

    
    self.lblDBo = Label(DataFrameLEFT, font=('arial',12,'bold'),text="Date of Borrowed:", padx=2, pady=2,bg="Cadet Blue")
    self.lblDBo.grid(row=3, column=2,sticky=W)
    self.txtDBo = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable = DBo,width=25)
    self.txtDBo.grid(row=3, column=3)

    self.lblsna = Label(DataFrameLEFT, font=('arial',12,'bold'),text="Surname:", padx=2, pady=2,bg="Cadet Blue")
    self.lblsna.grid(row=4, column=0,sticky=W)
    self.txtsna = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable = sna,width=25)
    self.txtsna.grid(row=4, column=1)

    self.lblDdu = Label(DataFrameLEFT, font=('arial',12,'bold'),text="Due Date", padx=2, pady=2,bg="Cadet Blue")
    self.lblDdu.grid(row=4, column=2,sticky=W)
    self.txtDdu = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable = Ddu,width=25)
    self.txtDdu.grid(row=4, column=3)

    self.lblAdr1 = Label(DataFrameLEFT, font=('arial',12,'bold'),text="Address1 :", padx=2, pady=2,bg="Cadet Blue")
    self.lblAdr1.grid(row=5, column=0,sticky=W)
    self.txtAdr1 = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable = Adr1,width=25)
    self.txtAdr1.grid(row=5, column=1)

    self.lblDonL = Label(DataFrameLEFT, font=('arial',12,'bold'),text="Days on Loan", padx=2, pady=2,bg="Cadet Blue")
    self.lblDonL.grid(row=5, column=2,sticky=W)
    self.txtDonL = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable = DonL,width=25)
    self.txtDonL.grid(row=5, column=3)

    self.lblAdr2 = Label(DataFrameLEFT, font=('arial',12,'bold'),text="Address2 :", padx=2, pady=2,bg="Cadet Blue")
    self.lblAdr2.grid(row=6, column=0,sticky=W)
    self.txtAdr2 = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable = Adr2,width=25)
    self.txtAdr2.grid(row=6, column=1)

    self.lblLrF = Label(DataFrameLEFT, font=('arial',12,'bold'),text="Late Return Fees", padx=2, pady=2,bg="Cadet Blue")
    self.lblLrF.grid(row=6, column=2,sticky=W)
    self.txtLrF = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable = LrF,width=25)
    self.txtLrF.grid(row=6, column=3)

    self.lblpcd = Label(DataFrameLEFT, font=('arial',12,'bold'),text="Post Code:", padx=2, pady=2,bg="Cadet Blue")
    self.lblpcd.grid(row=7, column=0,sticky=W)
    self.txtpcd = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable = pcd,width=25)
    self.txtpcd.grid(row=7, column=1)

    self.lblDoD = Label(DataFrameLEFT, font=('arial',12,'bold'),text="Date over Due:", padx=2, pady=2,bg="Cadet Blue")
    self.lblDoD.grid(row=7, column=2,sticky=W)
    self.txtDoD = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable = DoD,width=25)
    self.txtDoD.grid(row=7, column=3)

    self.lblMNo = Label(DataFrameLEFT, font=('arial',12,'bold'),text="Mobile Number:", padx=2, pady=2,bg="Cadet Blue")
    self.lblMNo.grid(row=8, column=0,sticky=W)
    self.txtMNo = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable = MNo,width=25)
    self.txtMNo.grid(row=8, column=1)

    self.lblsPr = Label(DataFrameLEFT, font=('arial',12,'bold'),text="Selling Price:", padx=2, pady=2,bg="Cadet Blue")
    self.lblsPr.grid(row=8, column=2,sticky=W)
    self.txtsPr = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable = sPr,width=25)
    self.txtsPr.grid(row=8, column=3)
    #=======================================ListBoc and Scrollbar=====================================


    scrollbar = Scrollbar(DataFrameRIGHT)
    scrollbar.grid(row=0,column = 1,sticky='ns')

    booklist = Listbox(DataFrameRIGHT,width=45, height = 12, font=('arial',12,'bold'),yscrollcommand = scrollbar.set)
    booklist.grid(row=0,column = 0, padx=8)
    scrollbar.config(command = booklist.yview)

     #=======================================Buttons=====================================
    self.btnAddData = Button(ButtonFrame , text = "ADD Data", font=('arial',14,'bold'),height= 2, width = 13,bd=4,command = addData)
    self.btnAddData.grid(row=0,column=0)

    self.btnDisplayData = Button(ButtonFrame , text = "Display Data", font=('arial',14,'bold'),height= 2, width = 14,bd=4)
    self.btnDisplayData.grid(row=0,column=1)

    self.btnClearData = Button(ButtonFrame , text = "Clear Data", font=('arial',14,'bold'),height= 2, width = 13,bd=4, command = ClaearData)
    self.btnClearData.grid(row=0,column=2)

    self.btnDeleteData = Button(ButtonFrame , text = "Delete Data", font=('arial',14,'bold'),height= 2, width = 14,bd=4)
    self.btnDeleteData.grid(row=0,column=3)

    self.btnUpdateData = Button(ButtonFrame , text = "Update Data", font=('arial',14,'bold'),height= 2, width = 14,bd=4)
    self.btnUpdateData.grid(row=0,column=4)

    self.btnSearchData = Button(ButtonFrame , text = "Search Data", font=('arial',14,'bold'),height= 2, width = 14,bd=4)
    self.btnSearchData.grid(row=0,column=5)

    self.btnExit = Button(ButtonFrame , text = "Exit", font=('arial',14,'bold'),height= 2, width = 13,bd=4, command = iExit)
    self.btnExit.grid(row=0,column=6)



if __name__=='__main__':
  root = Tk()
  application = Library(root)
  root.mainloop()




    


    
                   
