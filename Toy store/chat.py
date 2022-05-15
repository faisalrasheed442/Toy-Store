from tkinter import *
data=list()
class my_chat(Toplevel):
    def __init__(self,name):
        Toplevel.__init__(self)
        self.geometry("400x425")
        # self.resizable(False, False)
        self.title("Chat Box")
        self.iconbitmap("icon\\add.ico")
        # /////////////////////////////////
        self.name=name
        self.top=Frame(self,width=400,height=25,bg="blue")
        self.top.pack(side=TOP)
        self.btn = Button(self.top, text="Refresh",width=60, bg="white",command=self.pri)
        self.btn.place(x=0,y=0)
        self.chat_panal = LabelFrame(self, text="Chat", borderwidth=2, width=400, height=370,
                                        relief=SUNKEN, bg="#00d8d6")
        self.chat_panal.pack(side=TOP)
        self.input_frame=Frame(self, borderwidth=2, width=400, height=30,
                                        relief=SUNKEN, bg="black")
        self.input_frame.pack(side=BOTTOM)
        self.messages = Text(self.chat_panal,width=47, height=22,bg="#00d8d6")
        self.messages.grid(row=0, column=0)
        self.slide = Scrollbar(self.chat_panal, orient="vertical", command=self.messages.yview)
        self.messages.config(yscrollcommand=self.slide.set)
        self.slide.grid(row=0, column=1, sticky=N + S + E)
        self.messages.config(state="disabled")
        self.input_user = StringVar()
        self.input_field = Entry(self.input_frame, text=self.input_user,width=100)
        self.input_field.pack(side=BOTTOM, fill=X)
        self.input_field.bind("<Return>", self.Enter_pressed)

    def Enter_pressed(self,event):
        input_get = self.input_field.get()
        if input_get:
            input_get=self.name + ": " +input_get
            data.append(input_get)
        self.messages.config(state="normal")

        self.messages.delete('1.0', END)
        for x in range(len(data)):
            self.messages.insert(INSERT, '%s\n' % data[x])
        # label = Label(window, text=input_get)
        self.input_user.set('')
        self.messages.config(state="disabled")
        # label.pack()
        return "break"
    def pri(self):
        input_get = self.input_field.get()
        if input_get:
            input_get = self.name + ": " + input_get
            data.append(input_get)
        self.messages.config(state="normal")

        self.messages.delete('1.0', END)
        for x in range(len(data)):
            self.messages.insert(INSERT, '%s\n' % data[x])
        # label = Label(window, text=input_get)
        self.input_user.set('')
        self.messages.config(state="disabled")
        # label.pack()
        return "break"
