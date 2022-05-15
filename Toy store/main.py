from tkinter import *
import tkinter as tk
import datetime
import login_signup as ls
import customer_window as cu
from tkinter import messagebox
class myapp(object):
    def __init__(self,master):
        self.win=master

        # creating two frame one above and one below with color blue and white
        self.top = Frame(master, height=100, bg="white")
        self.top.pack(fill=X)
        self.bottom = Frame(master, height=300, bg="#576574")
        self.bottom.pack(fill=X)
#         adding logo and current time in top frame
        self.top_image = PhotoImage(file="icon\\1.png")
        self.toplbl = Label(self.top, image=self.top_image, bg="white")
        self.toplbl.grid(row=0, column=0, padx=40)
        # //////////////////////////////////
        self.heading = Label(self.top, text="All About Toys LTD", font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        # setting background image
        self.filename = PhotoImage(file="icon\\bg.png")
        background_label = Label(self.bottom, image=self.filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        # ////////////////////////////////
        self.today = str(datetime.datetime.today()).split()
        self.heading_time = Label(self.top, text="Date: " + self.today[0], font="centaur 11", bg="white")
        self.heading_time.place(x=285, y=5)
#         adding buttons into below frame
#         adminn
        self.admin_img = PhotoImage(file="icon\\3.png")
        self.admin_login = tk.Button(self.bottom,image=self.admin_img,compound=LEFT, text=" Administrator", width=180,command=self.admin_login)
        # employ
        self.employ_img = PhotoImage(file="icon\\5.png")
        self.employ_login = tk.Button(self.bottom, image=self.employ_img, compound=LEFT, text="Sales Staff", width=180,command=self.employ_login)
        # user
        self.user_img=PhotoImage(file="icon\\2.png")
        self.user_login = tk.Button(self.bottom,image=self.user_img,compound=LEFT ,text="Customer", width=180,command=self.user_login)
        # exit
        self.exit_img=PhotoImage(file="icon\\4.png")
        self.exit = tk.Button(self.bottom, text="Exit",image=self.exit_img,compound=LEFT, width=180 ,command=master.destroy)
        self.admin_login.place(x=110,y=70)
        self.employ_login.place(x=110,y=120)
        self.user_login.place(x=110,y=170)
        self.exit.place(x=110,y=219)
    #     ///////////////////////////////////////////////////////////////////////////////////
    # ////////////////////////////////////////////////////////////////////////////////////////////////////
    # /////////////////////////function//////////////////////////////////////////////////////////////////

    #     to handle close exception
    def admin_login(self):
        # to get to know if the admin is new user then he will register himself
        x = messagebox.askyesno(title="Info", message="Are you a new")
        if x :
            ls.signup_admin()
        else:
            ls.login_form(self.today[0])
    def employ_login(self):
            ls.employ_login(self.today[0])
    def user_login(self):
        cu.user_login(self.today[0])
def main():
    try:
        root=tk.Tk()
        root.geometry("400x400")
        root.title("Toy Store")
        root.iconbitmap('icon\\home.ico')
        root.resizable(False, False)
        app=myapp(root)

        def on_closing():
                root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_closing)
        root.mainloop()
    except:
        exit()
if __name__ == '__main__':
    main()


