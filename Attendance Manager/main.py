from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("Attendance Management System")
root.iconbitmap("cap.ico")
name = StringVar()

def name_get():
    nameget = name.get()
    print(nameget)

def student_role():
	frame.destroy()
	frame2 = Frame(width=700, height=500)
	fontchange = Font(family="Courier", size=12)
	entry = Label(frame2, text="Enter your Name :-", font=fontchange)
	entry.place(x=50, y=40)
	enter_name = Entry(frame2, textvariable=name, width=30)
	enter_name.place(x=250, y=45)
	submit_button = Button(frame2, text="Search", padx=10, pady=2, relief=RAISED, fg="BLACK", activebackground="GREEN", activeforeground="WHITE", command=name_get)
	submit_button.place(x=250, y=100)
	frame2.pack()

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