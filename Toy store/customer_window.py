from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import database as db
import shoping_cart as sc
import chat
import comment_window

class user_login(Toplevel):
    def __init__(self,time):
        Toplevel.__init__(self)
        self.data=list()
        self.geometry("1275x600")
        self.resizable(False, False)
        self.title("Customer")
        self.iconbitmap('icon\\user_img.ico')
        # Frames/////////////////////////////////////////////
        # Frames/////////////////////////////////////////////
        self.top = Frame(self, height=50, bg="white")
        self.top.pack(fill=X)
        # main bottom frame
        self.bottom = Frame(self, height=550, bg="#00d8d6")
        self.bottom.pack(fill=X)
        # for refresh button frame
        self.refresh_panel=Frame(self.bottom,borderwidth=2, height=30,relief=SUNKEN,bg="#00d8d6")
        self.refresh_panel.pack(fill=X)
        # Button for refresh
        self.refresh_img = PhotoImage(file="icon\\update_btn.png")
        self.refresh = tk.Button(self.refresh_panel, image=self.refresh_img, height=20,command=self.adding_details)
        self.refresh.place(x=2, y=0)
        # /////////////////////////////////////
        # ///////////////// adding logo/////////////////////////////
        self.top_image = PhotoImage(file="icon\\1.png")
        self.toplbl = Label(self.top, image=self.top_image, bg="white")
        self.toplbl.grid(row=0, column=0, padx=40)
        # //////////////////////////////////
        self.heading = Label(self.top, text="All About Toys LTD", font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        # ////////////////////////////////
        self.heading_time = Label(self.top, text="Date: " + str(time), font="centaur 11", bg="white")
        self.heading_time.place(x=820, y=5)
#         creating more frame

        # cata frame
        self.cata_panal = LabelFrame(self.bottom, text="Category", borderwidth=2, width=250, height=480, relief=SUNKEN,
                                     bg="#00d8d6")
        self.cata_panal.pack(fill=X, side=LEFT)
        # product frame
        self.product_panal = LabelFrame(self.bottom, text="Product", borderwidth=2, width=250, height=480,
                                        relief=SUNKEN, bg="#00d8d6")
        self.product_panal.pack(fill=X, side=LEFT)
        # employ frame
        self.item_panal = LabelFrame(self.bottom, text="Product Details", borderwidth=2, width=450, height=480, relief=SUNKEN,
                                       bg="#00d8d6")
        self.item_panal.pack(fill=X, side=LEFT)
        # button frame
        self.button_panal = Frame(self.bottom, borderwidth=2, width=350, height=520, relief=SUNKEN, bg="#00d8d6")
        self.button_panal.pack(fill=BOTH, side=RIGHT)
        # //////////////////// search panal       //////////////////////////////
        self.search_panal = Frame(self.button_panal, borderwidth=2, width=300, height=100, relief=SUNKEN, bg="#00d8d6")
        self.search_panal.pack(fill=X, side=TOP)
        #         //////////////////////Button Panal//////////////////
        self.add_panal = Frame(self.button_panal, borderwidth=2, width=300, height=420, relief=SUNKEN, bg="#00d8d6")
        self.add_panal.pack(fill=X, side=BOTTOM)
        # adding button to view cart
        self.view_img = PhotoImage(file="icon\\view.png")
        self.view_Carti= tk.Button(self.add_panal, image=self.view_img, compound=LEFT, text="View Cart", width=180,
                                    command=self.view_cart).place(x=60,y=100)
        # to delete cart
        self.del_img = PhotoImage(file="icon\\dele.png")
        self.del_Carti= tk.Button(self.add_panal, image=self.del_img, compound=LEFT, text="Empty Cart", width=180,
                                    command=self.deli_cart).place(x=60,y=200)
        self.chat_img = PhotoImage(file="icon\\chat_us.png")
        self.chat_Carti= tk.Button(self.add_panal, image=self.chat_img, compound=LEFT, text="Chat With Us", width=180,
                                    command=self.chat_win).place(x=60,y=300)
        # //////////////////////////////////////////////////
        # search bar/ in search panal
        self.search_bar = LabelFrame(self.search_panal, text="Search Box", width=300, height=100, bg="#00d8d6")
        self.search_bar.pack(fill=X, side=TOP)
        # search buttion and lables
        self.search_label = Label(self.search_bar, text="Search", bg="#00d8d6")
        self.search_label.place(x=10, y=10)
        self.search_entry = Entry(self.search_bar, width=35)
        self.search_entry.place(x=55, y=10)
        # search button...../////
        self.search_btn = Button(self.search_bar, text="Search", bg="white", width=20,command=self.searching_specific)
        self.search_btn.place(x=75, y=50)
#  ////////////////////////////////////inserting boxes
        # ///////////////////////////////////////////////////////
        # /////////////////////////////Cata box//////////////////////////////////////////
        self.cata_box = Listbox(self.cata_panal, width=38, height=29, bg="#00d8d6", selectmode=SINGLE)
        self.cata_box.grid(row=0, column=0, sticky=N)
        self.cata_slide = Scrollbar(self.cata_panal, orient=VERTICAL, command=self.cata_box.yview, bg="white")
        self.cata_box.config(yscrollcommand=self.cata_slide.set)
        self.cata_slide.grid(row=0, column=1, sticky=N + S + E)
        self.cata_box.bind("<Double-Button-1>", self.sort_cata)
        # ///////////////////////////////////////////////////////////////
        # //////////////////////////Product Box///////////////////////////////////////
        self.product_box = Listbox(self.product_panal, width=38, height=29, bg="#00d8d6", selectmode=SINGLE)
        self.product_box.grid(row=0, column=0, sticky=N)
        self.product_slide = Scrollbar(self.product_panal, orient=VERTICAL, command=self.product_box.yview, bg="white")
        self.product_box.config(yscrollcommand=self.product_slide.set)
        self.product_slide.grid(row=0, column=1, sticky=N + S + E)
        self.product_box.bind("<Double-Button-1>", self.detail_product)
        self.product_box.bind("<Button-3>", self.review)
        self.adding_details()
# for handlix X close
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
    def on_closing(self):
        self.destroy()
    #     //////////////////////////////////////////////
    # ////////////////////product view///////////////////////////////////////
    def product_view(self,id,name,price,category,quantity,details="s"):
        self.id=id
        # Label 1
        self.name = Label(self.item_panal, text="Name",
                          font="centaur 11", bg="#00d8d6")
        self.name.place(x=40, y=20)
        self.name1 = Entry(self.item_panal, font="calibri 11", bg="white")
        self.name1.delete(0,"end")
        self.name1.insert(0,name)
        self.name1.config(state="readonly")
        self.name1.place(x=160, y=20)
        # label2
        self.p_price = Label(self.item_panal, text="Price",
                             font="centaur 11", bg="#00d8d6")
        self.p_price.place(x=40, y=50)
        self.p_price1 = Entry(self.item_panal, font="calibri 11", bg="white")

        self.p_price1.delete(0, "end")
        self.p_price1.insert(0, price)
        self.p_price1.config(state="readonly")
        self.p_price1.place(x=160, y=50)
        # label 3
        self.p_cata = Label(self.item_panal, text="Category.",
                                font="centaur 11", bg="#00d8d6")
        self.p_cata.place(x=40, y=80)
        self.p_cata1 = Entry(self.item_panal, font="calibri 11", bg="white")
        self.p_cata1.delete(0, "end")
        self.p_cata1.insert(0, category)
        self.p_cata1.config(state="readonly")
        self.p_cata1.place(x=160, y=80)
        # category
        self.Stock = Label(self.item_panal, text="Quantity.",
                            font="centaur 11", bg="#00d8d6")

        self.Stock.place(x=40, y=120)
        # variable to get category value
        self.quantity_value = StringVar()
        # list for category
        self.stock_list = quantity
        self.stock1 = ttk.Combobox(self.item_panal, textvariable=self.quantity_value, values=self.stock_list)
        self.stock1.configure(state="readonly")
        self.stock1.place(x=160, y=120)
        # product details
        self.comment = Label(self.item_panal, text="Product Details:",
                             font="centaur 11", bg="#00d8d6").place(x=40, y=160)
        self.comment1 = Text(self.item_panal, width=45, height=7, bg="white")
        self.comment1.place(x=40, y=200)
        self.comment1.delete("1.0","end-1c")
        self.comment1.insert(INSERT,details)
        self.comment1.config(state="disabled")
        # btn/////////////////////
        self.btn_img = PhotoImage(file="icon\\cart.png")
        add_product = Button(self.item_panal, image=self.btn_img, compound=LEFT, text="Add Cart",
                                  font="centaur 11", bg="white", width=180,command=self.add_cart)
        add_product.place(x=130, y=350)
    # adding detawils into their required function
    def adding_details(self):
        self.product_box.delete(0, "end")
        self.cata_box.delete(0, "end")
        employ,product,category =db.box_list()
        for x in range(len(product)):
            self.product_box.insert(x, str(product[x]))
        for x in range(len(employ)):
            self.cata_box.insert(x, str(category[x]))
#     sort category
    def sort_cata(self,event):
        value = self.cata_box.curselection()
        for itm in value:
            id = str(self.cata_box.get(itm))
        val = id.split("-")
        val = val[1]
        data=db.sort_cat(val)
        self.product_box.delete(0, "end")
        for x in range(len(data)):
            self.product_box.insert(x, str(data[x]))
    # to view product details
    def detail_product(self,event):
        value=self.product_box.curselection()
        for itm in value:
            id = str(self.product_box.get(itm))
        val =id.split("-")
        val=val[0]
        x=db.get_alldata('product',val)
        y=db.sp_details(val)
        detail=str(y[0][0])
        stock=list()
        for y in range(x[3]+1):
            stock.append(y)
        self.stock_num=len(stock)-1
        self.product_view(x[0],x[1],x[2],x[4],stock,detail)
# /searching function
    def searching_specific(self):
        value=self.search_entry.get()
        data=db.searching_function('product',value)
        self.product_box.delete(0, "end")
        for x in range(len(data)):
            self.product_box.insert(x, str(data[x]))
    def add_cart(self):
        quantity=self.stock1.get()
        name=self.name1.get()
        price=self.p_price1.get()
        id=self.id

        if int(quantity)<=0:
            messagebox.showerror(title="error",message="Maybe the item is out of stock or you buying less than required")
        else:
            total_amount=int(quantity)*int(price)
            final=int(self.stock_num)-int(quantity)
            db.update_quantity(id,final)
            db.sold_product(id,quantity,total_amount)
            self.data.append([id,name,price,quantity])
    def view_cart(self):
        cart=sc.cart(self.data)
    def deli_cart(self):
        self.data.clear()
        messagebox.showinfo("Empty","Cart is Empty")
    def chat_win(self):
        chat.my_chat("You")
    def review(self,event):
        value = self.product_box.curselection()
        for itm in value:
            id = str(self.product_box.get(itm))
        val = id.split("-")
        val = val[0]
        comment_window.review_list(val)
