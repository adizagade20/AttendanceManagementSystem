from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.font import Font
import mysql.connector
from studentfile import StudentRoot
from teacherfile import TeacherRoot
from PIL import Image
from PIL import ImageTk


root = Tk()
root.title("Attendance Management System")
root.configure(background = 'LightPink1')



try:
	database = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
	mycursor = database.cursor()
	root.geometry("1000x600+180+30")
except mysql.connector.errors.InterfaceError:
	root.geometry("100x100+6000+4000")
	Label(root, text="Error!", font=Font(size=18)).pack()
	messagebox.showerror("Error!", "Connection to the Server could not be acquired", icon="error")
	exit()

database = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
mycursor = database.cursor()
mycursor.execute('CREATE TABLE IF NOT EXISTS attendance(Roll_No TINYINT(4),Name VARCHAR(255), PRN_Number INT(11),'
	                 'AM4 TINYINT(4), AM4_Tutorial TINYINT(4),'
	                 'AOA TINYINT(4), AOA_Practical TINYINT(4),'
	                 'CG TINYINT(4), CG_Practical TINYINT(4),'
	                 'OS TINYINT(4), OS_Practical TINYINT(4),'
	                 'COA TINYINT(4), COA_Practical TINYINT(4),'
	                 'OSTL TINYINT(4), OSTL_Practical TINYINT(4), IsDeleted TINYINT(2),'
	                 'UNIQUE (Roll_No, PRN_Number),'
	                 'PRIMARY KEY (Roll_No, PRN_Number) )'
                 )
database.commit()


class StartRoot:
	def __init__(self, root):
		self.master = root
		self.MainFrame = Frame(self.master, background = 'turquoise1')
		database = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
		mycursor = database.cursor()
		self.class1 = StudentRoot(root)
		self.class2 = TeacherRoot(root)
		self.first_page()
		root.bind('<Escape>', self.escape)
		
		try:
			database = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
			mycursor = database.cursor()
		except:
			Label(root, text="Error!", font=Font(size=18)).pack()
			messagebox.showerror("Error!", "Connection to the Server could not be acquired", icon="error")
			exit()


	def first_page(self):
		change_font = Font(family = "Courier", size = 16)
		Label(self.MainFrame, text = "You are as", font = change_font).place(relx=0.43, rely=0.15)
		
		width = 140
		height = 140
		img1 = Image.open("student.png")
		img1 = img1.resize((width, height), Image.ANTIALIAS)
		photoImg = ImageTk.PhotoImage(img1)
		a = Button(self.MainFrame, image = photoImg, command = self.destroymainframe_student, bd = 1)
		a.image = photoImg
		a.place(relx=0.25, rely=0.25)
		Button(self.MainFrame, font = change_font, text = "Student", relief = RAISED, padx = 15, pady = 5, bd = 5, activebackground = "BLUE", activeforeground = "WHITE", height = 1, command = self.destroymainframe_student).place(relx = 0.25, rely = 0.60)
		
		img2 = Image.open("teacher.png")
		img2 = img2.resize((width, height), Image.ANTIALIAS)
		photoImg2 = ImageTk.PhotoImage(img2)
		b = Button(self.MainFrame, image = photoImg2, command = self.destroymainframe_teacher, bd=1)
		b.image = photoImg2
		b.place(relx=0.60, rely=0.25)
		Button(self.MainFrame, font = change_font, text = "Teacher", relief = RAISED, padx = 15, pady = 5, bd = 5, activebackground = "BLUE", activeforeground = "WHITE", height = 1, command = self.destroymainframe_teacher).place(relx = 0.60, rely = 0.60)
		self.MainFrame.pack(side = TOP, fill = "both", expand = True)


	def destroymainframe_student(self):
		self.MainFrame.destroy()
		self.class1.studentcall()


	def destroymainframe_teacher(self):
		self.MainFrame.destroy()
		z = Toplevel()
		z.geometry("220x120+600+200")
		z.resizable(0, 0)
		teacherlist = [0, 1]
		self.c = Combobox(z, values=teacherlist).grid(row=0, column=0)
		self.e = Entry(z).grid(row=1, column=0)
		Button(z, command=self.verify).grid(row=2, column=0)


	def verify(self):
		pass




	def escape(self, event):
		student.MainFrame.destroy()
		self.class1.destroy1()
		self.class2.destroy2()
		try:
			self.class2.scrollbary.destroy()
		except:
			pass
		try:
			self.class2.scrollbary.destroy()
			self.class2.scrollbarx.destroy()
		except:
			pass
		student.__init__(self.master)





class addteacher:
	def __init__(self, root):
		self.master = root
		self.teacherdatabase = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
		self.cursor = database.cursor()
		self.cursor.execute(
			"CREATE TABLE IF NOT EXISTS`teachercredential`(`SrNo` TINYINT(4) NOT NULL, `Name` VARCHAR(255) NULL, `Password` INT(11) NULL, PRIMARY KEY (`SrNo`), UNIQUE INDEX `SrNo_UNIQUE` (`SrNo` ASC) VISIBLE)")
		self.teacherdatabase.commit()
		self.teacherdatabase = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
	
	
	def addteacherfun(self):
		self.addteachertop = Toplevel()
		self.addteachertop.title("Add Teacher")
		self.addteachertop.geometry("220x120+600+200")
		self.addteachertop.resizable(0,0)
		self.cursor.execute("SELECT * FROM teachercredential")
		teach = self.cursor.fetchall()
		self.all = len(teach)
		self.a = StringVar()
		self.b = StringVar()
		self.d = StringVar()
		Label(self.addteachertop, text = "ID :").grid(row=4, column=5)
		Label(self.addteachertop, text = self.all+1).grid(row=4, column=6)
		Label(self.addteachertop, text = "Enter Name :").grid(row=5, column=5)
		Entry(self.addteachertop, textvariable = self.a).grid(row=5, column=6)
		Label(self.addteachertop, text = "Enter Key :").grid(row=6, column=5)
		x = Entry(self.addteachertop, textvariable = self.b).grid(row=6, column=6)
		self.d.set(self.all+1)
		Button(self.addteachertop, text = "Add Teacher", bd = 2, command = self.addteacherfun2).grid(row=7, column=5, columnspan = 2, pady=10)
		Entry(self.addteachertop, textvariable = self.d).place(x=200, y=200)
	
	def addteacherfun2(self):
		idget = self.d.get()
		nameget = self.a.get()
		keyget = self.b.get()
		self.data = []
		self.data.append(idget)
		self.data.append(nameget)
		self.data.append(keyget)
		sql = "INSERT INTO adi.teachercredential(SrNo, Name, Password) VALUES (%s, %s, %s)"
		self.cursor.execute(sql, self.data)
		#datatuple = (self.all+1, nameget, keyget)
		#self.cursor.execute(sql, datatuple)
		#self.cursor.execute("INSERT INTO teachercredential(SrNo, Name, Password) VALUES(self.all+1, nameget, keyget)")
		self.teacherdatabase.commit()
		messagebox.showinfo("Success", "Teacher "+nameget+"added successfully!")
	

	def teacheraddadmin(self):
		self.z = Toplevel()
		self.z.title("Login")
		self.z.geometry("220x120+600+200")
		self.z.resizable(0, 0)
		self.c = StringVar()
		self.e = StringVar()
		Label(self.z, text="User ID :").grid(row=0, column=0)
		Entry(self.z, textvariable = self.c).grid(row=0, column=1)
		Label(self.z, text="Password :").grid(row=1, column=0)
		Entry(self.z, textvariable = self.e).grid(row=1, column=1)
		Button(self.z, text = "login", bd = 2, command = self.verify).grid(row=2, column=0, columnspan=2, pady=10)
	
	def verify(self):
		if self.e.get()=="Admin" and self.c.get()=="Admin":
			self.z.destroy()
			self.addteacherfun()
		elif self.e.get()=="" and self.c.get()=="":
			self.z.destroy()
			self.addteacherfun()
		else:
			messagebox.showerror("Login error", "User ID and Password combination is wrong")
		
		


def menubar():
	a = addteacher(root)
	main_menu = Menu(root)
	root.config(menu = main_menu)
	file_menu = Menu(main_menu, tearoff=False)
	main_menu.add_cascade(label="File", menu=file_menu)
	file_menu.add_command(label="Exit", command=root.quit)
	file_menu.add_command(label="Add Teacher", command=a.teacheraddadmin)
	
	
student = StartRoot(root)
Label(root, text = "Press 'esc' for going back to home from any step").pack(side=BOTTOM)


def on_closing():
	if messagebox.askokcancel("Quit", "Do you want to quit?", icon = "error"):
		root.destroy()

menubar()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.resizable(0,0)
root.mainloop()