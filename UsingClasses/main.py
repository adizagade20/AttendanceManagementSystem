from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import mysql.connector
from studentfile import StudentRoot
from teacherfile import TeacherRoot

root = Tk()
root.title("Attendance Management System")

try:
	database = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
	mycursor = database.cursor()
	root.geometry("1000x600+180+30")
except:
	root.geometry("100x100+6000+4000")
	Label(root, text="Error!", font=Font(size=18)).pack()
	messagebox.showerror("Error!", "Connection to the Server could not be acquired", icon="error")
	exit()


class StartRoot:
	def __init__(self, root):
		self.master = root
		self.master.title("Attendance Management System")
		self.master.bind('<Escape>', self.escape)
		self.test = Frame(self.master, width=1000, height=30)
		Button(self.test, text="Home", bd=5, command=self.gotohome).place(x=930, y=0)
		self.test.pack(side=TOP, padx=10, pady=10)
		self.MainFrame = Frame(self.master)
		self.class1 = StudentRoot(root)
		self.class2 = TeacherRoot(root)
		self.first_page()
		self.menubar()
		try:
			database = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
			mycursor = database.cursor()
		except:
			Label(root, text="Error!", font=Font(size=18)).pack()
			messagebox.showerror("Error!", "Connection to the Server could not be acquired", icon="error")
			exit()


	def first_page(self):
		change_font = Font(family = "Courier", size = 16)
		Label(self.MainFrame, text = "Choose your role", font = change_font).place(relx=0.40, rely=0.20)
		Button(self.MainFrame, font = change_font, text = "Student", relief = RAISED, padx = 15, pady = 5, bd = 5, activebackground = "BLUE", activeforeground = "WHITE", height = 1, command = self.destroymainframe_student).place(relx = 0.35, rely = 0.35)
		Button(self.MainFrame, font = change_font, text = "Teacher", relief = RAISED, padx = 15, pady = 5, bd = 5, activebackground = "BLUE", activeforeground = "WHITE", height = 1, command = self.destroymainframe_teacher).place(relx = 0.55, rely = 0.35)
		self.MainFrame.pack(side = TOP, fill = "both", expand = True)


	def destroymainframe_student(self):
		self.MainFrame.destroy()
		self.class1.studentcall()


	def destroymainframe_teacher(self):
		self.MainFrame.destroy()
		self.class2.teachercall()


	def menubar(self):
		self.main_menu = Menu(self.master)
		self.master.config(menu = self.main_menu)
		self.file_menu = Menu(self.main_menu, tearoff = False)
		self.edit_menu = Menu(self.main_menu, tearoff = False)
		self.main_menu.add_cascade(label="File", menu=self.file_menu)
		self.file_menu.add_command(label="Exit", command=self.master.quit)


	def gotohome(self):
		student.test.destroy()
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

	
	def escape(self, event):
		student.test.destroy()
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
		

student = StartRoot(root)


def on_closing():
	if messagebox.askokcancel("Quit", "Do you want to quit?", icon = "error"):
		root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()