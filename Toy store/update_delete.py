from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database as db
class add_employ(Toplevel):
    def __init__(self,id,name,email,phone,password,update='disabled',delete='disabled',iput='readonly',):
        Toplevel.__init__(self)
        self.id=id
        self.geometry("400x400")
        self.resizable(False, False)
        self.title("Update")
        self.iconbitmap("icon\\logo.ico")
        # Frames/////////////////////////////////////////////
        # Frames/////////////////////////////////////////////
        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=450, bg="#00d8d6")
        self.bottom.pack(fill=X)
        # styling///////////////////
        # Heading,image and date in top frame
        self.top_image = PhotoImage(file="icon\\logo.png")
        self.toplbl = Label(self.top, image=self.top_image, bg="white")
        self.toplbl.grid(row=0, column=0, padx=40)
        self.heading = Label(self.top, text="Update Member",
                             font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        # Label 1
        self.name = Label(self.bottom, text="Name",
                          font="centaur 11", bg="#00d8d6")
        self.name.place(x=40, y=20)
        self.name1 = Entry(self.bottom, font="calibri 11", bg="white")
        self.name1.insert(0,name)
        self.name1.config(state=iput)
        self.name1.place(x=160, y=20)
        # label2
        self.Email_name = Label(self.bottom, text="Email Address",
                                     font="centaur 11", bg="#00d8d6")
        self.Email_name.place(x=40, y=50)
        self.Email_name1 = Entry(self.bottom, font="calibri 11", bg="white")
        self.Email_name1.insert(0,email)
        self.Email_name1.config(state=iput)
        self.Email_name1.place(x=160, y=50)
        # label 3
        self.phone = Label(self.bottom, text="Contact No.",
                           font="centaur 11", bg="#00d8d6")
        self.phone.place(x=40, y=80)
        self.phone1 = Entry(self.bottom, font="calibri 11", bg="white")
        self.phone1.place(x=160, y=80)
        self.phone1.insert(0,phone)
        self.phone1.config(state=iput)
        # password
        self.pas = Label(self.bottom, text="Password.",
                           font="centaur 11", bg="#00d8d6")
        self.pas.place(x=40, y=120)
        self.password = Entry(self.bottom, font="calibri 11", bg="white")
        self.password.insert(0,password)
        self.password.config(state=iput)
        self.password.place(x=160, y=120)
        # btn/////////////////////
        self.btnicon2 = PhotoImage(file="icon\\update_btn.png")
        self.update_member = Button(self.bottom, image=self.btnicon2, compound=LEFT, text="Update member",
                                 font="centaur 11", bg="white", width=180,command=self.update_employ)
        self.update_member.place(x=130, y=180)
        self.update_member.config(state=update)
        # btn for delete
        self.btnicon = PhotoImage(file="icon\\delete.png")
        self.delete_member = Button(self.bottom, image=self.btnicon, compound=LEFT, text="Delete member",
                                 font="centaur 11", bg="white", width=180, command=self.delete_employ)
        self.delete_member.place(x=130, y=260)
        self.delete_member.config(state=delete)
        # handle close
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.destroy()
    def update_employ(self):
        name=self.name1.get()
        email=self.Email_name1.get()
        contact=self.phone1.get()
        password=self.password.get()
        id=self.id
        done=db.update_employ(id,name,email,contact,password)
        if done:
            messagebox.showinfo(title="Updated", message="Employ is Updated")
            self.destroy()
        else:
            messagebox.showerror(title="Failed",message="failed to update")
    def delete_employ(self):
        id=self.id
        mbox=messagebox.askquestion(title="Delete",message='Are you sure you want to Delete',icon = 'warning')
        if mbox=='yes':
            db.delete('employ',id)
            self.destroy()
        else:
            pass
# adding  add cata class
class add_category(Toplevel):
    def __init__(self,id,name,update='disabled',delete='disabled',iput='readonly'):
        Toplevel.__init__(self)
        self.id=id
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
                             font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        # handle close
        self.protocol("WM_DELETE_WINDOW", self.close)
    #     adding input
        self.name = Label(self.bottom, text="Name",
                          font="centaur 11", bg="#00d8d6")
        self.name.place(x=40, y=20)
        self.name1 = Entry(self.bottom, font="calibri 11", bg="white")
        self.name1.place(x=160, y=20)
        self.name1.insert(0,name)
        self.name1.config(state=iput)
    #     adding button
        self.btnicon2 = PhotoImage(file="icon\\update_btn.png")
        self.update_cata = Button(self.bottom, image=self.btnicon2, compound=LEFT, text="Update Category",
                                 font="centaur 11", bg="white", width=180,command=self.add_category)
        self.update_cata.place(x=130, y=80)
        self.update_cata.config(state=update)
        # delete btn
        self.btnicon = PhotoImage(file="icon\\delete.png")
        self.delete_cata = Button(self.bottom, image=self.btnicon, compound=LEFT, text="Delete",
                                 font="centaur 11", bg="white", width=180,command=self.del_category)
        self.delete_cata.place(x=130, y=130)
        self.delete_cata.config(state=delete)
    def close(self):
        self.destroy()
    def add_category(self):
        name=self.name1.get()
        id=self.id
        done = db.update_category(id, name)
        if done:
            messagebox.showinfo(title="Updated", message="Category is Updated")
            self.destroy()
        else:
            messagebox.showerror(title="Failed", message="Failed to Update")
    def del_category(self):
        id = self.id
        mbox = messagebox.askquestion(title="Delete", message='Are you sure you want to Delete', icon='warning')
        if mbox == 'yes':
            db.delete('category', id)
            self.destroy()
        else:
            pass



# ////////////////////////////////////////////////////////////
# /////////class for procuct/////////////////////////
# ////////////////////////////////////////////////////
class add_product(Toplevel):
    def __init__(self,id,name,price,quantity,category,update='disabled',delete='disabled',iput='readonly'):
        Toplevel.__init__(self)
        self.id=id
        self.geometry("400x400")
        self.resizable(False, False)
        self.title("Product")
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
        self.name1.insert(0,name)
        self.name1.config(state=iput)
        # label2
        self.p_price = Label(self.bottom, text="Price",
                                font="centaur 11", bg="#00d8d6")
        self.p_price.place(x=40, y=50)
        self.p_price1 = Entry(self.bottom, font="calibri 11", bg="white")
        self.p_price1.place(x=160, y=50)
        self.p_price1.insert(0, price)
        # self.p_price.config(state=iput)
        # label 3
        self.p_quantity = Label(self.bottom, text="Stock.",
                           font="centaur 11", bg="#00d8d6")
        self.p_quantity.place(x=40, y=80)
        self.p_quantity1 = Entry(self.bottom, font="centaur 11", bg="white")
        self.p_quantity1.place(x=160, y=80)
        self.p_quantity1.insert(0, quantity)
        # self.p_quantity1.config(state=iput)
        # category
        self.p_cata = Label(self.bottom, text="Category.",
                         font="centaur 11", bg="#00d8d6")
        self.p_cata.place(x=40, y=120)
        # variable to get category value
        self.cate_value = StringVar()
        # list for category
        self.cate_list=list(db.cate_list())
        self.p_cata = ttk.Combobox(self.bottom, textvariable=self.cate_value,values=self.cate_list)
        self.p_cata.configure(state="readonly")
        self.p_cata.place(x=160, y=120)
        # btn/////////////////////
        self.btnicon2 = PhotoImage(file="icon\\update_btn.png")
        self.upd_product= Button(self.bottom, image=self.btnicon2, compound=LEFT, text="Update Product",
                                 font="centaur 11", bg="white", width=180,command=self.update_product)
        self.upd_product.place(x=130, y=180)
        self.upd_product.config(state=update)
        # delete button
        self.btnicon = PhotoImage(file="icon\\delete.png")
        self.de_product= Button(self.bottom, image=self.btnicon, compound=LEFT, text="Delete Product",
                                 font="centaur 11", bg="white", width=180,command=self.del_product)
        self.de_product.place(x=130, y=240)
        self.de_product.config(state=delete)
        # handle close
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.destroy()

    def update_product(self):
        id = self.id
        name = self.name1.get()
        price = self.p_price1.get()
        quantity = self.p_quantity1.get()
        category = self.cate_value.get()
        done = db.update_product(id,name,price,quantity,category)
        if done:
            db.sold_update_product_update(id,name,price,category)
            messagebox.showinfo(title="Updated", message="Product is Updated")
            self.destroy()
        else:
            messagebox.showerror(title="Failed", message="Failed to Update")

    def del_product(self):
        id = self.id
        mbox = messagebox.askquestion(title="Delete", message='Are you sure you want to Delete', icon='warning')
        if mbox == 'yes':
            db.delete_comment(id)
            db.delete('product', id)
            self.destroy()
        else:
            pass


