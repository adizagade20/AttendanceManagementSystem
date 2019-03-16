from tkinter import *
from tkinter.font import Font
from tkinter.ttk import Combobox
from tkinter.ttk import Separator
import mysql.connector

root = Tk()
root.title("Attendance Management System")
#root.iconbitmap("cap.ico")
#MainFrame = Frame(root, width=1280, height=650)
MainFrame = Frame(root)
#StudentFrame = Frame(root, width=1280, height=650)
StudentFrame = Frame(root)
#DisplayStudentFrame = Frame(root, width=1280, height=650)
DisplayStudentFrame = Frame(root)
#TeacherFrame = Frame(root, width=1280, height=650)
TeacherFrame = Frame(root)
#AddStudentFrame = Frame(root, width=1280, height=650)
AddStudentFrame = Frame(root)
#CheckAttendanceFrame = Frame(root, width=1280, height=650)
CheckAttendanceFrame = Frame(root)





def checkattendance():
    TeacherFrame.destroy()
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM attendance ORDER by Roll_No ASC")
    result = mycursor.fetchall()
    print(result)

    rn_label = Label(CheckAttendanceFrame, text="Roll No.").grid(row=0, column=0, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=1, sticky='ns')
    prn_label = Label(CheckAttendanceFrame, text="PRN", width=10).grid(row=0, column=2, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=3, sticky='ns')
    name_label = Label(CheckAttendanceFrame, text="Name", width=20).grid(row=0, column=4, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=5, sticky='ns')
    m4_label = Label(CheckAttendanceFrame, text="AM4", width=7).grid(row=0, column=6, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=7, sticky='ns')
    m4t_label = Label(CheckAttendanceFrame, text="AM4 Tut", width=7).grid(row=0, column=8, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=9, sticky='ns')
    aoa_label = Label(CheckAttendanceFrame, text="AOA", width=7).grid(row=0, column=10, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=11, sticky='ns')
    aoal_label = Label(CheckAttendanceFrame, text="AOA Lab", width=7).grid(row=0, column=12, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=13, sticky='ns')
    cg_label = Label(CheckAttendanceFrame, text="CG", width=7).grid(row=0, column=14, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=15, sticky='ns')
    cgl_label = Label(CheckAttendanceFrame, text="CG LAb", width=7).grid(row=0, column=16, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=17, sticky='ns')
    os_label = Label(CheckAttendanceFrame, text="OS", width=7).grid(row=0, column=18, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=19, sticky='ns')
    osl_label = Label(CheckAttendanceFrame, text="OS Lab", width=7).grid(row=0, column=20, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=21, sticky='ns')
    coa_label = Label(CheckAttendanceFrame, text="COA", width=7).grid(row=0, column=22, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=23, sticky='ns')
    coal_label = Label(CheckAttendanceFrame, text="COA Lab", width=7).grid(row=0, column=24, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=25, sticky='ns')
    ostl_label = Label(CheckAttendanceFrame, text="OSTL Th", width=7).grid(row=0, column=26, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=27, sticky='ns')
    osltll_label = Label(CheckAttendanceFrame, text="OSTL", width=7).grid(row=0, column=28, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=29, sticky='ns')
    print(len(result))
    i=0
    j=0
    for i in range(len(result)):
        rn_label = Label(CheckAttendanceFrame, text=result[i][0]).grid(row=i+1, column=0, stick=E)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i+1, column=1, sticky='ns')
        prn_label = Label(CheckAttendanceFrame, text=result[i][1]).grid(row=i+1, column=2, stick=E)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i+1, column=3, sticky='ns')
        name_label = Label(CheckAttendanceFrame, text=result[i][2]).grid(row=i+1, column=4, stick=E)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i+1, column=5, sticky='ns')
        m4_label = Label(CheckAttendanceFrame, text=result[i][3]).grid(row=i+1, column=6, stick=E)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i+1, column=7, sticky='ns')
        m4t_label = Label(CheckAttendanceFrame, text=result[i][4]).grid(row=i+1, column=8, stick=E)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i+1, column=9, sticky='ns')
        aoa_label = Label(CheckAttendanceFrame, text=result[i][5]).grid(row=i+1, column=10, stick=E)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i+1, column=11, sticky='ns')
        aoal_label = Label(CheckAttendanceFrame, text=result[i][6]).grid(row=i+1, column=12, stick=E)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i+1, column=13, sticky='ns')
        cg_label = Label(CheckAttendanceFrame, text=result[i][7]).grid(row=i+1, column=14, stick=E)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i+1, column=15, sticky='ns')
        cgl_label = Label(CheckAttendanceFrame, text=result[i][8]).grid(row=i+1, column=16, stick=E)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i+1, column=17, sticky='ns')
        os_label = Label(CheckAttendanceFrame, text=result[i][9]).grid(row=i+1, column=18, stick=E)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i+1, column=19, sticky='ns')
        osl_label = Label(CheckAttendanceFrame, text=result[i][10]).grid(row=i+1, column=20, stick=E)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i+1, column=21, sticky='ns')
        coa_label = Label(CheckAttendanceFrame, text=result[i][11]).grid(row=i+1, column=22, stick=E)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i+1, column=23, sticky='ns')
        coal_label = Label(CheckAttendanceFrame, text=result[i][12]).grid(row=i+1, column=24, stick=E)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i+1, column=25, sticky='ns')
        ostl_label = Label(CheckAttendanceFrame, text=result[i][13]).grid(row=i+1, column=26, stick=E)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i+1, column=27, sticky='ns')
        osltll_label = Label(CheckAttendanceFrame, text=result[i][14]).grid(row=i+1, column=28, stick=E)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i+1, column=29, sticky='ns')
    CheckAttendanceFrame.pack(side=TOP, fill="both", expand=True)


rn=IntVar()
prn=IntVar()
name=StringVar()
m4=IntVar()
m4t=IntVar()
aoa=IntVar()
aoal=IntVar()
cg=IntVar()
cgl=IntVar()
os=IntVar()
osl=IntVar()
coa=IntVar()
coal=IntVar()
ostl=IntVar()
ostll=IntVar()


def fetchstudentdata():
    z=rn.get()
    a= prn.get()
    b=name.get()
    c=m4.get()
    d=m4t.get()
    e=aoa.get()
    f=aoal.get()
    g=cg.get()
    h=cgl.get()
    i=os.get()
    j=osl.get()
    k=coa.get()
    l=coal.get()
    m=ostl.get()
    n=ostll.get()
    values=[]
    values.append(z)
    values.append(a)
    values.append(b)
    values.append(c)
    values.append(d)
    values.append(e)
    values.append(f)
    values.append(g)
    values.append(h)
    values.append(i)
    values.append(j)
    values.append(k)
    values.append(l)
    values.append(m)
    values.append(n)
    mysqlvalues=tuple(values)
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
    mycursor=mydb.cursor()
    sql="INSERT INTO attendance (Roll_No, PRN_Number, Name, Am4, AM4_Tutorial, AOA, AOA_Practical, CG, CG_Practical, OS, OS_Practical, COA, COA_Practical, OSTL, OSTL_Practical) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, mysqlvalues)
    mydb.commit()
    print("Student added successfully : ", mysqlvalues)


def addstudent():
    TeacherFrame.destroy()
    label=Label(AddStudentFrame, text="Enter student details", font=Font(size=12)).grid(row=0, column=0, columnspan=2)
    rn_label=Label(AddStudentFrame, text="Roll No.").grid(row=1, column=0, stick=W)
    prn_label=Label(AddStudentFrame, text="PRN").grid(row=2, column=0, stick=W)
    name_label=Label(AddStudentFrame, text="Name").grid(row=3, column=0, stick=W)
    note_label=Label(AddStudentFrame, text="Enter Previous attendance if any", font=Font(size=12)).grid(row=4, column=0)
    m4_label=Label(AddStudentFrame, text="AM4").grid(row=5, column=0, stick=W)
    m4t_label=Label(AddStudentFrame, text="AM4 Tutorial").grid(row=6, column=0, stick=W)
    aoa_label=Label(AddStudentFrame, text="AOA").grid(row=7, column=0, stick=W)
    aoal_label=Label(AddStudentFrame, text="AOA Lab").grid(row=8, column=0, stick=W)
    cg_label=Label(AddStudentFrame, text="CG").grid(row=9, column=0, stick=W)
    cgl_label=Label(AddStudentFrame, text="CG LAb").grid(row=10, column=0, stick=W)
    os_label=Label(AddStudentFrame, text="OS").grid(row=11, column=0, stick=W)
    osl_label=Label(AddStudentFrame, text="OS Lab").grid(row=12, column=0, stick=W)
    coa_label=Label(AddStudentFrame, text="COA").grid(row=13, column=0, stick=W)
    coal_label=Label(AddStudentFrame, text="COA Lab").grid(row=14, column=0, stick=W)
    ostl_label=Label(AddStudentFrame, text="OSTL Theory").grid(row=15, column=0, stick=W)
    osltll_label=Label(AddStudentFrame, text="OSTL").grid(row=16, column=0, stick=W)

    rn_entry=Entry(AddStudentFrame, width=20, textvariable=rn).grid(row=1, column=1)
    prn_entry=Entry(AddStudentFrame, width=20, textvariable=prn).grid(row=2, column=1)
    name_entry=Entry(AddStudentFrame, width=20, textvariable=name).grid(row=3, column=1)
    m4_entry=Entry(AddStudentFrame, width=20, textvariable=m4).grid(row=5, column=1)
    m4t_entry=Entry(AddStudentFrame, width=20, textvariable=m4t).grid(row=6, column=1)
    aoa_entry=Entry(AddStudentFrame, width=20, textvariable=aoa).grid(row=7, column=1)
    aoal_entry = Entry(AddStudentFrame, width=20, textvariable=aoal).grid(row=8, column=1)
    cg_entry = Entry(AddStudentFrame, width=20, textvariable=cg).grid(row=9, column=1)
    cgl_entry = Entry(AddStudentFrame, width=20, textvariable=cgl).grid(row=10, column=1)
    os_entry = Entry(AddStudentFrame, width=20, textvariable=os).grid(row=11, column=1)
    osl_entry = Entry(AddStudentFrame, width=20, textvariable=osl).grid(row=12, column=1)
    coa_entry = Entry(AddStudentFrame, width=20, textvariable=coa).grid(row=13, column=1)
    coal_entry = Entry(AddStudentFrame, width=20, textvariable=coal).grid(row=14, column=1)
    ostl_entry = Entry(AddStudentFrame, width=20, textvariable=ostl).grid(row=15, column=1)
    ostll_entry = Entry(AddStudentFrame, width=20, textvariable=ostll).grid(row=16, column=1)
    Submit_Button=Button(AddStudentFrame, text="Save", font=Font(size=12), padx=10, pady=2, bg="BLUE",
                         fg="WHITE", command=fetchstudentdata)
    Submit_Button.grid(row=18, column=0, columnspan=2)
    AddStudentFrame.pack(side=TOP, fill="both", expand=True)


def teachercall():
    MainFrame.destroy()
    fontchange = Font(family="Courier", size=12)
    addnewstudent = Button(TeacherFrame, font=fontchange, text="Add Student", relief=RAISED, padx=10, pady=3, bg="YELLOW",
                 fg="RED", bd=2, activebackground="BLUE", activeforeground="WHITE", height=1, command=addstudent).pack()
    marknewattendace = Button(TeacherFrame, font=fontchange, text="Mark Attendance", relief=RAISED, padx=10, pady=3, bg="YELLOW",
                  fg="RED", bd=2, activebackground="BLUE", activeforeground="WHITE", height=1,).pack()
    checkclassattendance = Button(TeacherFrame, font=fontchange, text="Check Attendace", relief=RAISED, padx=10, pady=3,bg="YELLOW",
                   fg="RED", bd=2, activebackground="BLUE", activeforeground="WHITE", height=1, command=checkattendance).pack()
    TeacherFrame.pack(side=TOP, fill="both", expand=True)





def displaystudent(details):
    rn_label = Label(DisplayStudentFrame, text="Roll No.").grid(row=0, column=0, stick=W)
    prn_label = Label(DisplayStudentFrame, text="PRN").grid(row=1, column=0, stick=W)
    name_label = Label(DisplayStudentFrame, text="Name").grid(row=2, column=0, stick=W)
    m4_label = Label(DisplayStudentFrame, text="AM4").grid(row=3, column=0, stick=W)
    m4t_label = Label(DisplayStudentFrame, text="AM4 Tutorial").grid(row=4, column=0, stick=W)
    aoa_label = Label(DisplayStudentFrame, text="AOA").grid(row=5, column=0, stick=W)
    aoal_label = Label(DisplayStudentFrame, text="AOA Lab").grid(row=6, column=0, stick=W)
    cg_label = Label(DisplayStudentFrame, text="CG").grid(row=7, column=0, stick=W)
    cgl_label = Label(DisplayStudentFrame, text="CG LAb").grid(row=8, column=0, stick=W)
    os_label = Label(DisplayStudentFrame, text="OS").grid(row=9, column=0, stick=W)
    osl_label = Label(DisplayStudentFrame, text="OS Lab").grid(row=10, column=0, stick=W)
    coa_label = Label(DisplayStudentFrame, text="COA").grid(row=11, column=0, stick=W)
    coal_label = Label(DisplayStudentFrame, text="COA Lab").grid(row=12, column=0, stick=W)
    ostl_label = Label(DisplayStudentFrame, text="OSTL Theory").grid(row=13, column=0, stick=W)
    osltll_label = Label(DisplayStudentFrame, text="OSTL").grid(row=14, column=0, stick=W)
    detail=[(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)]
    rn_label2 = Label(DisplayStudentFrame, text=detail[0][0]).grid(row=0, column=1, stick=W)
    prn_label2 = Label(DisplayStudentFrame, text=detail[0][1]).grid(row=1, column=1, stick=W)
    name_label2 = Label(DisplayStudentFrame, text=detail[0][2]).grid(row=2, column=1, stick=W)
    m4_label2 = Label(DisplayStudentFrame, text=detail[0][3]).grid(row=3, column=1, stick=W)
    m4t_label2 = Label(DisplayStudentFrame, text=detail[0][4]).grid(row=4, column=1, stick=W)
    aoa_label2 = Label(DisplayStudentFrame, text=detail[0][5]).grid(row=5, column=1, stick=W)
    aoal_label2 = Label(DisplayStudentFrame, text=detail[0][6]).grid(row=6, column=1, stick=W)
    cg_label2 = Label(DisplayStudentFrame, text=detail[0][7]).grid(row=7, column=1, stick=W)
    cgl_label2 = Label(DisplayStudentFrame, text=detail[0][8]).grid(row=8, column=1, stick=W)
    os_label2 = Label(DisplayStudentFrame, text=detail[0][9]).grid(row=9, column=1, stick=W)
    osl_label2 = Label(DisplayStudentFrame, text=detail[0][10]).grid(row=10, column=1, stick=W)
    coa_label2 = Label(DisplayStudentFrame, text=detail[0][11]).grid(row=11, column=1, stick=W)
    coal_label2 = Label(DisplayStudentFrame, text=detail[0][12]).grid(row=12, column=1, stick=W)
    ostl_label2 = Label(DisplayStudentFrame, text=detail[0][13]).grid(row=13, column=1, stick=W)
    osltll_label2 = Label(DisplayStudentFrame, text=detail[0][14]).grid(row=14, column=1, stick=W)
    DisplayStudentFrame.pack(side=TOP, fill="both", expand=True)


mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
mycursor = mydb.cursor()
mycursor.execute("select PRN_Number from attendance")
prn_numbers = mycursor.fetchall()
prn_variable = IntVar()


def search_details(prn_no):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
    mycursor = mydb.cursor()
    sql = "SELECT * FROM attendance WHERE PRN_Number= '%d'"
    key = (prn_no)
    #mycursor.execute(sql, key)
    #print(mycursor.fetchone())
    #details = mycursor.fetchone()
    details=1
    displaystudent(details)


def get_prn():
    #StudentFrame.destroy()
    prn_no = (prn_variable.get())
    print(prn_no)
    search_details(prn_no)


def studentcall():
    MainFrame.destroy()
    fontchange = Font(family="Courier", size=12)
    label = Label(StudentFrame, text="Enter your PRN Number :-", font=fontchange)
    label.place(x=200, y=50)
    prn_dropdown = Combobox(StudentFrame, values=prn_numbers, textvariable=prn_variable)
    prn_dropdown.place(x=450, y=50)
    submit_button = Button(StudentFrame, text="Search", padx=10, pady=2, relief=RAISED, fg="BLACK", activebackground="GREEN", activeforeground="WHITE", command=get_prn)
    submit_button.place(x=350, y=100)
    StudentFrame.pack(side=TOP, fill="both", expand=True)


def start():
    fontchange = Font(family="Courier", size=16)
    label = Label(MainFrame, text="Choose your role", font = fontchange)
    label.place(x=500, y=200)
    StudentRoleButton = Button(MainFrame, font = fontchange, text = "Student", relief = RAISED, padx=10, pady=3, bg = "YELLOW",fg = "RED", bd = 2, activebackground ="BLUE", activeforeground = "WHITE", height = 1, command=studentcall)
    TeacherRoleButton = Button(MainFrame, font = fontchange, text = "Teacher", relief = RAISED, padx=10, pady=3, bg = "YELLOW",fg = "RED", bd = 2, activebackground ="BLUE", activeforeground = "WHITE", height = 1, command=teachercall)
    StudentRoleButton.place(x=400, y=300)
    TeacherRoleButton.place(x=700, y=300)
    MainFrame.pack(side=TOP, fill="both", expand=True)





start()
root.geometry("960x600+35+22")
root.mainloop()