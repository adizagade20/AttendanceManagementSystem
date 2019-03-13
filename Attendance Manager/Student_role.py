from tkinter import *
from tkinter.ttk import Combobox
from tkinter.font import Font
import mysql.connector
class Student_Class:

    def search_details(self, prn):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
        mycursor = mydb.cursor()
        sql = "SELECT * FROM attendance WHERE PRN_Number= '%d'"
        key = (prn,)
        mycursor.execute(sql, prn)
        print(mycursor.fetchone())
        details = mycursor.fetchone()
        print(details)

    def get_prn(self):
        prn_no = self.prn.get()
        print(prn_no)
        self.search_details(prn_no)

    def __init__(self, master):
        self.master = master
        frame = Frame(master, width=700, height=500)
        fontchange = Font(family="Courier", size=12)
        label = Label(master, text="Enter your Name :-", font=fontchange)
        label.place(x=50, y=40)
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
        mycursor = mydb.cursor()
        mycursor.execute("select PRN_Number from attendance")
        prn_numbers = mycursor.fetchall()
        self.prn = IntVar()
        prn_dropdown = Combobox(master, values=prn_numbers, textvariable = self.prn)
        prn_dropdown.place(x=250, y=45)
        submit_button = Button(master, text = "Search", padx = 10, pady = 2, relief = RAISED, fg = "BLACK", activebackground = "GREEN", activeforeground = "WHITE", command = self.get_prn)
        submit_button.place(x=250, y=100)
        frame.pack()


"""def dropdown():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
    mycursor = mydb.cursor()
    mycursor.execute("select PRN_Number from attendance")
    prn_numbers = mycursor.fetchall()
    #print(prn_numbers)

    root1 = Tk()
    prn_dropdown = Combobox(root1, values = )
    prn_dropdown.pack()
    root1.geometry("500x300+100+100")
    root1.mainloop()

dropdown()"""