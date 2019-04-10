from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.font import Font
import mysql.connector
from studentfile import StudentRoot
from teacherfile import TeacherRoot
import csv

root = Tk()
root.title("Attendance Management System")

#root.iconbitmap("cap.ico")

try:
	database = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
	mycursor = database.cursor()
except:
	root.geometry("100x100+6000+4000")
	Label(root, text="Error!", font=Font(size=18)).pack()
	messagebox.showerror("Error!", "Connection to the Server could not be acquired", icon="error")
	exit()


class StartRoot:
	def __init__(self, root):
		self.master = root
		self.master.title("Attendance Management System")
		test = Frame(self.master, width=1000, height=30)
		Button(test, text="Home", bd=5, command=self.gotohome).place(x=930, y=0)
		test.pack(side=TOP, padx=10, pady=10)
		self.MainFrame = Frame(self.master)
		root.geometry("1000x600+230+100")
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
		Label(self.MainFrame, text = "Choose your role", font = change_font).place(relx=0.40, rely=0.25)
		Button(self.MainFrame, font = change_font, text = "Student", relief = RAISED, padx = 15, pady = 5,
			   bg = "YELLOW", fg = "RED", bd = 2, activebackground = "BLUE", activeforeground = "WHITE",
			   height = 1, command = self.destroymainframe_student).place(relx = 0.35, rely = 0.4)
		Button(self.MainFrame, font = change_font, text = "Teacher", relief = RAISED, padx = 15, pady = 5,
			   bg = "YELLOW", fg = "RED", bd = 2, activebackground = "BLUE", activeforeground = "WHITE",
			   height = 1, command = self.destroymainframe_teacher).place(relx = 0.55, rely = 0.4)
		self.MainFrame.pack(side = TOP, fill = "both", expand = True)


	def destroymainframe_student(self):
		self.MainFrame.destroy()
		s = StudentRoot(self.master)
		s.studentcall()


	def destroymainframe_teacher(self):
		self.MainFrame.destroy()
		t = TeacherRoot(self.master)
		t.teachercall()


	def menubar(self):
		self.main_menu = Menu(self.master)
		self.master.config(menu = self.main_menu)
		self.file_menu = Menu(self.main_menu, tearoff = False)
		self.edit_menu = Menu(self.main_menu, tearoff = False)
		self.main_menu.add_cascade(label="File", menu=self.file_menu)
		self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)
		#self.file_menu.add_command(label="Open")
		#self.file_menu.add_command(label="Save")
		#self.file_menu.add_command(label="Save as")
		#self.file_menu.add_separator()
		self.file_menu.add_command(label="Export to CSV", command = self.export_to_csv)
		self.file_menu.add_command(label="Exit", command=self.master.quit)
		self.edit_menu.add_command(label="Copy")
		self.edit_menu.add_command(label="Cut")
		self.edit_menu.add_command(label="Paste")


	def export_to_csv(self):
		mycursor.execute("SELECT * FROM attendance")
		result = mycursor.fetchall()
		location = filedialog.asksaveasfilename(defaultextension = ".csv")
		try:
			c = csv.writer(open(location, 'w', newline=""), lineterminator="\n")
			columns = ['Roll_No', 'PRN_Number', 'Name', 'AM4', 'AM4_Tutorial', 'AOA', 'AOA_Practical', 'CG', 'CG_Practical', 'OS', 'OS_Practical', 'COA', 'COA_Practical', 'OSTL', 'OSTL_Practical']
			c.writerow(columns)
			for x in result:
				c.writerow(x)
		except FileNotFoundError:
			messagebox.showerror("Bad directory", "You may not have choosen any directory or wrong directory", icon="warning")

	def gotohome(self):
		self.master.destroy()
		root = Tk()
		student2 = StartRoot(root)


student = StartRoot(root)

def on_closing():
	if messagebox.askokcancel("Quit", "Do you want to quit?", icon = "error"):
		root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()