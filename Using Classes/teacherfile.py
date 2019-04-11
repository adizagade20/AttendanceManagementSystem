from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from tkinter.ttk import Combobox
from tkinter.ttk import Separator
import mysql.connector



class LabeledEntry(Entry):
    def __init__(self, master=None, label="", **kwargs):
        Entry.__init__(self, master, **kwargs)
        self.label = label
        self.on_exit()
        self.bind('<FocusIn>', self.on_entry)
        self.bind('<FocusOut>', self.on_exit)

    def on_entry(self, event=None):
        if self.get() == self.label:
            self.delete(0, END)

    def on_exit(self, event=None):
        if not self.get():
            self.insert(0, self.label)




class TeacherRoot:
	def __init__(self, root):
		self.master = root
		self.TeacherFrame = Frame(self.master)
		self.AddStudentFrame = Frame(self.master)
		self.MarkAttendanceFrame = Frame(self.master)
		self.DeleteStudentFrame = Frame(self.master)
		self.ShowDeletedStudentsFrame = Frame(self.master)
		self.canvas = Canvas(self.master)
		self.varlist = []
		self.columnnames = []
		self.check = []
		self.rollname = StringVar()
		self.columnvariable = StringVar()
		self.subs = ("Roll_No", "PRN_Number", "Name", "AM4", "AM4_Tut", "AOA", "AOA_Lab", "CG", "CG_Lab", "OS", "OS_Lab", "COA", "COA_Lab", "OSTL_Th", "OSTL")
		self.database = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
		self.mycursor = self.database.cursor()
		self.mycursor.execute("SELECT * FROM attendance")
		self.alldata2 = self.mycursor.fetchall()
		self.alldata=[]
		for i in range(len(self.alldata2)):
			if self.alldata2[i][15]!=1:
				self.alldata.append((self.alldata2[i]))


	def teachercall(self):
		self.TeacherFrame.destroy()
		self.AddStudentFrame.destroy()
		self.MarkAttendanceFrame.destroy()
		try:
			self.MarkAttendanceFrame2.destroy()
		except:
			pass
		self.DeleteStudentFrame.destroy()
		self.ShowDeletedStudentsFrame.destroy()
		self.canvas.destroy()
		self.__init__(self.master)

		fontchange = Font(family="Courier", size=14)
		Button(self.TeacherFrame, font = fontchange, text = "Add Student", relief = RAISED,
			   padx = 15, pady = 5, bg = "YELLOW", fg = "RED", bd = 2, activebackground = "BLUE",
			   activeforeground = "WHITE", height = 1, command = self.addstudent).pack()
		Button(self.TeacherFrame, font = fontchange, text = "Mark Attendance", relief = RAISED,
			   padx = 10, pady = 3, bg = "YELLOW", fg = "RED", bd = 2, activebackground = "BLUE",
			   activeforeground = "WHITE", height = 1, command = self.markattendance).pack()
		Button(self.TeacherFrame, font = fontchange, text = "Check Attendace", relief = RAISED,
			   padx = 10, pady = 3, bg = "YELLOW", fg = "RED", bd = 2, activebackground = "BLUE",
			   activeforeground = "WHITE", height = 1, command = self.checkattendance).pack()
		Button(self.TeacherFrame, font = fontchange, text = "Delete Student", relief = RAISED,
			   padx = 10, pady = 3, bg = "YELLOW", fg = "RED", bd = 2, activebackground = "BLUE",
			   activeforeground = "WHITE", height = 1, command = self.deletestudent).pack()
		Button(self.TeacherFrame, font=fontchange, text="Show Deleted Student List", relief=RAISED,
			   padx=10, pady=3, bg="YELLOW", fg="RED", bd=2, activebackground="BLUE",
			   activeforeground="WHITE", height=1, command=self.showdeletedstudents).pack()
		self.TeacherFrame.pack(side=TOP, fill="both", expand=True)


	def addstudent(self):
		self.TeacherFrame.destroy()
		self.AddStudentFrame.destroy()
		self.MarkAttendanceFrame.destroy()
		try:
			self.MarkAttendanceFrame2.destroy()
		except:
			pass
		self.DeleteStudentFrame.destroy()
		self.ShowDeletedStudentsFrame.destroy()
		self.canvas.destroy()
		self.__init__(self.master)

		Label(self.AddStudentFrame, text = "Enter student details", font = Font(size = 12)).grid(row = 1, column = 0, columnspan = 2)
		subs = ("Roll_No", "PRN_Number", "Name", "AM4", "AM4_Tut", "AOA", "AOA_Lab", "CG", "CG_Lab", "OS", "OS_Lab", "COA", "COA_Lab", "OSTL_Th", "OSTL")
		Label(self.AddStudentFrame, text = "* mark means it is compulsory", fg = "BLUE").grid(row=0, column=2)
		for i in range(len(self.subs)):
			if self.subs[i]!="Name":
				var = IntVar()
				Label(self.AddStudentFrame, text = subs[i]).grid(row = i+2, column = 0, stick = W)
				if subs[i] == 'Roll_No' or subs[i] == 'PRN_Number' or subs[i] == 'Name':
					Label(self.AddStudentFrame, text = '*', width = 1).grid(row = i+2, column = 1, stick = W)
				Entry(self.AddStudentFrame, width=32, textvariable=var).grid(row = i+2, column = 2)
				self.varlist.append(var)
			else:
				var = StringVar()
				Label(self.AddStudentFrame, text=subs[i]).grid(row=i+2, column=0, stick=W)
				if subs[i]=='Roll_No' or subs[i]=='PRN_Number' or subs[i]=='Name':
					Label(self.AddStudentFrame, text = '*', width = 1).grid(row = i+2, column = 1, stick = W)
				LabeledEntry(self.AddStudentFrame, label="First Name Middle Name Last Name", width=32, textvariable=var).grid(row=i+2, column=2)
				self.varlist.append(var)
		Button(self.AddStudentFrame, text = "Save", font = Font(size = 14), padx = 15, pady = 3, bg = "BLUE", fg = "WHITE", command = self.fetchdata).grid(row=i+4, column=0, columnspan=2, padx = 20, pady = 10)
		self.AddStudentFrame.pack(side = TOP, fill = "both", expand = True, padx = 300, pady = 50)


	def fetchdata(self):
		try:
			self.data = []
			count=0
			for i in range(len(self.varlist)):
				self.data.append(self.varlist[i].get())
				count+=1
		except:
			if count is not 2:
				messagebox.showerror("Wrong input", "You are trying to enter string in integer")
			else:
				messagebox.showerror("Wrong input", "Name must be 'string'")

		for j in range(3, len(self.data)):
			if self.data[j] == 'NULL':
				self.data[j] = 0

		try:
			if self.data[0]==0 or self.data[1]==0 or self.data[2]=='':
				messagebox.showwarning("Insufficient data", "Data entered by you is not sufficient", icon="warning")
			else:
				sql = "INSERT INTO attendance(Roll_No, PRN_Number, Name, Am4, AM4_Tutorial, AOA, AOA_Practical, CG, CG_Practical, OS, OS_Practical, COA, COA_Practical, OSTL, OSTL_Practical, IsDeleted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0)"
				self.mycursor.execute(sql, self.data)
				self.database.commit()
				messagebox.showinfo("Congo", "Student successfully added")
		except mysql.connector.errors.IntegrityError:
			messagebox.showerror("Duplicate Entry", "Please enter valid details")
		except mysql.connector.errors.ProgrammingError:
			pass
		except:
			messagebox.showwarning("Insufficient data", "Data entered by you is not sufficient", icon="warning")


	def markattendance(self):
		self.TeacherFrame.destroy()
		self.AddStudentFrame.destroy()
		self.MarkAttendanceFrame.destroy()
		try:
			self.MarkAttendanceFrame2.destroy()
		except:
			pass
		self.DeleteStudentFrame.destroy()
		self.ShowDeletedStudentsFrame.destroy()
		self.canvas.destroy()
		self.__init__(self.master)
		
		self.mycursor.execute("DESCRIBE attendance")
		self.AllColumnNames = self.mycursor.fetchall()
		for i in range(len(self.AllColumnNames)-1):
			if i in range(3):
				continue
			else:
				self.columnnames.append(self.AllColumnNames[i][0])
		Label(self.MarkAttendanceFrame, text="Choose Subject to Mark Attendance :").pack()
		class_dropdown = Combobox(self.MarkAttendanceFrame, values=self.columnnames, textvariable=self.columnvariable)
		class_dropdown.current(0)
		class_dropdown.pack()
		Button(self.MarkAttendanceFrame, text="Sumbit", padx=10, pady=2, relief=RAISED, fg="BLACK", activebackground="GREEN", activeforeground="WHITE", command=self.markattendance2).pack()
		self.MarkAttendanceFrame.pack()


	def markattendance2(self):
		self.canvas.pack(side = LEFT, fill = "both", expand = True, padx = 10, pady = 10)
		self.MarkAttendanceFrame2 = Frame(self.canvas)
		self.scrollbary = Scrollbar(self.master, orient = VERTICAL, command = self.canvas.yview)
		self.scrollbary.pack(side = RIGHT, fill = Y)
		self.canvas.configure(yscrollcommand = self.scrollbary.set)
		self.canvas.bind('<Configure>', self.on_configure)
		self.canvas.create_window((0, 0), window = self.MarkAttendanceFrame2, anchor = 'nw')
		for i in range(len(self.alldata)):
			if self.alldata[i][15] != 1:
				var = IntVar()
				Label(self.MarkAttendanceFrame2, text = self.alldata[i][0], width = 6).grid(row = i, column = 0)
				Label(self.MarkAttendanceFrame2, text = self.alldata[i][1], width = 12).grid(row = i, column = 1)
				Label(self.MarkAttendanceFrame2, text = self.alldata[i][2], width = 30).grid(row = i, column = 2, stick = W)
				Checkbutton(self.MarkAttendanceFrame2, text="Tick if Present", variable=var, offvalue=0, onvalue=1).grid(row=i, column=7)
				self.check.append(var)
		Button(self.MarkAttendanceFrame2, text="Save Attendance", bg="ORANGE", fg="YELLOW", command=self.getattendancemarked).grid(row = i+1, column = 2, padx=10, pady=20)
		self.MarkAttendanceFrame2.pack(side=TOP)


	def getattendancemarked(self):
		count = 2
		for n in self.columnnames:
			count+=1
			if n == self.columnvariable.get():
				break
		self.attend = []
		for i in range(len(self.check)):
			self.attend.append(self.check[i].get())
		i = 0
		x = []
		for i in range(len(self.attend)):
			if self.attend[i] == 1:
				subject = self.columnvariable.get()
				roll = self.alldata[i][0]
				x.append(self.alldata[i][0])
				new = self.alldata[i][count] + 1
				data = []
				j=0
				for i in self.alldata[i]:
					if j!=count:
						data.append(i)
					else:
						data.append(new)
					j+=1
				sql = ("DELETE FROM attendance WHERE Roll_No=%s")
				key = (roll, )
				self.mycursor.execute(sql, key)
				sql2 = "INSERT INTO attendance(Roll_No, PRN_Number, Name, Am4, AM4_Tutorial, AOA, AOA_Practical, CG, CG_Practical, OS, OS_Practical, COA, COA_Practical, OSTL, OSTL_Practical, IsDeleted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0)"
				key2 = (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], )
				self.mycursor.execute(sql2, key2, )
		a = messagebox.askyesno("Confirm", ("Attendance for ",x))
		if(a==True):
			self.database.commit()
			self.destroy2()
		elif(a==False):
			messagebox.showinfo("Not saved", "Attendance not updated")
			self.destroy2()
			

	def checkattendance(self):
		self.TeacherFrame.destroy()
		self.AddStudentFrame.destroy()
		self.MarkAttendanceFrame.destroy()
		try:
			self.MarkAttendanceFrame2.destroy()
		except:
			pass
		self.DeleteStudentFrame.destroy()
		self.ShowDeletedStudentsFrame.destroy()
		self.canvas.destroy()
		self.__init__(self.master)
		
		self.MarkAttendanceFrame2 = Frame(self.canvas)
		self.canvas.pack(side = LEFT, fill = "both", expand = True, padx = 10, pady = 10)
		self.scrollbary = Scrollbar(self.master, orient = VERTICAL, command = self.canvas.yview)
		self.scrollbary.pack(side = RIGHT, fill = Y)
		self.scrollbarx = Scrollbar(self.master, orient = HORIZONTAL, command = self.canvas.xview)
		self.scrollbarx.pack(side = BOTTOM, fill = X)
		self.canvas.configure(xscrollcommand = self.scrollbarx.set, yscrollcommand = self.scrollbary.set)
		self.canvas.bind('<Configure>', self.on_configure)
		self.CheckAttendanceFrame = Frame(self.canvas)
		self.canvas.create_window((0,0), window = self.CheckAttendanceFrame, anchor = "nw")
		#self.mycursor.execute("SELECT * FROM attendance")
		#self.result = self.mycursor.fetchall()
		size = range(1,50,2)
		Separator(self.CheckAttendanceFrame, orient=HORIZONTAL).grid(row=0, column=0, columnspan=50, sticky='ew')
		for i in range(len(self.subs)):
			if self.subs[i] == "Name":
				Label(self.CheckAttendanceFrame, text = self.subs[i], width = 25).grid(row = 1, column = size[i], stick = W)
			elif self.subs[i] == "PRN_Number":
				Label(self.CheckAttendanceFrame, text = self.subs[i], width = 10).grid(row = 1, column = size[i], stick = W)
			else:
				Label(self.CheckAttendanceFrame, text = self.subs[i], width = 7).grid(row = 1, column = size[i], stick = W)
			Separator(self.CheckAttendanceFrame, orient = VERTICAL).grid(row = 1, column = size[i]-1, sticky = 'ns')
		self.total = Label(self.CheckAttendanceFrame, text = "Total", width = 7, font = Font(size = 12), fg = "GREEN").grid(row = 1, column = size[i]+2, stick = W)
		Separator(self.CheckAttendanceFrame, orient = VERTICAL).grid(row = 1, column = size[i]+1, sticky = 'ns')
		Separator(self.CheckAttendanceFrame, orient = VERTICAL).grid(row = 1, column = size[i]+3, sticky = 'ns')
		Separator(self.CheckAttendanceFrame, orient=HORIZONTAL).grid(row=2, column=0, columnspan=50, sticky='ew')

		for i in range(len(self.alldata)):
			if self.alldata[i][len(self.subs)] == 1:
				continue
			for j in range(len(self.subs)):
				Label(self.CheckAttendanceFrame, text = self.alldata[i][j]).grid(row = i+5, column = size[j], stick = E)
				Separator(self.CheckAttendanceFrame, orient=VERTICAL).grid(row = i+5, column = size[j]-1, sticky='ns')
			Separator(self.CheckAttendanceFrame, orient=VERTICAL).grid(row = i+5, column = size[j]+1, sticky='ns')
			self.total = self.alldata[i][3] + self.alldata[i][4] + self.alldata[i][5] + self.alldata[i][6] + self.alldata[i][7] + self.alldata[i][8] + self.alldata[i][9] + self.alldata[i][10] + self.alldata[i][11] + self.alldata[i][12] + self.alldata[i][13] + self.alldata[i][14]
			Label(self.CheckAttendanceFrame, text = self.total, font = Font(size = 12), fg = "GREEN").grid(row = i+5, column = size[j]+2, stick = E)
			Separator(self.CheckAttendanceFrame, orient=VERTICAL).grid(row = i+5, column = size[j]+3, sticky='ns')
		Separator(self.CheckAttendanceFrame, orient=HORIZONTAL).grid(row = i+6, column = 0, columnspan=50, sticky='ew')


	def on_configure(self, event):
		self.canvas.configure(scrollregion = self.canvas.bbox('all'))


	def deletestudent(self):
		self.TeacherFrame.destroy()
		self.AddStudentFrame.destroy()
		self.MarkAttendanceFrame.destroy()
		try:
			self.MarkAttendanceFrame2.destroy()
		except:
			pass
		self.DeleteStudentFrame.destroy()
		self.ShowDeletedStudentsFrame.destroy()
		self.canvas.destroy()
		self.__init__(self.master)
		
		self.mycursor.execute("SELECT Roll_No, Name, IsDeleted FROM attendance")
		self.rollandname2 = self.mycursor.fetchall()
		self.rollandname = []
		for i in self.rollandname2:
			if i[2] == 1:
				continue
			else:
				self.rollandname.append(i[0:2])

		self.rollandname_dropdown = Combobox(self.DeleteStudentFrame, values=self.rollandname, textvariable=self.rollname, width=30)
		self.rollandname_dropdown.current(0)
		self.rollandname_dropdown.place(x=400, y=100)
		Button(self.DeleteStudentFrame, text="Delete", bg="ORANGE", fg="YELLOW", command=self.finaldelete, padx=15, pady=5).place(x=450, y=150)
		self.DeleteStudentFrame.pack(side=TOP, fill="both", expand=True)


	def finaldelete(self):
		self.data = self.rollname.get()
		ans = messagebox.askyesno("Delete", "Are yu sure to delete : "+self.data, icon = "warning")
		if ans:
			sql = "UPDATE attendance SET IsDeleted=1 where Roll_No=%s"
			key = (self.data[0]+self.data[1], )
			self.mycursor.execute(sql, key)
			self.database.commit()
			messagebox.showinfo("Congo", "Deleted successfully : "+self.data)


	def showdeletedstudents(self):
		self.TeacherFrame.destroy()
		self.AddStudentFrame.destroy()
		self.MarkAttendanceFrame.destroy()
		try:
			self.MarkAttendanceFrame2.destroy()
		except:
			pass
		self.DeleteStudentFrame.destroy()
		self.ShowDeletedStudentsFrame.destroy()
		self.canvas.destroy()
		self.__init__(self.master)
		
		list = []
		for i in range(len(self.alldata2)):
			print(self.alldata2[i][len(self.subs)])
			if self.alldata2[i][len(self.subs)]==1:
				list.append(self.alldata2[i])
		print(list)

		size = range(1, 50, 2)
		Separator(self.ShowDeletedStudentsFrame, orient=HORIZONTAL).grid(row=0, column=0, columnspan=50, sticky='ew')
		for i in range(len(self.subs)):
			if self.subs[i] == "Name":
				Label(self.ShowDeletedStudentsFrame, text=self.subs[i], width=25).grid(row=1, column=size[i], stick=W)
			elif self.subs[i] == "PRN_Number":
				Label(self.ShowDeletedStudentsFrame, text=self.subs[i], width=10).grid(row=1, column=size[i], stick=W)
			else:
				Label(self.ShowDeletedStudentsFrame, text=self.subs[i], width=7).grid(row=1, column=size[i], stick=W)
			Separator(self.ShowDeletedStudentsFrame, orient=VERTICAL).grid(row=1, column=size[i] - 1, sticky='ns')
		self.total = Label(self.ShowDeletedStudentsFrame, text="Total", width=7, font=Font(size=12), fg="GREEN").grid(row=1, column= size[i]+2, stick=W)
		Separator(self.ShowDeletedStudentsFrame, orient=VERTICAL).grid(row=1, column=size[i] + 1, sticky='ns')
		Separator(self.ShowDeletedStudentsFrame, orient=VERTICAL).grid(row=1, column=size[i] + 3, sticky='ns')
		Separator(self.ShowDeletedStudentsFrame, orient=HORIZONTAL).grid(row=2, column=0, columnspan=50, sticky='ew')

		for i in range(len(list)):
			for j in range(len(self.subs)):
				Label(self.ShowDeletedStudentsFrame, text=list[i][j]).grid(row=i+5, column=size[j], stick=E)
				Separator(self.ShowDeletedStudentsFrame, orient=VERTICAL).grid(row=i + 5, column=size[j] - 1, sticky='ns')
			Separator(self.ShowDeletedStudentsFrame, orient=VERTICAL).grid(row=i + 5, column=size[j] + 1, sticky='ns')
			self.total = list[i][3] + list[i][4] + list[i][5] + list[i][6] + list[i][7] + list[i][8] + list[i][9] + list[i][10] + list[i][11] + list[i][12] + list[i][13] + list[i][14]
			Label(self.ShowDeletedStudentsFrame, text=self.total, font=Font(size=12), fg="GREEN").grid(row=i+5, column=size[j]+2, stick=E)
			Separator(self.ShowDeletedStudentsFrame, orient=VERTICAL).grid(row=i + 5, column=size[j] + 3, sticky='ns')
		Separator(self.ShowDeletedStudentsFrame, orient=HORIZONTAL).grid(row=i + 6, column=0, columnspan=50, sticky='ew')
		self.ShowDeletedStudentsFrame.pack(side=TOP, fill="both", expand=True)
		
		
	def destroy2(self):
		self.TeacherFrame.destroy()
		self.AddStudentFrame.destroy()
		self.MarkAttendanceFrame.destroy()
		try:
			self.MarkAttendanceFrame2.destroy()
		except:
			pass
		self.DeleteStudentFrame.destroy()
		self.ShowDeletedStudentsFrame.destroy()
		self.canvas.destroy()