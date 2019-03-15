from tkinter import *
from tkinter.font import Font
from Student_role import *
import TeacherClass

root = Tk()
root.title("Attendance Management System")
root.iconbitmap("cap.ico")

def student_role():
	frame.destroy()
	student = Student_Class(root)

def teacher_role():
	frame.destroy()
	TeacherClass.Start(root)

def menubar(root):
	main_menu = Menu()
	root.config(menu = main_menu)
	file_menu = Menu(main_menu, tearoff=False)
	edit_menu = Menu(main_menu, tearoff=False)
	main_menu.add_cascade(label="File", menu=file_menu)
	main_menu.add_cascade(label="Edit", menu=edit_menu)

	file_menu.add_command(label="Open")
	file_menu.add_command(label="Save")
	file_menu.add_command(label="Save as")
	file_menu.add_separator()
	file_menu.add_command(label="Print")
	file_menu.add_command(label="Exit", command = root.quit)

	edit_menu.add_command(label="Copy")
	edit_menu.add_command(label="Cut")
	edit_menu.add_command(label="Paste")


frame = Frame(root, width=700, height=500)
fontchange = Font(family="Courier", size=16)
label = Label(frame, text="Choose your role", font = fontchange)
label.place(x=270, y=100)
student = Button(frame, font = fontchange, text = "Student", relief = RAISED, padx=10, pady=3, bg = "YELLOW", fg = "RED", bd = 2, activebackground ="BLUE", activeforeground = "WHITE", height = 1, command = student_role)
teacher = Button(frame, font = fontchange, text = "Teacher", relief = RAISED, padx=10, pady=3, bg = "YELLOW", fg = "RED", bd = 2, activebackground ="BLUE", activeforeground = "WHITE", height = 1, command = teacher_role)
student.place(x=200, y=200)
teacher.place(x=400, y=200)
frame.pack()
menubar(root)

root.geometry("700x500+300+100")
root.mainloop()