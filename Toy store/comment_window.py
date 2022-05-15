from tkinter import *
import add_comment_window
import database as db
class review_list(Toplevel):
    def __init__(self,id):
        Toplevel.__init__(self)
        self.keys=id
        self.data=list()
        self.geometry("515x530")
        # self.resizable(False, False)
        self.title("Order")
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
        self.top_image = PhotoImage(file="icon\\deliever.png")
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
        self.delivered_btn = Button(self.product_panal, image=self.img, compound=LEFT, text=" View Comment",
                                    width=180,command=self.view_comment)
        self.delivered_btn.place(x=30, y=40)
        # add comment
        self.imgi=PhotoImage(file="icon\\process.png")
        self.process_btn = Button(self.product_panal, image=self.imgi, compound=LEFT, text=" Add Comment",
                                    width=180,command=self.add_comment)
        self.process_btn.place(x=30, y=130)
        # refresh comment
        self.re=PhotoImage(file="icon\\update_btn.png")
        self.re_btn = Button(self.product_panal, image=self.re, compound=LEFT, text=" Refresh",
                                    width=180,command=self.windoe)
        self.re_btn.place(x=30, y=220)
        self.windoe()
    def windoe(self):
        data = db.get_all_comment(self.keys)
        self.cata_box.delete(0, "end")
        for x in range(len(data)):
            self.cata_box.insert(x, str(data[x][0]) + "----" + str(data[x][1]) )


    def view_comment(self):
        value=self.cata_box.curselection()
        for itm in value:
            id = str(self.cata_box.get(itm))
        id=id.split("----")
        self.ide=int(id[0])
        data=db.view_comment(self.ide)
        add_comment_window.view_comment(data)


    def add_comment(self):
        add_comment_window.add_comment(self.keys)