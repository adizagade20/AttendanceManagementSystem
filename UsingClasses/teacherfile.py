from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.font import Font
from tkinter.ttk import Combobox
from tkinter.ttk import Separator
from tkinter import filedialog
import csv
import mysql.connector
import functools
import operator


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
		self.TeacherFrame = Frame(self.master, background = 'turquoise1')
		self.AddStudentFrame = Frame(self.master, background = 'turquoise1')
		self.MarkAttendanceFrame = Frame(self.master, background = 'turquoise1')
		#self.DeleteStudentFrame = Frame(self.master, background = 'turquoise1')
		self.ShowDeletedStudentsFrame = Frame(self.master, background = 'turquoise1')
		self.canvas = Canvas(self.master, background = 'turquoise1')
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
		self.alldata = []
		for i in range(len(self.alldata2)):
			if self.alldata2[i][15] != 1:
				self.alldata.append((self.alldata2[i]))
	
	
	def teachercall(self):
		self.destroy2()
		self.__init__(self.master)
		
		fontchange = Font(family="Courier", size=14)
		Button(self.TeacherFrame, font=fontchange, text="Add Student", relief=RAISED, padx=10, pady=3, bd=4, activebackground="BLUE", activeforeground="WHITE", height=1, command=self.addstudent, width=15).place(relx=0.25, rely=0.20)
		Button(self.TeacherFrame, font=fontchange, text="Delete Student", relief=RAISED, padx=10, pady=3, bd=4, activebackground="BLUE", activeforeground="WHITE", height=1, command=self.deletestudent, width=15).place(relx=0.55, rely=0.20)
		Button(self.TeacherFrame, font=fontchange, text="Mark Attendance", relief=RAISED, padx=10, pady=3, bd=4, activebackground="BLUE", activeforeground="WHITE", height=1, command=self.markattendance, width=15).place(relx=0.25, rely=0.40)
		Button(self.TeacherFrame, font=fontchange, text="Check Attendace", relief=RAISED, padx=10, pady=3, bd=4, activebackground="BLUE", activeforeground="WHITE", height=1, command=self.checkattendance, width=15).place(relx=0.55, rely=0.40)
		Button(self.TeacherFrame, font=fontchange, text="Deleted Data", relief=RAISED, padx=10, pady=3, bd=4, activebackground="BLUE", activeforeground="WHITE", height=1, command=self.showdeletedstudents, width=15).place(relx=0.25, rely=0.60)
		Button(self.TeacherFrame, font=fontchange, text="Export to CSV", relief=RAISED, padx=10, pady=3, bd=4, activebackground="BLUE", activeforeground="WHITE", height=1, command=self.export_to_csv, width=15).place(relx=0.55,rely=0.60)
		self.TeacherFrame.pack(side=TOP, fill="both", expand=True)

	
	def addstudent(self):
		self.destroy2()
		self.__init__(self.master)
		Label(self.AddStudentFrame, text="Enter student details", font=Font(size=12)).grid(row=2, column=0, columnspan=2)
		subs = ("Roll_No", "PRN_Number", "Name", "AM4", "AM4_Tut", "AOA", "AOA_Lab", "CG", "CG_Lab", "OS", "OS_Lab", "COA", "COA_Lab", "OSTL_Th", "OSTL")
		Label(self.AddStudentFrame, text="* mark means it is compulsory", fg="BLUE").grid(row=0, column=0, columnspan=3)
		Label(self.AddStudentFrame, text="Never start any value with 'zero'", fg="BLUE").grid(row=1, column=0, columnspan=3)
		for i in range(len(self.subs)):
			if self.subs[i] != "Name":
				var = IntVar()
				var.set("")
				Label(self.AddStudentFrame, text=subs[i]).grid(row=i + 3, column=0, stick=W)
				if subs[i] == 'Roll_No' or subs[i] == 'PRN_Number' or subs[i] == 'Name':
					Label(self.AddStudentFrame, text='*', width=1).grid(row=i+3, column=1, stick=W)
				Entry(self.AddStudentFrame, width=25, textvariable=var).grid(row=i+3, column=2, pady=3)
				self.varlist.append(var)
			else:
				var = StringVar()
				Label(self.AddStudentFrame, text=subs[i]).grid(row=i + 3, column=0, stick=W)
				if subs[i] == 'Roll_No' or subs[i] == 'PRN_Number' or subs[i] == 'Name':
					Label(self.AddStudentFrame, text='*', width=1).grid(row=i+3, column=1, stick=W)
				LabeledEntry(self.AddStudentFrame, label="First Name Last Name", width=25, textvariable=var).grid(row=i+3, column=2, pady=3)
				self.varlist.append(var)
		Button(self.AddStudentFrame, text="Save", font=Font(size=14), padx=15, pady=3, bg="BLUE", fg="WHITE", command=self.fetchdata).grid(row=i+5, column=1, columnspan=3, pady=10)
		self.AddStudentFrame.pack(side=TOP, fill="both", expand=True, padx=350, pady=30)
	
	
	def fetchdata(self):
		self.data = []
		for i in range(len(self.varlist)):
			try:
				self.data.append(self.varlist[i].get())
			except:
				self.data.append(0)
				
		try:
			if self.data[0] == 0 or self.data[1] == 0 or self.data[2] == '':
				messagebox.showwarning("Insufficient data", "Data entered by you is not sufficient", icon="warning")
			else:
				sql = "INSERT INTO attendance(Roll_No, PRN_Number, Name, Am4, AM4_Tutorial, AOA, AOA_Practical, CG, CG_Practical, OS, OS_Practical, COA, COA_Practical, OSTL, OSTL_Practical, IsDeleted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0)"
				self.mycursor.execute(sql, self.data)
				self.database.commit()
				messagebox.showinfo("Congo", "Student successfully added")
				self.destroy2()
				self.__init__(self.master)
				self.teachercall()
		except mysql.connector.errors.IntegrityError:
			messagebox.showerror("Duplicate Entry", "Please enter valid details")
		except mysql.connector.errors.ProgrammingError:
			pass
		except:
			messagebox.showwarning("Insufficient data", "Data entered by you is not sufficient", icon="warning")
			
	
	def markattendance(self):
		self.destroy2()
		self.__init__(self.master)
		
		self.mycursor.execute("DESCRIBE attendance")
		self.AllColumnNames = self.mycursor.fetchall()
		for i in range(len(self.AllColumnNames) - 1):
			if i in range(3):
				continue
			else:
				self.columnnames.append(self.AllColumnNames[i][0])
		Label(self.MarkAttendanceFrame, text="Choose Subject to Mark Attendance :").pack()
		class_dropdown = Combobox(self.MarkAttendanceFrame, values=self.columnnames, textvariable=self.columnvariable)
		class_dropdown.current(0)
		class_dropdown.state(['readonly'])
		class_dropdown.bind("<FocusIn>", self.defocus)
		class_dropdown.pack()
		Button(self.MarkAttendanceFrame, text="Sumbit", padx=10, pady=2, relief=RAISED, fg="BLACK", activebackground="GREEN", activeforeground="WHITE", command=self.markattendance2).pack()
		self.MarkAttendanceFrame.pack()
	
	
	def markattendance2(self):
		self.canvas.pack(side=LEFT, fill="both", expand=True, padx=10, pady=10)
		self.MarkAttendanceFrame2 = Frame(self.canvas, background = 'turquoise1')
		self.scrollbary = Scrollbar(self.master, orient=VERTICAL, command=self.canvas.yview)
		self.scrollbary.pack(side=RIGHT, fill=Y)
		self.canvas.configure(yscrollcommand=self.scrollbary.set)
		self.canvas.bind('<Configure>', self.on_configure)
		self.canvas.create_window((0, 0), window=self.MarkAttendanceFrame2, anchor='nw')
		i=0
		for i in range(len(self.alldata)):
			if self.alldata[i][15] != 1:
				var = IntVar()
				Label(self.MarkAttendanceFrame2, text=self.alldata[i][0], width=6).grid(row=i, column=0)
				Label(self.MarkAttendanceFrame2, text=self.alldata[i][1], width=12).grid(row=i, column=1)
				Label(self.MarkAttendanceFrame2, text=self.alldata[i][2], width=30).grid(row=i, column=2, stick=W)
				Checkbutton(self.MarkAttendanceFrame2, text="Tick if Present", variable=var, offvalue=0,
				            onvalue=1).grid(row=i, column=7)
				self.check.append(var)
		if i!=0:
			Button(self.MarkAttendanceFrame2, text="Save Attendance", bg="ORANGE", fg="YELLOW", command=self.getattendancemarked).grid(row=i+1, column=2, padx=10, pady=20)
		else:
			messagebox.showerror("Error", "No student found")
			self.destroy2()
			self.scrollbary.destroy()
			self.__init__(self.master)
			self.teachercall()
		self.MarkAttendanceFrame2.pack(side=TOP)
	
	
	def getattendancemarked(self):
		count = 2
		for n in self.columnnames:
			count += 1
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
				j = 0
				for i in self.alldata[i]:
					if j != count:
						data.append(i)
					else:
						data.append(new)
					j += 1
				sql = ("DELETE FROM attendance WHERE Roll_No=%s")
				key = (roll,)
				self.mycursor.execute(sql, key)
				sql2 = "INSERT INTO attendance(Roll_No, PRN_Number, Name, Am4, AM4_Tutorial, AOA, AOA_Practical, CG, CG_Practical, OS, OS_Practical, COA, COA_Practical, OSTL, OSTL_Practical, IsDeleted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0)"
				key2 = (
				data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10],
				data[11], data[12], data[13], data[14],)
				self.mycursor.execute(sql2, key2, )
		a = messagebox.askyesno("Confirm", ("Attendance for ", x))
		if (a == True):
			self.database.commit()
			try:
				self.destroy2()
				self.scrollbary.destroy()
				self.teachercall()
			except:
				self.destroy2()
				self.scrollbarx.destroy()
				self.scrollbary.destroy()
				self.teachercall()
		elif (a == False):
			messagebox.showinfo("Not saved", "Attendance not updated")
			try:
				self.destroy2()
				self.scrollbary.destroy()
				self.teachercall()
			except:
				self.destroy2()
				self.scrollbarx.destroy()
				self.scrollbary.destroy()
				self.teachercall()

	
	def checkattendance(self):
		self.destroy2()
		self.__init__(self.master)
		
		if(len(self.alldata)==0):
			messagebox.showerror("Error", "NO student found")
			self.destroy2()
			self.__init__(self.master)
			self.teachercall()
		else:
			self.MarkAttendanceFrame2 = Frame(self.canvas, background = 'turquoise1')
			self.canvas.pack(side=LEFT, fill="both", expand=True, padx=10, pady=10)
			self.scrollbary = Scrollbar(self.master, orient=VERTICAL, command=self.canvas.yview)
			self.scrollbary.pack(side=RIGHT, fill=Y)
			self.scrollbarx = Scrollbar(self.master, orient=HORIZONTAL, command=self.canvas.xview)
			self.scrollbarx.pack(side=BOTTOM, fill=X)
			self.canvas.configure(xscrollcommand=self.scrollbarx.set, yscrollcommand=self.scrollbary.set)
			self.canvas.bind('<Configure>', self.on_configure)
			self.CheckAttendanceFrame = Frame(self.canvas, background = 'turquoise1')
			self.canvas.create_window((0, 0), window=self.CheckAttendanceFrame, anchor="nw")
			# self.mycursor.execute("SELECT * FROM attendance")
			# self.result = self.mycursor.fetchall()
			size = range(1, 50, 2)
			Separator(self.CheckAttendanceFrame, orient=HORIZONTAL).grid(row=0, column=0, columnspan=50, sticky='ew')
			for i in range(len(self.subs)):
				if self.subs[i] == "Name":
					Label(self.CheckAttendanceFrame, text=self.subs[i], width=25).grid(row=1, column=size[i], stick=W)
				elif self.subs[i] == "PRN_Number":
					Label(self.CheckAttendanceFrame, text=self.subs[i], width=10).grid(row=1, column=size[i], stick=W)
				else:
					Label(self.CheckAttendanceFrame, text=self.subs[i], width=7).grid(row=1, column=size[i], stick=W)
				Separator(self.CheckAttendanceFrame, orient=VERTICAL).grid(row=1, column=size[i] - 1, sticky='ns')
			self.total = Label(self.CheckAttendanceFrame, text="Total", width=7, font=Font(size=12), fg="GREEN").grid(row=1, column= size[i]+2, stick=W)
			Separator(self.CheckAttendanceFrame, orient=VERTICAL).grid(row=1, column=size[i] + 1, sticky='ns')
			Separator(self.CheckAttendanceFrame, orient=VERTICAL).grid(row=1, column=size[i] + 3, sticky='ns')
			Separator(self.CheckAttendanceFrame, orient=HORIZONTAL).grid(row=2, column=0, columnspan=50, sticky='ew')
			
			for i in range(len(self.alldata)):
				if self.alldata[i][len(self.subs)] == 1:
					continue
				for j in range(len(self.subs)):
					Label(self.CheckAttendanceFrame, text=self.alldata[i][j]).grid(row=i + 5, column=size[j], stick=E)
					Separator(self.CheckAttendanceFrame, orient=VERTICAL).grid(row=i + 5, column=size[j] - 1, sticky='ns')
				Separator(self.CheckAttendanceFrame, orient=VERTICAL).grid(row=i + 5, column=size[j] + 1, sticky='ns')
				self.total = self.alldata[i][3] + self.alldata[i][4] + self.alldata[i][5] + self.alldata[i][6] + \
				             self.alldata[i][7] + self.alldata[i][8] + self.alldata[i][9] + self.alldata[i][10] + \
				             self.alldata[i][11] + self.alldata[i][12] + self.alldata[i][13] + self.alldata[i][14]
				Label(self.CheckAttendanceFrame, text=self.total, font=Font(size=12), fg="GREEN").grid(row=i + 5, column=size[j]+2, stick=E)
				Separator(self.CheckAttendanceFrame, orient=VERTICAL).grid(row=i + 5, column=size[j] + 3, sticky='ns')
			Separator(self.CheckAttendanceFrame, orient=HORIZONTAL).grid(row=i + 6, column=0, columnspan=50, sticky='ew')

	
	def on_configure(self, event):
		self.canvas.configure(scrollregion=self.canvas.bbox('all'))


	def defocus(self, event):
		event.widget.master.focus_set()

	
	def deletestudent(self):
		self.destroy2()
		self.__init__(self.master)
		self.DeleteStudentFrame = Toplevel(background = 'turquoise1')
		self.DeleteStudentFrame.geometry("200x200+600+200")
		self.DeleteStudentFrame.resizable(0, 0)
		self.mycursor.execute("SELECT Roll_No, Name, IsDeleted FROM attendance")
		self.rollandname2 = self.mycursor.fetchall()
		if len(self.rollandname2)==0:
			messagebox.showerror("Error", "No student available")
			self.destroy2()
			self.__init__(self.master)
			self.teachercall()
			
		self.rollandname = []
		for i in self.rollandname2:
			if i[2] == 1:
				continue
			else:
				self.rollandname.append(i[0:2])
		
		self.rollandname_dropdown = Combobox(self.DeleteStudentFrame, values = self.rollandname, textvariable = self.rollname, width = 20)
		self.rollandname_dropdown.current(0)
		self.rollandname_dropdown.state(['readonly'])
		self.rollandname_dropdown.bind("<FocusIn>", self.defocus)
		self.rollandname_dropdown.place(x = 30, y = 50)
		Button(self.DeleteStudentFrame, text = "Delete", bg = "ORANGE", fg = "YELLOW", command = self.finaldelete, padx = 15, pady = 5).place(x = 55, y = 100)
	
	
	def finaldelete(self):
		self.data = self.rollname.get()
		ans = messagebox.askyesno("Delete", "Are yu sure to delete : "+self.data, icon = "warning")
		try:
			if ans:
				sql = "UPDATE attendance SET IsDeleted=1 where Roll_No=%s"
				key = (self.data[0]+self.data[1], )
				self.mycursor.execute(sql, key)
				self.database.commit()
				messagebox.showinfo("Congo", "Deleted successfully : "+self.data)
				self.destroy2()
				self.teachercall()
		except:
			print("Delete")
		self.destroy2()
		self.__init__(self.master)
		self.teachercall()


	def showdeletedstudents(self):
		self.destroy2()
		self.__init__(self.master)
		list = []
		for i in range(len(self.alldata2)):
			if self.alldata2[i][len(self.subs)] == 1:
				list.append(self.alldata2[i])
		if len(list) == 0:
			messagebox.showerror("Error", "Recycle bin is empty")
			self.destroy2()
			self.__init__(self.master)
			self.teachercall()
		else:
			size = range(1, 50, 2)
			Separator(self.ShowDeletedStudentsFrame, orient=HORIZONTAL).grid(row=0, column=0, columnspan=50, sticky='ew')
			for i in range(len(self.subs)):
				if self.subs[i] == "Name":
					Label(self.ShowDeletedStudentsFrame, text=self.subs[i], width=20).grid(row=1, column=size[i], stick=W)
				elif self.subs[i] == "PRN_Number":
					Label(self.ShowDeletedStudentsFrame, text=self.subs[i], width=10).grid(row=1, column=size[i], stick=W)
				else:
					Label(self.ShowDeletedStudentsFrame, text=self.subs[i], width=6).grid(row=1, column=size[i], stick=W)
				Separator(self.ShowDeletedStudentsFrame, orient=VERTICAL).grid(row=1, column=size[i] - 1, sticky='ns')
			self.total = Label(self.ShowDeletedStudentsFrame, text="Total", width=7, font=Font(size=12), fg="GREEN").grid(row=1, column=size[i] + 2, stick=W)
			Separator(self.ShowDeletedStudentsFrame, orient=VERTICAL).grid(row=1, column=size[i] + 1, sticky='ns')
			Separator(self.ShowDeletedStudentsFrame, orient=VERTICAL).grid(row=1, column=size[i] + 3, sticky='ns')
			Separator(self.ShowDeletedStudentsFrame, orient=HORIZONTAL).grid(row=2, column=0, columnspan=50, sticky='ew')
			
			for i in range(len(list)):
				for j in range(len(self.subs)):
					Label(self.ShowDeletedStudentsFrame, text=list[i][j]).grid(row=i + 5, column=size[j], stick=E)
					Separator(self.ShowDeletedStudentsFrame, orient=VERTICAL).grid(row=i + 5, column=size[j] - 1, sticky='ns')
				Separator(self.ShowDeletedStudentsFrame, orient=VERTICAL).grid(row=i + 5, column=size[j] + 1, sticky='ns')
				self.total = list[i][3] + list[i][4] + list[i][5] + list[i][6] + list[i][7] + list[i][8] + list[i][9] + \
				             list[i][10] + list[i][11] + list[i][12] + list[i][13] + list[i][14]
				Label(self.ShowDeletedStudentsFrame, text=self.total, font=Font(size=12), fg="GREEN").grid(row=i+5, column=size[j]+2, stick=E)
				Separator(self.ShowDeletedStudentsFrame, orient=VERTICAL).grid(row=i + 5, column=size[j] + 3, sticky='ns')
			Separator(self.ShowDeletedStudentsFrame, orient=HORIZONTAL).grid(row=i + 6, column=0, columnspan=50, sticky='ew')
			self.ShowDeletedStudentsFrame.pack(side=TOP, fill="both", expand=True)
	
	
	def export_to_csv(self):
		self.mycursor.execute("SELECT * FROM attendance")
		result = self.mycursor.fetchall()
		total = simpledialog.askinteger("Export", "Enter total number of lectures")
		location = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=(("CSV Files", ".csv"), ("All files", "*.*")))
		try:
			c = csv.writer(open(location, 'w', newline=""), lineterminator="\n")
			columns = ['Roll_No', 'PRN_Number', 'Name', 'AM4', 'AM4_Tutorial', 'AOA', 'AOA_Practical', 'CG',
			           'CG_Practical', 'OS', 'OS_Practical', 'COA', 'COA_Practical', 'OSTL', 'OSTL_Practical',
			           'Percentage']
			c.writerow(columns)
			count = 0
			for x in result:
				totatt = 0
				for i in range(3, 15):
					totatt = totatt + result[count][i]
				if x[len(x) - 1] == 0:
					write = x[0:(len(x) - 1)]
					write1 = list(write)
					write2 = (totatt / total * 100)
					write1.append(write2)
					c.writerow(write1)
				count += 1
		except FileNotFoundError:
			messagebox.showerror("Bad directory", "You may not have choosen any directory or wrong directory",
			                     icon="warning")
	
	
	def destroy2(self):
		self.TeacherFrame.destroy()
		self.AddStudentFrame.destroy()
		self.MarkAttendanceFrame.destroy()
		try:
			self.MarkAttendanceFrame2.destroy()
		except:
			pass
		try:
			self.DeleteStudentFrame.destroy()
		except:
			pass
		self.ShowDeletedStudentsFrame.destroy()
		self.canvas.destroy()