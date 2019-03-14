from tkinter import *
from tkinter.font import Font
import mysql.connector

class Teacher_Class:
    def add_student(self, frame1):
        self.frame1.destroy()
        prnlabel = Label().place()

    def add_student_patch(self, values):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
        mycursor = mydb.cursor()
        sql = "INSERT INTO attendance (PRN_Number, Name, AM4, AM4_Tutorial, AOA, AOA_Practical, CG, CG_Practical, COA, COA_Practical, OS, OS_Practical, OSTL, OSTL_Practical) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql, values)
        mydb.commit()

    def mark_attendance(self):
        pass

    def check_attendance(self):
        pass

    def check_attendance_class(self):
        pass

    def __init__(self, master):
        self.master = master
        frame1 = Frame(master, width = 700, height = 500)
        fontchange = Font(family = "Courier", size = 12)
        add = Button(frame1, font=fontchange, text="Add Student", relief=RAISED, padx=10, pady=3, bg="YELLOW", fg="RED", bd=2, activebackground="BLUE", activeforeground="WHITE", height=1, command = self.add_student)
        mark = Button(frame1, font=fontchange, text="Mark Attendance", relief=RAISED, padx=10, pady=3, bg="YELLOW", fg="RED", bd=2, activebackground="BLUE", activeforeground="WHITE", height=1, command = self.mark_attendance)
        check = Button(frame1, font=fontchange, text="Check attendace of paticular student", relief=RAISED, padx=10, pady=3, bg="YELLOW", fg="RED", bd=2, activebackground="BLUE", activeforeground="WHITE", height=1, command = self.check_attendance)
        check_class = Button(frame1, font=fontchange, text="Mark Attendance of whole class", relief=RAISED, padx=10, pady=3, bg="YELLOW", fg="RED", bd=2, activebackground="BLUE", activeforeground="WHITE", height=1, command = self.check_attendance_class)
        add.place(x=100, y=100)
        mark.place(x=400, y=100)
        check.place(x=150, y=200)
        check_class.place(x=180, y=300)
        frame1.pack()