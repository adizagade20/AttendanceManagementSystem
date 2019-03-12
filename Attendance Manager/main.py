from tkinter import *
from tkinter.font import Font
from StudentClass import Student_Class

root = Tk()
root.title("Attendance Management System")
root.iconbitmap("cap.ico")
name = StringVar()

def student_role():
	frame.destroy()
	student = Student_Class(root)
	print(student)
def Student_Search():
	name = student.get_name()
	print(student.name_var)




def teacher_role():
	pass







frame = Frame(root, width=700, height=500)
fontchange = Font(family="Courier", size=16)
label = Label(frame, text="Choose your role", font = fontchange)
label.place(x=270, y=100)
student = Button(frame, font = fontchange, text = "Student", relief = RAISED, padx=10, pady=3, bg = "YELLOW", fg = "RED", bd = 2, activebackground ="BLUE", activeforeground = "WHITE", height = 1, command = student_role)
teacher = Button(frame, font = fontchange, text = "Teacher", relief = RAISED, padx=10, pady=3, bg = "YELLOW", fg = "RED", bd = 2, activebackground ="BLUE", activeforeground = "WHITE", height = 1, command = teacher_role)
student.place(x=200, y=200)
teacher.place(x=400, y=200)
frame.pack()

root.geometry("700x500+300+100")
root.mainloop()