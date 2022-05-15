from tkinter import *
import tkinter as tk
import order_list_discount_window as odw
import sale_report_window as srw
import chat as ch
import employ_comment as ec
import product_details
class employ_login(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("400x450")
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
        self.top_image = PhotoImage(file="icon\\emp_logo.png")
        self.toplbl = Label(self.top, image=self.top_image, bg="white")
        self.toplbl.grid(row=0, column=0, padx=40)
        self.heading = Label(self.top, text="All About Toys LTD",
                             font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        # button for Generate sale report
        self.sale_img = PhotoImage(file="icon\\print.png")
        self.sale_report = tk.Button(self.bottom, image=self.sale_img, compound=LEFT, text=" Generate Sale Report", width=180,command=self.sale_repot_info)
        self.sale_report.place(x=110, y=70)
        # to process order
        self.process_img = PhotoImage(file="icon\\cata_button.png")
        self.Order_list = tk.Button(self.bottom, image=self.process_img, compound=LEFT, text=" Order List", width=180,command=self.order_pro)
        self.Order_list.place(x=110, y=120)
        # discount
        self.dis_img = PhotoImage(file="icon\\dis.png")
        self.dis_lis = tk.Button(self.bottom, image=self.dis_img, compound=LEFT, text=" Discount", width=180,command=self.add_discount)
        self.dis_lis.place(x=110, y=170)
        # chat butoon
        self.chat_img = PhotoImage(file="icon\\chat.png")
        self.chat_button = tk.Button(self.bottom, image=self.chat_img, compound=LEFT, text=" View Messages",
                                    width=180,command=self.chat)
        self.chat_button.place(x=110, y=219)
        # view comments
        self.ch_img = PhotoImage(file="icon\\chat.png")
        self.view_button = tk.Button(self.bottom, image=self.ch_img, compound=LEFT, text=" Comments",
                                    width=180,command=self.view_comment)
        self.view_button.place(x=110, y=270)
        self.cha_img = PhotoImage(file="icon\\de.png")
        self.det_button = tk.Button(self.bottom, image=self.cha_img, compound=LEFT, text=" Product Details",
                                    width=180,command=self.product_details)
        self.det_button.place(x=110, y=320)

        # employ
        # chat function
    def chat(self):
        ch.my_chat("Agent")
#
# /generate sale report
    def sale_repot_info(self):
        srw.sale()
    def add_discount(self):
        odw.set_discount()
    def order_pro(self):
        odw.order_list()
    def view_comment(self):
        ec.review_list()
    def product_details(self):
        product_details.product_Details()


