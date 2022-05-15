from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import database as db
import createpdfreport as pd
import os
class sale(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("400x420")
        self.resizable(False, False)
        self.title("Sales")
        self.iconbitmap("icon\\emp.ico")
        # Frames/////////////////////////////////////////////
        # Frames/////////////////////////////////////////////
        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=450, bg="#00d8d6")
        self.bottom.pack(fill=X)
        # styling///////////////////
        # Heading,image and date in top frame
        self.top_image = PhotoImage(file="icon\\report.png")
        self.toplbl = Label(self.top, image=self.top_image, bg="white")
        self.toplbl.grid(row=0, column=0, padx=40)
        self.heading = Label(self.top, text="All About Toys LTD",
                             font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        # adding main buuton and radio buuton
        self.sale_img = PhotoImage(file="icon\\print.png")
        self.sale_report = tk.Button(self.bottom, image=self.sale_img, compound=LEFT, text=" Generate Full Report",
                                     width=180,command=self.full_report)
        self.sale_report.place(x=120, y=20)
#         generate report by category
        self.name = Label(self.bottom, text="Report By Category", font="centaur 11", bg="#00d8d6")
        self.name.place(x=40, y=90)
#         box
        self.category_value = StringVar()
        # list for category
        self.stock_list = db.cate_list()
        self.cate1 = ttk.Combobox(self.bottom, textvariable=self.category_value, values=self.stock_list)
        self.cate1.configure(state="readonly")
        self.cate1.place(x=160, y=90)
        self.cate_img=PhotoImage(file="icon\\catae.png")
        self.cate_btn=Button(self.bottom,text="Category or Product Report",image=self.cate_img,compound=LEFT,width=185,command=self.cate_report)
        self.cate_btn.place(x=120,y=130)
    #     repotr of highest product
        self.high_img=PhotoImage(file="icon\\high.png")
        self.higest_btn = Button(self.bottom,image=self.high_img,compound=LEFT, text="Highest Sale",width=180,command=self.high_report)
        self.higest_btn.place(x=120, y=190)
        # lowest
        self.low_img=PhotoImage(file="icon\\high.png")
        self.low_btn = Button(self.bottom,image=self.high_img,compound=LEFT, text="Worst Sale",width=180,command=self.low_report)
        self.low_btn.place(x=120, y=250)
    def full_report(self):
        data=db.all_sold()
        string=[["ID","Name","Category","Sale Quantity", "Item Price", "Total"]]
        for x in range(len(data)):
            string.append(data[x])
        pd.create_file(string,"Full_Report")
        messagebox.showinfo("Done","Report Has been Generated")
        os.system(f'start excel.exe Full_Report.csv')
    def cate_report(self):
        cate=self.category_value.get()
        data=db.cate_sold(cate)
        string = [["ID", "Name", "Category", "Sale Quantity", "Item Price", "Total"]]
        for x in range(len(data)):
            string.append(data[x])
        pd.create_file(string, "Category_or_Product_Report")
        messagebox.showinfo("Done", "Report Has been Generated")
        os.system(f'start excel.exe Category_or_Product_Report.csv')
    def high_report(self):
        data = db.high_sold()
        string = [["ID", "Name", "Category", "Sale Quantity", "Item Price", "Total"]]
        for x in range(len(data)):
            string.append(data[x])
        pd.create_file(string, "Highest_Sale_Report")
        messagebox.showinfo("Done", "Report Has been Generated")
        os.system(f'start excel.exe Highest_Sale_Report.csv')
    def low_report(self):
        data = db.low_saleing()
        string = [["ID", "Name", "Category", "Sale Quantity", "Item Price", "Total"]]
        for x in range(len(data)):
            string.append(data[x])
        pd.create_file(string, "Worst_Sale_Report")
        messagebox.showinfo("Done", "Report Has been Generated")
        os.system(f'start excel.exe Worst_Sale_Report.csv')
