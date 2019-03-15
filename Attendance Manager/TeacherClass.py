from tkinter import *
from tkinter.font import Font
from tkinter.ttk import Separator
import mysql.connector

root = Tk()
frame = Frame(root)
mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")


mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM attendance ORDER by Roll_No ASC")
result=mycursor.fetchall()
CheckAttendanceFrame=Frame(root, width=1280, height=650)

def CheckAttendance():
    frame.destroy()
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

    CheckAttendanceFrame.pack()











AddStudentFrame=Frame(root, width=1280, height=650)
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

def FetchStudentData():
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

def AddStudent():
    frame.destroy()
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

    #Separator(AddStudentFrame, orient=VERTICAL).grid(column=2, row=0, rowspan=16, sticky='ns')
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

    Submit_Button=Button(AddStudentFrame, text="Save", font=Font(size=12), padx=10, pady=2, bg="BLUE", fg="WHITE", command=FetchStudentData)
    Submit_Button.grid(row=18, column=0, columnspan=2)
    AddStudentFrame.pack()

def Start(root):
    fontchange = Font(family="Courier", size=12)
    add = Button(frame, font=fontchange, text="Add Student", relief=RAISED, padx=10, pady=3, bg="YELLOW", fg="RED", bd=2, activebackground="BLUE", activeforeground="WHITE", height=1, command=AddStudent).pack()
    mark = Button(frame, font=fontchange, text="Mark Attendance", relief=RAISED, padx=10, pady=3, bg="YELLOW",fg="RED", bd=2, activebackground="BLUE", activeforeground="WHITE", height=1,).pack()
    check = Button(frame, font=fontchange, text="Check attendace of paticular student", relief=RAISED, padx=10,pady=3, bg="YELLOW", fg="RED", bd=2, activebackground="BLUE", activeforeground="WHITE", height=1, command=CheckAttendance).pack()
    check_class = Button(frame, font=fontchange, text="Mark Attendance of whole class", relief=RAISED, padx=10,pady=3, bg="YELLOW", fg="RED", bd=2, activebackground="BLUE", activeforeground="WHITE", height=1).pack()
    frame.pack(side=TOP, fill="both", expand=True)

Start(root)
root.geometry("1280x650+35+22")
root.mainloop()