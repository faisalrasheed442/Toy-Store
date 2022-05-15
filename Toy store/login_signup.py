from tkinter import *
import customer_window as cust
import admin_window as ad
from tkinter import messagebox
import database as db
import employ_window as emp
class signup_admin(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("400x400")
        self.resizable(False, False)
        self.title("Add Admin")
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
        self.heading = Label(self.top, text="Register",
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

        # password
        self.pas = Label(self.bottom, text="Password.",
                           font="centaur 11", bg="#00d8d6")
        self.pas.place(x=40, y=80)
        self.password = Entry(self.bottom, font="calibri 11", bg="white")
        self.password.place(x=160, y=80)
        # btn/////////////////////
        self.btnicon2 = PhotoImage(file="icon\\add_btn.png")
        self.add_member = Button(self.bottom, image=self.btnicon2, compound=LEFT, text="Add member",
                                 font="centaur 11", bg="white", width=180,command=self.add_admin)
        self.add_member.place(x=130, y=150)
        # handle close
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.destroy()
    def add_admin(self):
        name=self.name1.get()
        email=self.Email_name1.get()
        password=self.password.get()
        if db.search_admin_email("admin",str(email)):
            messagebox.showerror(title="Already exists", message="This email is already registered")
        else:
            db.admin_signup(name,email,password)
            messagebox.showinfo(title="Registered", message="Admin is Registered")
            self.destroy()
# /////////////////////////////////////////////////////////////
# /////////////////////////Login/////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////
class login_form(Toplevel):

    def __init__(self,time):
        Toplevel.__init__(self)
        self.time = time
        self.geometry("400x400")
        self.resizable(False, False)
        self.title("Login")
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
        self.heading = Label(self.top, text="Login",
                             font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        # label2
        self.Email_name = Label(self.bottom, text="Email Address",
                                     font="centaur 11", bg="#00d8d6")
        self.Email_name.place(x=40, y=20)
        self.Email_name1 = Entry(self.bottom, font="calibri 11", bg="white")
        self.Email_name1.place(x=160, y=20)

        # password
        self.pas = Label(self.bottom, text="Password.",
                           font="centaur 11", bg="#00d8d6")
        self.pas.place(x=40, y=80)
        self.password = Entry(self.bottom,show='*', font="calibri 11", bg="white")
        self.password.place(x=160, y=80)
        # btn/////////////////////
        self.btnicon2 = PhotoImage(file="icon\\login.png")
        self.login = Button(self.bottom, image=self.btnicon2, compound=LEFT, text="Login",
                                 font="centaur 11", bg="white", width=180,command=self.add_admin)
        self.login.place(x=130, y=150)
        # handle close
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.destroy()
    def add_admin(self):
        email=self.Email_name1.get()
        password=self.password.get()
        if db.verify_login("admin",email,password):
            self.destroy()
            ad.admin_login(self.time)
        else:
            messagebox.showerror(title="Invalid ", message="Invalid Email or Password ")
 # /employ class//////////////
class employ_login(login_form):
    def add_admin(self):
        email=self.Email_name1.get()
        password=self.password.get()
        if db.verify_login("employ",email,password):
            self.destroy()
            emp.employ_login()
        else:
            messagebox.showerror(title="Invalid ", message="Invalid Email or Password ")

#         ///////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////
