from tkinter import *
import tkinter as tk
import database as db
from tkinter import messagebox
class add_details(Toplevel):
    def __init__(self,id):
        Toplevel.__init__(self)
        self.key=id
        self.size=self.geometry("400x300")
        self.resizable(False, False)
        self.title("Details")
        self.iconbitmap("icon\\comment.ico")
        # Frames/////////////////////////////////////////////
        # Frames/////////////////////////////////////////////
        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=650, bg="#00d8d6")
        self.bottom.pack(fill=X)
        # styling///////////////////
        # Heading,image and date in top frame
        self.top_image = PhotoImage(file="icon\\der.png")
        self.toplbl = Label(self.top, image=self.top_image, bg="white")
        self.toplbl.grid(row=0, column=0, padx=40)
        self.heading = Label(self.top, text="All About Toys LTD",
                             font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        self.comment = Label(self.bottom, text="Product Details:",
                          font="centaur 11", bg="#00d8d6").place(x=10,y=10)
        self.comment1 = Text(self.bottom,width=45, height=7,bg="white")
        self.comment1.place(x=10,y=40)

        # chat butoon
        self.chat_img = PhotoImage(file="icon\\chat.png")
        self.chat_button = tk.Button(self.bottom, image=self.chat_img, compound=LEFT, text=" Add",
                                    width=180,command=self.add_details)
        self.chat_button.place(x=110, y=180)

        # employ
        # chat function
        data = db.sp_details(self.key)
        try:

            self.comment1.insert(INSERT,data[0][0])
        except:
            pass
    def add_details(self):
        comment=self.comment1.get("1.0","end-1c")
        db.add_product_details(self.key,comment)
        messagebox.showinfo("Details Added","Details has been added")
        self.destroy()