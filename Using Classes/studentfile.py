from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from tkinter.ttk import Combobox
from tkinter.ttk import Separator
import mysql.connector


class StudentRoot:
	def __init__(self, root):
		self.master = root
		self.StudentFrame = Frame(self.master)
		self.DisplayStudentFrame = Frame(self.master)
		self.prn_variable = IntVar()
		self.database = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
		self.mycursor = self.database.cursor()


	def studentcall(self):
		change_font = Font(family = "Courier", size = 12)
		label = Label(self.StudentFrame, text="Choose your PRN Number :- ", font = change_font).place(x = 240, y = 30)
		self.mycursor.execute("select PRN_Number, IsDeleted from attendance")
		self.prn_numbers = self.mycursor.fetchall()
		prn = []
		for i in range(len(self.prn_numbers)):
			if self.prn_numbers[i][1] == 0:
				prn.append(self.prn_numbers[i][0])
		Combobox(self.StudentFrame, values=prn, textvariable=self.prn_variable).place(x=540, y=30)
		Button(self.StudentFrame, text = "Search", padx = 10, pady = 2, relief = RAISED, fg = "BLACK", activebackground="GREEN", activeforeground="WHITE", command=self.search_details).place(x=440, y=80)
		self.StudentFrame.pack(side=TOP, fill="both", expand=True)


	def search_details(self):
		self.sql = "SELECT * FROM attendance WHERE PRN_Number='%s'"
		self.key = (self.prn_variable.get(), )
		self.mycursor.execute(self.sql, self.key)
		self.details = self.mycursor.fetchall()
		self.columns = ("Roll_No", "PRN_Number", "Name", "AM4", "AM4_Tut", "AOA", "AOA_Lab", "CG", "CG_Lab", "OS", "OS_Lab", "COA", "COA_Lab", "OSTL_Th", "OSTL")
		for i in range(len(self.columns)-1):
			Label(self.DisplayStudentFrame, text = self.columns[i]).grid(row = i+6, column = 6, stick = W)
			Label(self.DisplayStudentFrame, text = self.details[0][i]).grid(row = i+6, column = 7, stick = E)
		self.DisplayStudentFrame.pack(side=TOP, fill="both", expand=True, padx=350)