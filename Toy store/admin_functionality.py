from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database as db
class add_employ(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("400x400")
        self.resizable(False, False)
        self.title("Add Employ")
        self.iconbitmap("icon\\add.ico")
        # Frames/////////////////////////////////////////////
        # Frames/////////////////////////////////////////////
        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=450, bg="#00d8d6")
        self.bottom.pack(fill=X)
        # styling///////////////////
        # Heading,image and date in top frame
        self.top_image = PhotoImage(file="icon\\add.png")
        self.toplbl = Label(self.top, image=self.top_image, bg="white")
        self.toplbl.grid(row=0, column=0, padx=40)
        self.heading = Label(self.top, text="Add Member",
                             font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        # Label 1
        self.name = Label(self.bottom, text="Name",
                          font="centaur 11", bg="#00d8d6")
        self.name.place(x=40, y=20)
        self.name1 = Entry(self.bottom, font="calibri 11", bg="white")
        self.name1.place(x=160, y=20)
        # label2
        self.Email_name = Label(self.bottom, text="Email Address",
                                     font="centaur 11", bg="#00d8d6")
        self.Email_name.place(x=40, y=50)
        self.Email_name1 = Entry(self.bottom, font="calibri 11", bg="white")
        self.Email_name1.place(x=160, y=50)
        # label 3
        self.phone = Label(self.bottom, text="Contact No.",
                           font="centaur 11", bg="#00d8d6")
        self.phone.place(x=40, y=80)
        self.phone1 = Entry(self.bottom, font="calibri 11", bg="white")
        self.phone1.place(x=160, y=80)
        # password
        self.pas = Label(self.bottom, text="Password.",
                           font="centaur 11", bg="#00d8d6")
        self.pas.place(x=40, y=120)
        self.password = Entry(self.bottom, font="calibri 11", bg="white")
        self.password.place(x=160, y=120)
        # btn/////////////////////
        self.btnicon2 = PhotoImage(file="icon\\add_btn.png")
        self.add_member = Button(self.bottom, image=self.btnicon2, compound=LEFT, text="Add member",
                                 font="calibri 11", bg="white", width=180,command=self.add_employ)
        self.add_member.place(x=130, y=180)
        # handle close
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.destroy()
    def add_employ(self):
        name=self.name1.get()
        email=self.Email_name1.get()
        contact=self.phone1.get()
        password=self.password.get()
        if db.search_employ(str(email)):
            messagebox.showerror(title="Already exists", message="This email is already Registered")
        else:
            db.add_employ(name,email,contact,password)
            messagebox.showinfo(title="Registered", message="Employ is Registered")
# adding  add cata class
class add_category(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("400x400")
        self.resizable(False, False)
        self.title("Category")
        self.iconbitmap("icon\\cata_icon.ico")
        # Frames/////////////////////////////////////////////
        # Frames/////////////////////////////////////////////
        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=450, bg="#00d8d6")
        self.bottom.pack(fill=X)
        # styling///////////////////
        # Heading,image and date in top frame
        self.top_image = PhotoImage(file="icon\\add.png")
        self.toplbl = Label(self.top, image=self.top_image, bg="white")
        self.toplbl.grid(row=0, column=0, padx=40)
        self.heading = Label(self.top, text="Add Category",
                             font="calibri 14", bg="white")
        self.heading.grid(row=0, column=1)
        # handle close
        self.protocol("WM_DELETE_WINDOW", self.close)
    #     adding input
        self.name = Label(self.bottom, text="Name",
                          font="centaur 11", bg="#00d8d6")
        self.name.place(x=40, y=20)
        self.name1 = Entry(self.bottom, font="centaur 11", bg="white")
        self.name1.place(x=160, y=20)
    #     adding button
        self.btnicon2 = PhotoImage(file="icon\\cata_button.png")
        self.add_cata = Button(self.bottom, image=self.btnicon2, compound=LEFT, text="Add Category",
                                 font="calibri 11", bg="white", width=180,command=self.add_category)
        self.add_cata.place(x=130, y=80)
    def close(self):
        self.destroy()
    def add_category(self):
        name=self.name1.get()
        if db.search_cate(str(name)):
            messagebox.showerror(title="Already exists", message="This Category is already present")
        else:
            db.add_category(name)
            messagebox.showinfo(title="Category Added", message="Category is Added")



# ////////////////////////////////////////////////////////////
# /////////class for procuct/////////////////////////
# ////////////////////////////////////////////////////
class add_product(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("400x400")
        self.resizable(False, False)
        self.title("Add Product")
        self.iconbitmap("icon\\p_icon.ico")
        # Frames/////////////////////////////////////////////
        # Frames/////////////////////////////////////////////
        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=450, bg="#00d8d6")
        self.bottom.pack(fill=X)
        # styling///////////////////
        # Heading,image and date in top frame
        self.top_image = PhotoImage(file="icon\\product_logo.png")
        self.toplbl = Label(self.top, image=self.top_image, bg="white")
        self.toplbl.grid(row=0, column=0, padx=40)
        self.heading = Label(self.top, text="Add Product",
                             font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        # Label 1
        self.name = Label(self.bottom, text="Name",
                          font="centaur 11", bg="#00d8d6")
        self.name.place(x=40, y=20)
        self.name1 = Entry(self.bottom, font="calibri 11", bg="white")
        self.name1.place(x=160, y=20)
        # label2
        self.p_price = Label(self.bottom, text="Price",
                                font="centaur 11", bg="#00d8d6")
        self.p_price.place(x=40, y=50)
        self.p_price1 = Entry(self.bottom, font="calibri 11", bg="white")
        self.p_price1.place(x=160, y=50)
        # label 3
        self.p_quantity = Label(self.bottom, text="Stock.",
                           font="centaur 11", bg="#00d8d6")
        self.p_quantity.place(x=40, y=80)
        self.p_quantity1 = Entry(self.bottom, font="calibri 11", bg="white")
        self.p_quantity1.place(x=160, y=80)
        # password
        self.p_cata = Label(self.bottom, text="Category.",
                         font="calibri 11", bg="#00d8d6")
        self.p_cata.place(x=40, y=120)
        # variable to get category value
        self.cate_value = StringVar()
        # list for category
        self.cate_list=list(db.cate_list())
        self.p_cata = ttk.Combobox(self.bottom, textvariable=self.cate_value,values=self.cate_list)
        self.p_cata.configure(state="readonly")
        self.p_cata.place(x=160, y=120)
        # btn/////////////////////
        self.btnicon2 = PhotoImage(file="icon\\pro_btn.png")
        self.add_product= Button(self.bottom, image=self.btnicon2, compound=LEFT, text="Add Product",
                                 font="calibri 11", bg="white", width=180,command=self.add_product)
        self.add_product.place(x=130, y=180)
        # handle close
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.destroy()
    def add_product(self):
        name=self.name1.get()
        price=self.p_price1.get()
        quantity=self.p_quantity1.get()
        category=self.cate_value.get()
        db.add_product(name,price,quantity,category)
        messagebox.showinfo(title="Product Added", message="Product is Added")
        db.sold_when_admin_add()