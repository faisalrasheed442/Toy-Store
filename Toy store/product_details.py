from tkinter import *
import add_comment_window
import database as db
import adding_product_details
class product_Details(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("515x530")
        # self.resizable(False, False)
        self.title("Product Details")
        self.iconbitmap('icon\\comment.ico')
        # Frames/////////////////////////////////////////////
        # Frames/////////////////////////////////////////////
        self.top = Frame(self, height=50, bg="white")
        self.top.pack(fill=X)
        # main bottom frame
        self.bottom = Frame(self, height=550, bg="#00d8d6")
        self.bottom.pack(fill=X)

        # /////////////////////////////////////
        # ///////////////// adding logo/////////////////////////////
        self.top_image = PhotoImage(file="icon\\der.png")
        self.toplbl = Label(self.top, image=self.top_image, bg="white")
        self.toplbl.grid(row=0, column=0, padx=40)
        # //////////////////////////////////
        self.heading = Label(self.top, text="All About Toys LTD", font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        # ////////////////////////////////

#         creating more frame

        # cata frame
        self.cata_panal = LabelFrame(self.bottom, text="Comment", borderwidth=2, width=250, height=480, relief=SUNKEN,
                                     bg="#00d8d6")
        self.cata_panal.pack(fill=X, side=LEFT)
        # product frame
        self.product_panal = LabelFrame(self.bottom, text="Action", borderwidth=2, width=250, height=480,relief=SUNKEN, bg="#00d8d6")
        self.product_panal.pack(fill=X, side=LEFT)
        # order list box
        self.cata_box = Listbox(self.cata_panal, width=38, height=29, bg="#00d8d6", selectmode=SINGLE)
        self.cata_box.grid(row=0, column=0, sticky=N)
        self.cata_slide = Scrollbar(self.cata_panal, orient=VERTICAL, command=self.cata_box.yview, bg="white")
        self.cata_box.config(yscrollcommand=self.cata_slide.set)
        self.cata_slide.grid(row=0, column=1, sticky=N + S + E)
        # to sort product between delivered and process radio button

        # View comment
        self.img=PhotoImage(file="icon\\delivered.png")
        self.delivered_btn = Button(self.product_panal, image=self.img, compound=LEFT, text=" Add Details",
                                    width=180,command=self.update_details)
        self.delivered_btn.place(x=30, y=40)

        # refresh comment
        self.re=PhotoImage(file="icon\\update_btn.png")
        self.re_btn = Button(self.product_panal, image=self.re, compound=LEFT, text=" Rafresh",
                                    width=180,command=self.windoe)
        self.re_btn.place(x=30, y=130)
        self.windoe()
    def windoe(self):
        data = db.product_details_geting()
        self.cata_box.delete(0, "end")
        for x in range(len(data)):
            self.cata_box.insert(x, str(data[x]))


    def update_details(self):
        value=self.cata_box.curselection()
        for itm in value:
            id = str(self.cata_box.get(itm))
        id=id.split("----")
        self.ide=int(id[0])
        print(self.ide)
        adding_product_details.add_details(self.ide)

