from tkinter import *

from tkinter import messagebox
import database as db
class order_list(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.data=list()
        self.geometry("515x530")
        # self.resizable(False, False)
        self.title("Order")
        self.iconbitmap('icon\\user_img.ico')
        # Frames/////////////////////////////////////////////
        # Frames/////////////////////////////////////////////
        self.top = Frame(self, height=50, bg="white")
        self.top.pack(fill=X)
        # main bottom frame
        self.bottom = Frame(self, height=550, bg="#00d8d6")
        self.bottom.pack(fill=X)

        # /////////////////////////////////////
        # ///////////////// adding logo/////////////////////////////
        self.top_image = PhotoImage(file="icon\\deliever.png")
        self.toplbl = Label(self.top, image=self.top_image, bg="white")
        self.toplbl.grid(row=0, column=0, padx=40)
        # //////////////////////////////////
        self.heading = Label(self.top, text="All About Toys LTD", font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        # ////////////////////////////////

#         creating more frame

        # cata frame
        self.cata_panal = LabelFrame(self.bottom, text="Order", borderwidth=2, width=250, height=480, relief=SUNKEN,
                                     bg="#00d8d6")
        self.cata_panal.pack(fill=X, side=LEFT)
        # product frame
        self.product_panal = LabelFrame(self.bottom, text="Action", borderwidth=2, width=250, height=480,
                                        relief=SUNKEN, bg="#00d8d6")
        self.product_panal.pack(fill=X, side=LEFT)
        # order list box
        self.cata_box = Listbox(self.cata_panal, width=38, height=29, bg="#00d8d6", selectmode=SINGLE)
        self.cata_box.grid(row=0, column=0, sticky=N)
        self.cata_slide = Scrollbar(self.cata_panal, orient=VERTICAL, command=self.cata_box.yview, bg="white")
        self.cata_box.config(yscrollcommand=self.cata_slide.set)
        self.cata_slide.grid(row=0, column=1, sticky=N + S + E)
        # to sort product between delivered and process radio button
        # Radio btn
        self.choose = IntVar()
        self.list_radio1 = Radiobutton(self.product_panal, text="All", var=self.choose, value=0, bg="#00d8d6")
        self.list_radio1.place(x=20, y=40)
        self.list_radio2 = Radiobutton(self.product_panal, text="Process", var=self.choose, value=1, bg="#00d8d6")
        self.list_radio2.place(x=80, y=40)
        self.list_radio3 = Radiobutton(self.product_panal, text="Delivered", var=self.choose, value=2, bg="#00d8d6")
        self.list_radio3.place(x=150, y=40)
        self.search_btn = Button(self.product_panal, text="Sort By", bg="white", width=20, command=self.searching_specific)
        self.search_btn.place(x=60, y=80)
        # Mark as delivered
        self.img=PhotoImage(file="icon\\delivered.png")
        self.delivered_btn = Button(self.product_panal, image=self.img, compound=LEFT, text=" Mark Delivered",
                                    width=180,command=self.delivered)
        self.delivered_btn.place(x=30, y=150)
        # mark as process
        self.imgi=PhotoImage(file="icon\\process.png")
        self.process_btn = Button(self.product_panal, image=self.imgi, compound=LEFT, text=" Mark Process",
                                    width=180,command=self.processed)
        self.process_btn.place(x=30, y=250)
        self.windoe()
    def windoe(self):
        data = db.get_order_id()
        self.cata_box.delete(0, "end")
        for x in range(len(data)):
            self.cata_box.insert(x, str(data[x][0]) + "----" + str(data[x][1]) + "----" + str(data[x][2]))

    def searching_specific(self):
        order=self.choose.get()
        if order==0:
            data=db.get_order_id()
            self.cata_box.delete(0, "end")
            for x in range(len(data)):
                self.cata_box.insert(x, str(data[x][0])+"----"+str(data[x][1])+ "----"+str(data[x][2]))
        elif order==1:
            data = db.mark_order(0)
            self.cata_box.delete(0, "end")
            for x in range(len(data)):
                self.cata_box.insert(x, str(data[x]))
        elif order==2:
            data = db.mark_order(1)
            self.cata_box.delete(0, "end")
            for x in range(len(data)):
                self.cata_box.insert(x, str(data[x]))
        else:
            pass
    def delivered(self):
        value=self.cata_box.curselection()
        for itm in value:
            id = str(self.cata_box.get(itm))
        id=id.split("----")
        self.ide=int(id[0])
        db.order_status(self.ide,"1")
        messagebox.showinfo("Delivered","Order Status has been change to delivered")

    def processed(self):
        db.order_status(self.ide, "0")
        messagebox.showinfo("Delivered", "Order Status has been change to process")


class set_discount(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("400x500")
        self.resizable(False, False)
        self.title("Discount")
        self.iconbitmap("icon\\ic.ico")
        # Frames/////////////////////////////////////////////
        # Frames/////////////////////////////////////////////
        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=450, bg="#00d8d6")
        self.bottom.pack(fill=X)
        # styling///////////////////
        # Heading,image and date in top frame
        self.top_image = PhotoImage(file="icon\\dis_logo.png")
        self.toplbl = Label(self.top, image=self.top_image, bg="white")
        self.toplbl.grid(row=0, column=0, padx=40)
        self.heading = Label(self.top, text="Set Discount",
                             font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        # package 1
        self.package1=Label(self.bottom, text="First package",
                          font="centaur 15", bg="#00d8d6")
        self.package1.place(x=150,y=2)
        # Label 1
        self.name = Label(self.bottom, text="Amount",
                          font="centaur 11", bg="#00d8d6")
        self.name.place(x=40, y=30)
        self.name1 = Entry(self.bottom, font="calibri 11", bg="white")
        self.name1.place(x=160, y=30)
        # label2
        self.dis_name = Label(self.bottom, text="Discount Amount",
                                font="centaur 11", bg="#00d8d6")
        self.dis_name.place(x=40, y=70)
        self.dis_name1 = Entry(self.bottom, font="calibri 11", bg="white")
        self.dis_name1.place(x=160, y=70)
        # package 2
        self.package2 = Label(self.bottom, text="Second package",
                              font="centaur 15", bg="#00d8d6")
        self.package2.place(x=150, y=100)
        # password
        self.pk = Label(self.bottom, text="Amount.",
                         font="centaur 11", bg="#00d8d6")
        self.pk.place(x=40, y=140)
        self.pk1 = Entry(self.bottom, font="calibri 11", bg="white")
        self.pk1.place(x=160, y=140)
        self.pk11 = Label(self.bottom, text="Discount.",
                         font="centaur 11", bg="#00d8d6")
        self.pk11.place(x=40, y=180)
        self.pk111 = Entry(self.bottom, font="calibri 11", bg="white")
        self.pk111.place(x=160, y=180)
        # package 3
        self.package3 = Label(self.bottom, text="Third package",
                              font="centaur 15", bg="#00d8d6")
        self.package3.place(x=150, y=210)
        # password
        self.pk2 = Label(self.bottom, text="Amount.",
                        font="centaur 11", bg="#00d8d6")
        self.pk2.place(x=40, y=250)
        self.pk3 = Entry(self.bottom, font="calibri 11", bg="white")
        self.pk3.place(x=160, y=250)
        self.pk33 = Label(self.bottom, text="Discount.",
                        font="centaur 11", bg="#00d8d6")
        self.pk33.place(x=40, y=280)
        self.pk333 = Entry(self.bottom, font="calibri 11", bg="white")
        self.pk333.place(x=160, y=280)
        # btn/////////////////////
        self.btnicon2 = PhotoImage(file="icon\\disbtn.png")
        self.add_dis = Button(self.bottom, image=self.btnicon2, compound=LEFT, text="Discount",
                                 font="centaur 11", bg="white", width=180, command=self.set_dis)
        self.add_dis.place(x=130, y=340)
        self.insert_val()
        # handle close
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.destroy()

    def set_dis(self):
        pk1=self.name1.get()
        dis1=self.dis_name1.get()
        pk2=self.pk1.get()
        dis2=self.pk111.get()
        pk3=self.pk3.get()
        dis3=self.pk333.get()
        db.set_dis(pk1,dis1,pk2,dis2,pk3,dis3)
        messagebox.showinfo("done","Discount Has been updated")
        self.destroy()
    def insert_val(self):
        data=db.get_dis()
        self.name1.insert(0,data[0][1])
        self.dis_name1.insert(0,data[0][2])
        self.pk1.insert(0,data[1][1])
        self.pk111.insert(0,data[1][2])
        self.pk3.insert(0,data[2][1])
        self.pk333.insert(0,data[2][2])
