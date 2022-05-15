from tkinter import *
import tkinter as tk
import os
import admin_functionality as ad
from tkinter import messagebox
import database as db
import update_delete as ud
import createpdfreport as pd
class admin_login(Toplevel):
    def __init__(self,time):
        Toplevel.__init__(self)
        self.geometry("950x600")
        self.resizable(False, False)
        self.title("Admin")
        self.iconbitmap('icon\\admin.ico')
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
        #
        # Button for refresh
        self.refresh_img = PhotoImage(file="icon\\update_btn.png")
        self.refresh = tk.Button(self.refresh_panel, image=self.refresh_img,height=20, command=self.adding_details)
        self.refresh.place(x=2, y=0)
        self.print_img = PhotoImage(file="icon\\print.png")
        self.print_btn = tk.Button(self.refresh_panel, image=self.print_img,height=20, command=self.print_data)
        self.print_btn.place(x=910, y=0)
        #
        # employ frame
        self.employ_panal=LabelFrame(self.bottom,text="Employ", borderwidth=2, width=200, height=520,relief=SUNKEN,bg="#00d8d6")
        self.employ_panal.pack(fill=X,side=LEFT)
        # cata frame
        self.cata_panal = LabelFrame(self.bottom, text="Category",borderwidth=2, width=200, height=520, relief=SUNKEN, bg="#00d8d6")
        self.cata_panal.pack(fill=X, side=LEFT)
        # product frame
        self.product_panal = LabelFrame(self.bottom,text="Product", borderwidth=2, width=200, height=520, relief=SUNKEN, bg="#00d8d6")
        self.product_panal.pack(fill=X, side=LEFT)
        # button frame
        self.button_panal = Frame(self.bottom, borderwidth=2, width=350, height=520, relief=SUNKEN, bg="#00d8d6")
        self.button_panal.pack(fill=BOTH, side=RIGHT)
# //////////////////// search panal       //////////////////////////////
        self.search_panal = Frame(self.button_panal, borderwidth=2, width=300, height=200, relief=SUNKEN, bg="#00d8d6")
        self.search_panal.pack(fill=X, side=TOP)
#         //////////////////////Button Panal//////////////////
        self.add_panal = Frame(self.button_panal, borderwidth=2, width=300, height=320, relief=SUNKEN, bg="#00d8d6")
        self.add_panal.pack(fill=X, side=BOTTOM)
# //////////////////////////////////////////////////
        # search bar/ in search panal
        self.search_bar = LabelFrame(self.search_panal, text="Search Box", width=300, height=200, bg="#00d8d6")
        self.search_bar.pack(fill=X, side=TOP)
        # search buttion and lables
        self.search_label = Label(self.search_bar, text="Search", bg="#00d8d6")
        self.search_label.place(x=10,y=10)
        self.search_entry = Entry(self.search_bar, width=35)
        self.search_entry.place(x=55,y=10)
        # ////////////////inserting list radio//////////////
        # Radio btn
        self.choose = IntVar()
        self.list_radio1 = Radiobutton(self.search_bar, text="Employ", var=self.choose, value=0, bg="#00d8d6")
        self.list_radio1.place(x=30,y=40)
        self.list_radio2 = Radiobutton(self.search_bar, text="Category", var=self.choose, value=1, bg="#00d8d6")
        self.list_radio2.place(x=110,y=40)
        self.list_radio3 = Radiobutton(self.search_bar, text="Product", var=self.choose, value=2, bg="#00d8d6")
        self.list_radio3.place(x=190,y=40)
        self.search_btn = Button(self.search_bar, text="Search", bg="white", width=20,command=self.searching_specific)
        self.search_btn.place(x=75,y=80)
    #///////////////////////////////////////////////
    #     //////////////////////////////////////////////////
    #     ////////////Adding basic button//////////
        self.employ_img = PhotoImage(file="icon\\1486146612-propertyagent002_79450.png")
        self.add_employ=tk.Button(self.add_panal,image=self.employ_img,compound=LEFT,text="Add Employ",width=180,command=self.add_employs)
        self.add_employ.place(x=49,y=30)
        self.cat_img = PhotoImage(file="icon\\category-add-button_icon-icons.com_71724.png")
        self.add_cat = tk.Button(self.add_panal,image=self.cat_img,compound=LEFT, text="Add Category", width=180,command=self.add_category)
        self.add_cat.place(x=49, y=110)
        self.product_img = PhotoImage(file="icon\\producthunt-black_100125.png")
        self.add_product = tk.Button(self.add_panal,image=self.product_img,compound=LEFT, text="Add Product", width=180,command=self.add_product)
        self.add_product.place(x=49, y=190)
    # list employ
        # //////////////////List box
        self.employ_box = Listbox(self.employ_panal,width=32, height=31, bg="#00d8d6", selectmode=SINGLE)
        self.employ_box.grid(row=0, column=0, sticky=N)
        self.employ_slide = Scrollbar(self.employ_panal, orient=VERTICAL, command=self.employ_box.yview, bg="white")
        self.employ_box.config(yscrollcommand=self.employ_slide.set)
        self.employ_slide.grid(row=0, column=1, sticky=N + S + E)
        self.employ_box.bind("<Double-Button-1>",self.detail_employ)
        self.employ_box.bind("<Button-3>",self.edit_employ)
       # ///////////////////////////////////////////////////////
# /////////////////////////////Cata box//////////////////////////////////////////
        self.cata_box = Listbox(self.cata_panal,width=32, height=31, bg="#00d8d6", selectmode=SINGLE)
        self.cata_box.grid(row=0, column=0, sticky=N)
        self.cata_slide = Scrollbar(self.cata_panal, orient=VERTICAL, command=self.cata_box.yview, bg="white")
        self.cata_box.config(yscrollcommand=self.cata_slide.set)
        self.cata_slide.grid(row=0, column=1, sticky=N + S + E)
        self.cata_box.bind("<Double-Button-1>", self.detail_cata)
        self.cata_box.bind("<Button-3>", self.edit_cata)
        # ///////////////////////////////////////////////////////////////
        # //////////////////////////Product Box///////////////////////////////////////
        self.product_box = Listbox(self.product_panal, width=32, height=31, bg="#00d8d6", selectmode=SINGLE)
        self.product_box.grid(row=0, column=0, sticky=N)
        self.product_slide = Scrollbar(self.product_panal, orient=VERTICAL, command=self.product_box.yview, bg="white")
        self.product_box.config(yscrollcommand=self.product_slide.set)
        self.product_slide.grid(row=0, column=1, sticky=N + S + E)
        self.product_box.bind("<Double-Button-1>", self.detail_product)
        self.product_box.bind("<Button-3>", self.edit_product)
        # /////////////////////////////////////
        # ///////////////// adding logo/////////////////////////////
        self.top_image = PhotoImage(file="icon\\administrator_3552.png")
        self.toplbl = Label(self.top, image=self.top_image, bg="white")
        self.toplbl.grid(row=0, column=0, padx=40)
        # //////////////////////////////////
        self.heading = Label(self.top, text="All About Toys LTD", font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        # ////////////////////////////////
        self.heading_time = Label(self.top, text="Date: " + str(time), font="centaur 11", bg="white")
        self.heading_time.place(x=820, y=5)
        # details function
        self.adding_details()
        self.less_stock()
        # handling x close
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        # adding function
    def add_employs(self):
        ad.add_employ()
    def add_category(self):
        ad.add_category()
    def add_product(self):
        ad.add_product()
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()
    def adding_details(self):
        self.employ_box.delete(0, "end")
        self.product_box.delete(0, "end")
        self.cata_box.delete(0, "end")
        employ,product,category =db.box_list()
        for x in range(len(employ)):
            self.employ_box.insert(x, str(employ[x]))
        for x in range(len(product)):
            self.product_box.insert(x, str(product[x]))
        for x in range(len(category)):
            self.cata_box.insert(x, str(category[x]))
    def searching_specific(self):
        order=self.choose.get()
        value=self.search_entry.get()
        if order==0:
            data=db.searching_function('employ',value)
            self.employ_box.delete(0, "end")
            for x in range(len(data)):
                self.employ_box.insert(x, str(data[x]))
        elif order==1:
            data = db.searching_function('category', value)
            self.cata_box.delete(0, "end")
            for x in range(len(data)):
                self.cata_box.insert(x, str(data[x]))
        elif order==2:
            data = db.searching_function('product', value)
            self.product_box.delete(0, "end")
            for x in range(len(data)):
                self.product_box.insert(x, str(data[x]))
        else:
            pass
    def detail_employ(self,event):
        value=self.employ_box.curselection()
        for itm in value:
            id = str(self.employ_box.get(itm))
        val =id.split("-")
        val=val[0]
        x=db.get_alldata('employ',val)
        ud.add_employ(x[0],x[1],x[2],x[3],x[4])
    def edit_employ(self,event):
        value = self.employ_box.curselection()
        for itm in value:
            id = str(self.employ_box.get(itm))
        val = id.split("-")
        val = val[0]
        x = db.get_alldata('employ', val)
        ud.add_employ(x[0], x[1], x[2], x[3], x[4],'active','active','normal')
#     for category

    def detail_cata(self,event):
        value = self.cata_box.curselection()
        for itm in value:
            id = str(self.cata_box.get(itm))
        val = id.split("-")
        val = val[0]

        x = db.get_alldata('category', val)
        ud.add_category(x[0],x[1])
    def edit_cata(self,event):
        value = self.cata_box.curselection()
        for itm in value:
            id = str(self.cata_box.get(itm))
        val = id.split("-")
        val = val[0]
        x = db.get_alldata('category', val)
        ud.add_category(x[0], x[1],'active','active','normal')
#  for product add and delete
    def detail_product(self,event):
        value=self.product_box.curselection()
        for itm in value:
            id = str(self.product_box.get(itm))
        val =id.split("-")
        val=val[0]
        x=db.get_alldata('product',val)
        ud.add_product(x[0],x[1],x[2],x[3],x[4])
    def edit_product(self,event):
        value = self.product_box.curselection()
        for itm in value:
            id = str(self.product_box.get(itm))
        val = id.split("-")
        val = val[0]
        x = db.get_alldata('product', val)
        ud.add_product(x[0], x[1], x[2], x[3], x[4],'active','active','normal')
    def print_data(self):
        data=db.all_print()
        string = [["id" ,"name","price","Stock","category"]]

        for x in range(len(data)):
            string.append(data[x])
        pd.create_file(string,"report")
        messagebox.showinfo("Done","Report has been created")

        # to open created file
        os.system('start excel.exe report.csv')
    def less_stock(self):
        string=""
        data=db.all_print()
        if data:

            for x in range(len(data)):
                string=string+ str(data[x][1])+ ","
            string=string + " is less in stock"
            messagebox.showwarning("Less in stock", string)
