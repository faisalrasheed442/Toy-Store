from tkinter import *
import  payment_method as pw
class delivery(Toplevel):
    def __init__(self,data,price_val):
        Toplevel.__init__(self)
        self.billdata=data
        self.bill_val=price_val

        self.geometry("400x400")
        self.resizable(False, False)
        self.title("Add Admin")
        self.iconbitmap("icon\\add.ico")
        # Frames/////////////////////////////////////////////
        # Frames/////////////////////////////////////////////

        self.frame=Frame(self,bg="#00d8d6",width=400,height=400)
        self.frame.pack()
        self.choose = IntVar()
        self.list_radio1 = Radiobutton(self.frame, text="Express Delivery Charges 3$ in 7 days", var=self.choose, value=0, bg="#00d8d6")
        self.list_radio1.place(x=20, y=40)
        self.list_radio2 = Radiobutton(self.frame ,text="Standered Delivery 1$ in 14 days", var=self.choose, value=1, bg="#00d8d6")
        self.list_radio2.place(x=20, y=80)
        self.list_radio3 = Radiobutton(self.frame ,text="Overnight Delivery 5$ in 1 day", var=self.choose, value=2, bg="#00d8d6")
        self.list_radio3.place(x=20, y=120)
        self.list_radio4 = Radiobutton(self.frame ,text="Free Delivery within 1-2 Months", var=self.choose, value=3, bg="#00d8d6")
        self.list_radio4.place(x=20, y=160)
        self.search_btn = Button(self, text="Submit", bg="white", width=20,command=self.submiting)
        self.search_btn.place(x=60, y=200)
    def submiting(self):
        order = self.choose.get()
        if order == 0:
            bill=int(self.bill_val)+ 3
            pw.payment(self.billdata, bill)
            self.destroy()
        elif order == 1:
            bill = int(self.bill_val) + 1
            pw.payment(self.billdata, bill)
            self.destroy()
        elif order == 2:
            bill = int(self.bill_val) + 5
            pw.payment(self.billdata, bill)
            self.destroy()
        elif order == 3:
            bill = int(self.bill_val)
            pw.payment(self.billdata, bill)
            self.destroy()
        else:
            pass