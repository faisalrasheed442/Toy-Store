from tkinter import *
import tkinter as tk
import database as db
from tkinter import messagebox
class add_comment(Toplevel):
    def __init__(self,id):
        Toplevel.__init__(self)
        self.key=id
        self.size=self.geometry("400x500")
        self.resizable(False, False)
        self.title("Add Comment")
        self.iconbitmap("icon\\comment.ico")
        # Frames/////////////////////////////////////////////
        # Frames/////////////////////////////////////////////
        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=650, bg="#00d8d6")
        self.bottom.pack(fill=X)
        # styling///////////////////
        # Heading,image and date in top frame
        self.top_image = PhotoImage(file="icon\\chat_us.png")
        self.toplbl = Label(self.top, image=self.top_image, bg="white")
        self.toplbl.grid(row=0, column=0, padx=40)
        self.heading = Label(self.top, text="All About Toys LTD",
                             font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        # button for Generate sale report
        self.name = Label(self.bottom, text="Name:",
                          font="centaur 11", bg="#00d8d6").place(x=10,y=20)
        self.name1 = Entry(self.bottom, font="calibri 11", bg="white",width=50)
        self.name1.place(x=10,y=50)
        self.email = Label(self.bottom, text="Email:",
                          font="centaur 11", bg="#00d8d6").place(x=10,y=80)
        self.email1 = Entry(self.bottom, font="calibri 11", bg="white",width=50)
        self.email1.place(x=10,y=110)
        self.comment = Label(self.bottom, text="Comment:",
                          font="centaur 11", bg="#00d8d6").place(x=10,y=140)
        self.comment1 = Text(self.bottom,width=45, height=7,bg="white")
        self.comment1.place(x=10,y=170)

        # chat butoon
        self.chat_img = PhotoImage(file="icon\\chat.png")
        self.chat_button = tk.Button(self.bottom, image=self.chat_img, compound=LEFT, text=" Add",
                                    width=180,command=self.add_comment)
        self.chat_button.place(x=110, y=330)

        # employ
        # chat function
    def add_comment(self):
        keys=self.key
        name=self.name1.get()
        email=self.email1.get()
        comment=self.comment1.get("1.0","end-1c")
        reply=""
        db.add_comment(keys,name,email,comment,reply)
        messagebox.showinfo("Comment Added","Comment has been added")
        self.destroy()

# view class comment
class view_comment(Toplevel):
    def __init__(self,id):
        Toplevel.__init__(self)
        self.data=id
        self.size=self.geometry("400x700")
        self.resizable(False, False)
        self.title("Add Comment")
        self.iconbitmap("icon\\comment.ico")
        # Frames/////////////////////////////////////////////
        # Frames/////////////////////////////////////////////
        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=650, bg="#00d8d6")
        self.bottom.pack(fill=X)
        # styling///////////////////
        # Heading,image and date in top frame
        self.top_image = PhotoImage(file="icon\\chat_us.png")
        self.toplbl = Label(self.top, image=self.top_image, bg="white")
        self.toplbl.grid(row=0, column=0, padx=40)
        self.heading = Label(self.top, text="All About Toys LTD",
                             font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        # button for Generate sale report
        self.name = Label(self.bottom, text="Name:",
                          font="centaur 11", bg="#00d8d6").place(x=10,y=20)
        self.name1 = Entry(self.bottom, font="calibri 11", bg="white",width=50)
        self.name1.place(x=10,y=50)
        self.email = Label(self.bottom, text="Email:",
                          font="centaur 11", bg="#00d8d6").place(x=10,y=80)
        self.email1 = Entry(self.bottom, font="calibri 11", bg="white",width=50)
        self.email1.place(x=10,y=110)
        self.comment = Label(self.bottom, text="Comment:",
                          font="centaur 11", bg="#00d8d6").place(x=10,y=140)
        self.comment1 = Text(self.bottom,width=45, height=7,bg="white")
        self.comment1.place(x=10,y=170)

        self.reply = Label(self.bottom, text="Reply from Seller:",
                          font="centaur 11", bg="#00d8d6").place(x=10,y=300)
        self.reply1 = Text(self.bottom,width=45, height=7,bg="white")
        self.reply1.place(x=10,y=330)
        self.view_comment()
        # employ
        # chat function
    def view_comment(self):
        self.name1.insert(0,self.data[0][0])
        self.email1.insert(0,self.data[0][1])
        self.comment1.insert(INSERT,self.data[0][2])
        self.reply1.insert(INSERT,self.data[0][3])
        self.name1.config(state="readonly")
        self.email1.config(state="readonly")
        self.comment1.config(state="disabled")
        self.reply1.config(state="disabled")

class update_comment(Toplevel):
    def __init__(self,id):
        Toplevel.__init__(self)
        self.id=id
        self.size=self.geometry("400x700")
        self.resizable(False, False)
        self.title("Add Comment")
        self.iconbitmap("icon\\comment.ico")
        # Frames/////////////////////////////////////////////
        # Frames/////////////////////////////////////////////
        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=650, bg="#00d8d6")
        self.bottom.pack(fill=X)
        # styling///////////////////
        # Heading,image and date in top frame
        self.top_image = PhotoImage(file="icon\\chat_us.png")
        self.toplbl = Label(self.top, image=self.top_image, bg="white")
        self.toplbl.grid(row=0, column=0, padx=40)
        self.heading = Label(self.top, text="All About Toys LTD",
                             font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        # button for Generate sale report
        self.name = Label(self.bottom, text="Name:",
                          font="centaur 11", bg="#00d8d6").place(x=10,y=20)
        self.name1 = Entry(self.bottom, font="calibri 11", bg="white",width=50)
        self.name1.place(x=10,y=50)
        self.email = Label(self.bottom, text="Email:",
                          font="centaur 11", bg="#00d8d6").place(x=10,y=80)
        self.email1 = Entry(self.bottom, font="calibri 11", bg="white",width=50)
        self.email1.place(x=10,y=110)
        self.comment = Label(self.bottom, text="Comment:",
                          font="centaur 11", bg="#00d8d6").place(x=10,y=140)
        self.comment1 = Text(self.bottom,width=45, height=7,bg="white")
        self.comment1.place(x=10,y=170)

        self.reply = Label(self.bottom, text="Reply to Customer:",
                          font="centaur 11", bg="#00d8d6").place(x=10,y=300)
        self.reply1 = Text(self.bottom,width=45, height=7,bg="white")
        self.reply1.place(x=10,y=330)
        # chat butoon
        self.chat_img = PhotoImage(file="icon\\chat.png")
        self.chat_button = tk.Button(self.bottom, image=self.chat_img, compound=LEFT, text=" Update",
                                    width=180,command=self.Update_comment)
        self.chat_button.place(x=110, y=480)

        # employ
        # chat function
        self.add_values()
    def add_values(self):
        data=db.view_comment(self.id)
        self.name1.insert(0,data[0][0])
        self.email1.insert(0,data[0][1])
        self.comment1.insert(INSERT,data[0][2])
        self.reply1.insert(INSERT,data[0][3])
        self.name1.config(state="readonly")
        self.email1.config(state="readonly")
        self.comment1.config(state="disabled")
    def Update_comment(self):
        reply=self.reply1.get("1.0","end-1c")
        db.update_comment(self.id,reply)
        messagebox.showinfo("Comment Updated","Comment has been Updated")
        self.destroy()