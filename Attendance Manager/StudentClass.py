from tkinter import *
from tkinter.font import Font

class Student_Class:

    def get_name(self):
        self.name = self.name_var.get()
        print(self.name)

    def __init__(self, master):
        self.master = master
        frame = Frame(master, width=700, height=500)
        fontchange = Font(family="Courier", size=12)
        entry = Label(master, text="Enter your Name :-", font=fontchange)
        entry.place(x=50, y=40)
        self.name_var = StringVar()
        enter_name = Entry(master, textvariable=self.name_var, width=30)
        enter_name.place(x=250, y=45)
        submit_button = Button(master, text="Search", padx=10, pady=2, relief=RAISED, fg="BLACK", activebackground="GREEN", activeforeground="WHITE", command = self.get_name)
        submit_button.place(x=250, y=100)
        frame.pack()