from tkinter import *
from tkinter.font import Font
from student import *
from teacher import *

root = Tk()

def student_role():
	student = Student()

def teacher_role():
	teacher = Teacher()


fontchange = Font(family="Helvetica", size=16)
Label(root, text="Choose your role", font = fontchange).place(x=270, y=100)
student = Button(root, font = fontchange, text = "Student", relief = RAISED, padx=10, pady=3, bg = "YELLOW", fg = "RED", bd = 2, activebackground ="BLUE", activeforeground = "WHITE", height = 1, command = student_role)
teacher = Button(root, font = fontchange, text = "Teacher", relief = RAISED, padx=10, pady=3, bg = "YELLOW", fg = "RED", bd = 2, activebackground ="BLUE", activeforeground = "WHITE", height = 1, command = teacher_role)
student.place(x=200, y=200)
teacher.place(x=400, y=200)

root.geometry("700x500+300+100")
root.mainloop()