
from tkinter import *
import delivery_window as dw

class cart(Toplevel):
    def __init__(self,data):
        self.data=data
        Toplevel.__init__(self)
        self.geometry("258x650")
        # self.resizable(False, False)
        self.title("Cart")
        self.iconbitmap('icon\\user_img.ico')
        # Frames/////////////////////////////////////////////
        # Frames/////////////////////////////////////////////
        self.top = Frame(self, height=50, bg="white")
        self.top.pack(fill=X)
        # main bottom frame
        self.bottom = Frame(self, height=600, bg="#00d8d6")
        self.bottom.pack(fill=BOTH)
        # /////////////////////////////////////
        # ///////////////// adding logo/////////////////////////////
        self.top_image = PhotoImage(file="icon\\1.png")
        self.toplbl = Label(self.top, image=self.top_image, bg="white")
        self.toplbl.grid(row=0, column=0)
        # //////////////////////////////////
        self.heading = Label(self.top, text="All About Toys LTD", font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        # cata frame
        self.cata_panal = LabelFrame(self.bottom, text="Cart", borderwidth=2, width=250, height=400, relief=SUNKEN,
                                     bg="#00d8d6")
        self.cata_panal.pack(fill=X)
        # bottom frame
        self.add_panal = Frame(self.bottom, borderwidth=2, width=250, height=200, relief=SUNKEN, bg="#00d8d6")
        self.add_panal.pack(fill=BOTH)
#         total Bill
        Label(self.add_panal, text="Total Bill", bg="#00d8d6").place(x=2,y=3)
        self.total_bill_value=Entry(self.add_panal,width=18)
        self.total_bill_value.place(x=120,y=3)
        self.close_cart=Button(self.add_panal, text="Close Cart", bg="white", width=10,command=self.destroy).place(x=10,y=80)
        self.check_cart=Button(self.add_panal, text="Checkout", bg="white", width=10,command=self.check_out).place(x=120,y=80)
#         adding a list box in cart
        # /////////////////////////////Cata box//////////////////////////////////////////
        self.cata_box = Listbox(self.cata_panal, width=38, height=25, bg="#00d8d6", selectmode=SINGLE)
        self.cata_box.grid(row=0, column=0, sticky=N)
        self.cata_slide = Scrollbar(self.cata_panal, orient=VERTICAL, command=self.cata_box.yview, bg="white")
        self.cata_box.config(yscrollcommand=self.cata_slide.set)
        self.cata_slide.grid(row=0, column=1, sticky=N + S + E)
        self.add_details()
#     ////////////////////////
#     ///////////////check out///
    def check_out(self):
        dw.delivery(self.billdata,self.bill_val)
        # pm.payment(self.billdata,self.bill_val)
        self.destroy()
    def add_details(self):
        data=self.data
        self.cata_box.delete(0, "end")
        bill=list()
        name_price=list()
        for x in range(len(data)):
            bill.append(int(data[x][2])*int(data[x][3]))
            name_price.append(str(data[x][3])+"----"+str(data[x][1])+"----"+str(data[x][2]+"$"))
        for x in range(len(name_price)):
            self.cata_box.insert(x, str(name_price[x]))


        bill=sum(bill)
        # taking these values into customer payment windwo
        self.billdata = name_price
        self.bill_val = bill
        # ///////////////////////////////////////////////////
        self.bill_do=str(str(bill)+"$")
        self.total_bill_value.delete(0,"end")
        self.total_bill_value.insert(0,self.bill_do)
        self.total_bill_value.config(state="readonly")