from tkinter import *
import tkinter as tk
import database as db
import os
import createpdfreport as pd
from tkinter import messagebox
class payment(Toplevel):
    def __init__(self,data,value):
        self.bill=data
        self.bill_price=value
        Toplevel.__init__(self)
        self.data=list()
        self.geometry("550x600")
        self.resizable(False, False)
        self.title("Payment")
        self.iconbitmap('icon\\pay.ico')
        # Frames/////////////////////////////////////////////
        # Frames/////////////////////////////////////////////
        self.top = Frame(self, height=50, bg="white")
        self.top.pack(fill=X)
        # main bottom frame
        self.bottom = Frame(self, height=550, bg="#00d8d6")
        self.bottom.pack(fill=X)
        # for refresh button frame

        # /////////////////////////////////////
        # ///////////////// adding logo/////////////////////////////
        self.top_image = PhotoImage(file="icon\\payment.png")
        self.toplbl = Label(self.top, image=self.top_image, bg="white")
        self.toplbl.grid(row=0, column=0, padx=40)
        # //////////////////////////////////
        self.heading = Label(self.top, text="All About Toys LTD", font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        # ////////////////////////////////////////////
        # ////////////////////////////adding baisc inputs and info
        # Label 1
        self.name = Label(self.bottom, text="Name",font="centaur 11", bg="#00d8d6")
        self.name.place(x=40, y=20)
        self.name1 = Entry(self.bottom, font="calibri 11", bg="white",width=40)
        self.name1.place(x=160, y=20)
        # Total price
        self.price = Label(self.bottom, text="Total Price",font="centaur 11", bg="#00d8d6")
        self.price.place(x=40, y=60)
        self.price1 = Entry(self.bottom, font="calibri 11", bg="white",width=40)

        self.price1.place(x=160, y=60)
        # Total item
        self.item = Label(self.bottom, text="Total Item",font="centaur 11", bg="#00d8d6")
        self.item.place(x=40, y=100)
        self.item1 = Entry(self.bottom, font="calibri 11", bg="white",width=40)
        self.item1.place(x=160, y=100)
        # discount
        self.discount = Label(self.bottom, text="Discount",font="centaur 11", bg="#00d8d6")
        self.discount.place(x=40, y=140)
        self.discount1 = Entry(self.bottom, font="calibri 11", bg="white",width=40)
        self.discount1.place(x=160, y=140)
        # card label
        self.card = Label(self.bottom, text="Enter your Visa or Master card Details",font="centaur 11", bg="#00d8d6")
        self.card.place(x=170, y=200)
        # card name
        self.card_name = Label(self.bottom, text="Card Holder Name", font="centaur 11", bg="#00d8d6")
        self.card_name.place(x=40, y=230)
        self.card_name1 = Entry(self.bottom, font="calibri 11", bg="white", width=40)
        self.card_name1.place(x=160, y=230)
        # card number
        self.card_number = Label(self.bottom, text="Card Number", font="centaur 11", bg="#00d8d6")
        self.card_number.place(x=40, y=270)
        self.card_number1 = Entry(self.bottom, font="calibri 11", bg="white", width=40)
        self.card_number1.place(x=160, y=270)
        # card exp and csv
        self.exp = Label(self.bottom, text="Expire date", font="centaur 11", bg="#00d8d6")
        self.exp.place(x=40, y=300)
        self.exp1 = Entry(self.bottom, font="calibri 11", bg="white", width=10)
        self.exp1.place(x=160, y=300)
        # card csvnumber
        self.csv = Label(self.bottom, text="CSV", font="centaur 11", bg="#00d8d6")
        self.csv.place(x=250, y=300)
        self.csv1 = Entry(self.bottom, font="calibri 11", bg="white", width=10)
        self.csv1.place(x=300, y=300)
#         billing address
        self.billng=Label(self.bottom, text="Address", font="centaur 11", bg="#00d8d6")
        self.billng.place(x=40, y=350)
        self.billing1=self.messages = Text(self.bottom,width=36, height=7,bg="white")
        self.messages.place(x=160, y=350)
        # submit
        self.sub_img = PhotoImage(file="icon\\sub.png")
        self.submit1 = tk.Button(self.bottom, text="Submit", image=self.sub_img, compound=LEFT, width=180,
                              command=self.submit_details)
        self.submit1.place(x=200, y=480)
        self.add_data()
    def submit_details(self):
        name=self.name1.get()
        total_price=self.price1.get()
        total_item=self.item1.get()
        status = int('0')
        discount=self.discount1.get()
        address=str(self.billing1.get("1.0","end-1c"))
        print(address)

        d=db.order_now(name,total_price,total_item,status,discount,address)
        id=db.get_order_id()
        id=len(id)
        id_value="Receipt"+"_"+str(id)
        string = [["order id" ,"name","price","Quantity","discount","address"],[id,name,total_price,total_item,discount,address]]
        pd.create_file(string,id_value)
        # to open created file

        messagebox.showinfo("Order", f"This is your order id {id_value}")
        os.system(f'start excel.exe {id_value}.csv')
        self.destroy()

    def add_data(self):
        item=list()
        for x in range(len(self.bill)):
            string=str(self.bill[x])
            string=string.split("----")
            item.append(int(string[0]))
        self.item=sum(item)
        self.item1.insert(0,self.item)
        self.item1.config(state="readonly")
        bill=self.bill_price
        data=db.get_discount_val()
        print(data)
        print(data[0][1],data[1][1])
        if int(bill)>= int(data[0][0]) and int(bill)<int(data[1][0]):

            bill=int(bill)-int(data[0][1])

            self.price1.insert(0,str(bill)+"$")
            self.price1.config(state="readonly")
            self.discount1.insert(0,int(data[0][1]))
        elif int(bill)>= int(data[1][0]) and int(bill)< int(data[2][0]):
            bill=int(bill)-int(data[1][1])

            self.price1.insert(0, str(bill) + "$")
            self.price1.config(state="readonly")
            self.discount1.insert(0, int(data[1][1]))
        elif int(bill)>= int(data[2][1]):
            bill=int(bill)-int(data[2][1])
            self.price1.insert(0, str(bill) + "$")
            self.price1.config(state="readonly")
            self.discount1.insert(0, int(data[2][1]))
            self.discount1.config(state="readonly")
        else:
            self.price1.insert(0, str(bill) + "$")
            self.price1.config(state="readonly")
            self.discount1.insert(0, "0")
            self.discount1.config(state="readonly")

#

