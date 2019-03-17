from tkinter import *
from tkinter.font import Font
from tkinter.ttk import Combobox
from tkinter.ttk import Separator
import mysql.connector

root = Tk()
root.title("Attendance Management System")
# root.iconbitmap("cap.ico")

mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
MainFrame = Frame(root)
StudentFrame = Frame(root)
DisplayStudentFrame = Frame(root)
TeacherFrame = Frame(root)
AddStudentFrame = Frame(root)
MarkAttendanceFrame = Frame(root)
canvas = Canvas(root)
check = []
columnnames = []
column_variable = StringVar()

# mycursor.execute("SELECT Roll_No, PRN_Number, Name FROM attendance")
# list = mycursor.fetchall()

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM attendance")
data = mycursor.fetchall()


def subget():
    sub = column_variable.get()
    return sub


def getattendancemarked():
    print(columnnames)
    print("Data:-", data)
    mycursor.execute("DESCRIBE attendance")
    AllColumnNames = mycursor.fetchall()

    for i in range(len(columnnames)):
        if columnnames[i] == subget():
            columnnumber = i
            break

    attend=[]
    for i in range(len(check)):
        attend.append( check[i].get() )

    print("attend",attend)
    attend=tuple(attend)
    print("attend",attend)

    for i in range(len(attend)):
        if attend == 1:
            j = i + 3
            print("j=", j)
            sql = "UPDATE attendance SET %s=%s+1 WHERE Roll_No=data[j][0]"
            key=(subget(),AllColumnNames[j], )
            mycursor.execute(sql, key)
            mydb.commit()
    mycursor.execute("SELECT * FROM attendance")
    dbms = mycursor.fetchall()
    print(dbms)


def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))


def markattendance2():
    canvas.pack(side=LEFT, fill="both", expand=True, padx=10, pady=10)
    scrollbary = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    canvas.configure(yscrollcommand=scrollbary.set)
    canvas.bind('<Configure>', on_configure)
    MarkAttendanceFrame2 = Frame(canvas)
    canvas.create_window((0, 0), window=MarkAttendanceFrame2, anchor='nw')
    for i in range(len(data)):
        var = IntVar()
        check.append(var)
        Label(MarkAttendanceFrame2, text=data[i][0], width=6).grid(row=i, column=0)
        Label(MarkAttendanceFrame2, text=data[i][1], width=12).grid(row=i, column=1)
        Label(MarkAttendanceFrame2, text=data[i][2], width=30).grid(row=i, column=2, stick=W)
        Checkbutton(MarkAttendanceFrame2, text="Tick if Present", variable=check[i],
                    offvalue=0, onvalue=1).grid(row=i, column=7)
    Button(MarkAttendanceFrame2, text="Save Attendance", bg="ORANGE", fg="YELLOW",
           command=getattendancemarked).grid(row=i + 1, column=2, padx=10, pady=20)
    MarkAttendanceFrame2.pack(side=TOP)


def markattendance():
    TeacherFrame.destroy()
    mycursor = mydb.cursor()
    mycursor.execute("DESCRIBE attendance")
    AllColumnNames = mycursor.fetchall()
    for i in range(len(AllColumnNames)):
        if i in range(3):
            continue
        else:
            columnnames.append(AllColumnNames[i][0])
    sublabel = Label(MarkAttendanceFrame, text="Choose Subject to Mark Attendance :").pack()
    class_dropdown = Combobox(MarkAttendanceFrame, values=columnnames, textvariable=column_variable)
    class_dropdown.current(0)
    class_dropdown.pack()
    Button(MarkAttendanceFrame, text="Sumbit", padx=10, pady=2, relief=RAISED, fg="BLACK",
           activebackground="GREEN", activeforeground="WHITE", command=markattendance2).pack()
    MarkAttendanceFrame.pack()


def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))


def checkattendance():
    TeacherFrame.destroy()

    canvas.pack(side=LEFT, fill="both", expand=True, padx=10, pady=10)
    scrollbary = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
    scrollbary.pack(side=RIGHT, fill=Y)

    scrollbarx = Scrollbar(root, orient=HORIZONTAL, command=canvas.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    canvas.configure(xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
    canvas.bind('<Configure>', on_configure)
    CheckAttendanceFrame = Frame(canvas)
    canvas.create_window((0, 0), window=CheckAttendanceFrame, anchor='nw')

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
    m4_label = Label(CheckAttendanceFrame, text="AM4", width=6).grid(row=0, column=6, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=7, sticky='ns')
    m4t_label = Label(CheckAttendanceFrame, text="AM4 Tut", width=6).grid(row=0, column=8, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=9, sticky='ns')
    aoa_label = Label(CheckAttendanceFrame, text="AOA", width=6).grid(row=0, column=10, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=11, sticky='ns')
    aoal_label = Label(CheckAttendanceFrame, text="AOA Lab", width=6).grid(row=0, column=12, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=13, sticky='ns')
    cg_label = Label(CheckAttendanceFrame, text="CG", width=6).grid(row=0, column=14, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=15, sticky='ns')
    cgl_label = Label(CheckAttendanceFrame, text="CG LAb", width=6).grid(row=0, column=16, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=17, sticky='ns')
    os_label = Label(CheckAttendanceFrame, text="OS", width=6).grid(row=0, column=18, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=19, sticky='ns')
    osl_label = Label(CheckAttendanceFrame, text="OS Lab", width=6).grid(row=0, column=20, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=21, sticky='ns')
    coa_label = Label(CheckAttendanceFrame, text="COA", width=6).grid(row=0, column=22, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=23, sticky='ns')
    coal_label = Label(CheckAttendanceFrame, text="COA Lab", width=6).grid(row=0, column=24, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=25, sticky='ns')
    ostl_label = Label(CheckAttendanceFrame, text="OSTL Th", width=6).grid(row=0, column=26, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=27, sticky='ns')
    osltll_label = Label(CheckAttendanceFrame, text="OSTL", width=6).grid(row=0, column=28, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=29, sticky='ns')
    osltll_label = Label(CheckAttendanceFrame, text="Total", width=6).grid(row=0, column=30, stick=W)
    Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=0, column=31, sticky='ns')
    print(len(result))

    for i in range(len(result)):
        rn_label = Label(CheckAttendanceFrame, text=result[i][0], width=5).grid(row=i + 1, column=0, stick=W)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i + 1, column=1, sticky='ns')
        prn_label = Label(CheckAttendanceFrame, text=result[i][1], width=10).grid(row=i + 1, column=2, stick=W)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i + 1, column=3, sticky='ns')
        name_label = Label(CheckAttendanceFrame, text=result[i][2], width=20).grid(row=i + 1, column=4, stick=W)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i + 1, column=5, sticky='ns')
        m4_label = Label(CheckAttendanceFrame, text=result[i][3], width=6).grid(row=i + 1, column=6, stick=W)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i + 1, column=7, sticky='ns')
        m4t_label = Label(CheckAttendanceFrame, text=result[i][4], width=6).grid(row=i + 1, column=8, stick=W)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i + 1, column=9, sticky='ns')
        aoa_label = Label(CheckAttendanceFrame, text=result[i][5], width=6).grid(row=i + 1, column=10, stick=W)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i + 1, column=11, sticky='ns')
        aoal_label = Label(CheckAttendanceFrame, text=result[i][6], width=6).grid(row=i + 1, column=12, stick=W)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i + 1, column=13, sticky='ns')
        cg_label = Label(CheckAttendanceFrame, text=result[i][7], width=6).grid(row=i + 1, column=14, stick=W)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i + 1, column=15, sticky='ns')
        cgl_label = Label(CheckAttendanceFrame, text=result[i][8], width=6).grid(row=i + 1, column=16, stick=W)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i + 1, column=17, sticky='ns')
        os_label = Label(CheckAttendanceFrame, text=result[i][9], width=6).grid(row=i + 1, column=18, stick=W)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i + 1, column=19, sticky='ns')
        osl_label = Label(CheckAttendanceFrame, text=result[i][10], width=6).grid(row=i + 1, column=20, stick=W)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i + 1, column=21, sticky='ns')
        coa_label = Label(CheckAttendanceFrame, text=result[i][11], width=6).grid(row=i + 1, column=22, stick=W)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i + 1, column=23, sticky='ns')
        coal_label = Label(CheckAttendanceFrame, text=result[i][12], width=6).grid(row=i + 1, column=24, stick=W)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i + 1, column=25, sticky='ns')
        ostl_label = Label(CheckAttendanceFrame, text=result[i][13], width=6).grid(row=i + 1, column=26, stick=W)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i + 1, column=27, sticky='ns')
        osltll_label = Label(CheckAttendanceFrame, text=result[i][14], width=6).grid(row=i + 1, column=28, stick=W)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i + 1, column=29, sticky='ns')
        total = result[i][3] + result[i][4] + result[i][5] + result[i][6] + result[i][7] + result[i][8] + \
                result[i][9] + result[i][10] + result[i][11] + result[i][12] + result[i][13] + result[i][14]
        osltll_label = Label(CheckAttendanceFrame, text=total, width=6).grid(row=i + 1, column=30, stick=W)
        Separator(CheckAttendanceFrame, orient=VERTICAL).grid(row=i + 1, column=31, sticky='ns')


rn = IntVar()
prn = IntVar()
name = StringVar()
m4 = IntVar()
m4t = IntVar()
aoa = IntVar()
aoal = IntVar()
cg = IntVar()
cgl = IntVar()
os = IntVar()
osl = IntVar()
coa = IntVar()
coal = IntVar()
ostl = IntVar()
ostll = IntVar()


def fetchstudentdata():
    z = rn.get()
    a = prn.get()
    b = name.get()
    c = m4.get()
    d = m4t.get()
    e = aoa.get()
    f = aoal.get()
    g = cg.get()
    h = cgl.get()
    i = os.get()
    j = osl.get()
    k = coa.get()
    l = coal.get()
    m = ostl.get()
    n = ostll.get()
    values = []
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
    mysqlvalues = tuple(values)
    mycursor = mydb.cursor()
    sql = "INSERT INTO attendance(Roll_No, PRN_Number, Name, Am4, AM4_Tutorial, AOA, AOA_Practical, CG, CG_Practical, OS, OS_Practical, COA, COA_Practical, OSTL, OSTL_Practical) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, mysqlvalues)
    mydb.commit()
    print("Student added successfully : ", mysqlvalues)


def addstudent():
    TeacherFrame.destroy()
    label = Label(AddStudentFrame, text="Enter student details", font=Font(size=12)).grid(row=0, column=0, columnspan=2)
    rn_label = Label(AddStudentFrame, text="Roll No.").grid(row=1, column=0, stick=W)
    prn_label = Label(AddStudentFrame, text="PRN").grid(row=2, column=0, stick=W)
    name_label = Label(AddStudentFrame, text="Name").grid(row=3, column=0, stick=W)
    note_label = Label(AddStudentFrame, text="Enter Previous attendance if any", font=Font(size=12)).grid(row=4,
                                                                                                          column=0)
    m4_label = Label(AddStudentFrame, text="AM4").grid(row=5, column=0, stick=W)
    m4t_label = Label(AddStudentFrame, text="AM4 Tutorial").grid(row=6, column=0, stick=W)
    aoa_label = Label(AddStudentFrame, text="AOA").grid(row=7, column=0, stick=W)
    aoal_label = Label(AddStudentFrame, text="AOA Lab").grid(row=8, column=0, stick=W)
    cg_label = Label(AddStudentFrame, text="CG").grid(row=9, column=0, stick=W)
    cgl_label = Label(AddStudentFrame, text="CG LAb").grid(row=10, column=0, stick=W)
    os_label = Label(AddStudentFrame, text="OS").grid(row=11, column=0, stick=W)
    osl_label = Label(AddStudentFrame, text="OS Lab").grid(row=12, column=0, stick=W)
    coa_label = Label(AddStudentFrame, text="COA").grid(row=13, column=0, stick=W)
    coal_label = Label(AddStudentFrame, text="COA Lab").grid(row=14, column=0, stick=W)
    ostl_label = Label(AddStudentFrame, text="OSTL Theory").grid(row=15, column=0, stick=W)
    osltll_label = Label(AddStudentFrame, text="OSTL").grid(row=16, column=0, stick=W)

    rn_entry = Entry(AddStudentFrame, width=20, textvariable=rn).grid(row=1, column=1)
    prn_entry = Entry(AddStudentFrame, width=20, textvariable=prn).grid(row=2, column=1)
    name_entry = Entry(AddStudentFrame, width=20, textvariable=name).grid(row=3, column=1)
    m4_entry = Entry(AddStudentFrame, width=20, textvariable=m4).grid(row=5, column=1)
    m4t_entry = Entry(AddStudentFrame, width=20, textvariable=m4t).grid(row=6, column=1)
    aoa_entry = Entry(AddStudentFrame, width=20, textvariable=aoa).grid(row=7, column=1)
    aoal_entry = Entry(AddStudentFrame, width=20, textvariable=aoal).grid(row=8, column=1)
    cg_entry = Entry(AddStudentFrame, width=20, textvariable=cg).grid(row=9, column=1)
    cgl_entry = Entry(AddStudentFrame, width=20, textvariable=cgl).grid(row=10, column=1)
    os_entry = Entry(AddStudentFrame, width=20, textvariable=os).grid(row=11, column=1)
    osl_entry = Entry(AddStudentFrame, width=20, textvariable=osl).grid(row=12, column=1)
    coa_entry = Entry(AddStudentFrame, width=20, textvariable=coa).grid(row=13, column=1)
    coal_entry = Entry(AddStudentFrame, width=20, textvariable=coal).grid(row=14, column=1)
    ostl_entry = Entry(AddStudentFrame, width=20, textvariable=ostl).grid(row=15, column=1)
    ostll_entry = Entry(AddStudentFrame, width=20, textvariable=ostll).grid(row=16, column=1)
    Submit_Button = Button(AddStudentFrame, text="Save", font=Font(size=12), padx=10, pady=2, bg="BLUE",
                           fg="WHITE", command=fetchstudentdata)
    Submit_Button.grid(row=18, column=0, columnspan=2)
    AddStudentFrame.pack(side=TOP, fill="both", expand=True)


def teachercall():
    MainFrame.destroy()
    fontchange = Font(family="Courier", size=12)
    Button(TeacherFrame, font=fontchange, text="Add Student", relief=RAISED, padx=10, pady=3, bg="YELLOW", fg="RED",
           bd=2, activebackground="BLUE", activeforeground="WHITE", height=1, command=addstudent).pack()
    # Button(TeacherFrame, font=fontchange, text="Add Student", relief=RAISED, padx=10, pady=3, bg="YELLOW", fg="RED",
    #       bd=2, activebackground="BLUE", activeforeground="WHITE", height=1, command=deletestudent).pack()
    Button(TeacherFrame, font=fontchange, text="Mark Attendance", relief=RAISED, padx=10, pady=3, bg="YELLOW",
           fg="RED", bd=2, activebackground="BLUE", activeforeground="WHITE", height=1, command=markattendance).pack()
    Button(TeacherFrame, font=fontchange, text="Check Attendace", relief=RAISED, padx=10, pady=3, bg="YELLOW",
           fg="RED", bd=2, activebackground="BLUE", activeforeground="WHITE", height=1, command=checkattendance).pack()
    TeacherFrame.pack(side=TOP, fill="both", expand=True)


def displaystudent(details):
    detail = []
    detail = details[0]
    print(detail)

    rn_label = Label(DisplayStudentFrame, text="Roll No.").grid(row=8, column=6, stick=W)
    prn_label = Label(DisplayStudentFrame, text="PRN").grid(row=7, column=6, stick=W)
    name_label = Label(DisplayStudentFrame, text="Name").grid(row=6, column=6, stick=W)
    m4_label = Label(DisplayStudentFrame, text="AM4").grid(row=9, column=6, stick=W)
    m4t_label = Label(DisplayStudentFrame, text="AM4 Tutorial").grid(row=10, column=6, stick=W)
    aoa_label = Label(DisplayStudentFrame, text="AOA").grid(row=11, column=6, stick=W)
    aoal_label = Label(DisplayStudentFrame, text="AOA Lab").grid(row=12, column=6, stick=W)
    cg_label = Label(DisplayStudentFrame, text="CG").grid(row=13, column=6, stick=W)
    cgl_label = Label(DisplayStudentFrame, text="CG LAb").grid(row=14, column=6, stick=W)
    os_label = Label(DisplayStudentFrame, text="OS").grid(row=15, column=6, stick=W)
    osl_label = Label(DisplayStudentFrame, text="OS Lab").grid(row=16, column=6, stick=W)
    coa_label = Label(DisplayStudentFrame, text="COA").grid(row=17, column=6, stick=W)
    coal_label = Label(DisplayStudentFrame, text="COA Lab").grid(row=18, column=6, stick=W)
    ostl_label = Label(DisplayStudentFrame, text="OSTL Theory").grid(row=19, column=6, stick=W)
    osltll_label = Label(DisplayStudentFrame, text="OSTL").grid(row=20, column=6, stick=W)
    osltll_label = Label(DisplayStudentFrame, text="Total", width=20).grid(row=21, column=6, stick=W)

    rn_label2 = Label(DisplayStudentFrame, text=detail[0]).grid(row=8, column=7, stick=E)
    prn_label2 = Label(DisplayStudentFrame, text=detail[1]).grid(row=7, column=7, stick=E)
    name_label2 = Label(DisplayStudentFrame, text=detail[2]).grid(row=6, column=7, stick=E)
    m4_label2 = Label(DisplayStudentFrame, text=detail[3]).grid(row=9, column=7, stick=E)
    m4t_label2 = Label(DisplayStudentFrame, text=detail[4]).grid(row=10, column=7, stick=E)
    aoa_label2 = Label(DisplayStudentFrame, text=detail[5]).grid(row=11, column=7, stick=E)
    aoal_label2 = Label(DisplayStudentFrame, text=detail[6]).grid(row=12, column=7, stick=E)
    cg_label2 = Label(DisplayStudentFrame, text=detail[7]).grid(row=13, column=7, stick=E)
    cgl_label2 = Label(DisplayStudentFrame, text=detail[8]).grid(row=14, column=7, stick=E)
    os_label2 = Label(DisplayStudentFrame, text=detail[9]).grid(row=15, column=7, stick=E)
    osl_label2 = Label(DisplayStudentFrame, text=detail[10]).grid(row=16, column=7, stick=E)
    coa_label2 = Label(DisplayStudentFrame, text=detail[11]).grid(row=17, column=7, stick=E)
    coal_label2 = Label(DisplayStudentFrame, text=detail[12]).grid(row=18, column=7, stick=E)
    ostl_label2 = Label(DisplayStudentFrame, text=detail[13]).grid(row=19, column=7, stick=E)
    osltll_label2 = Label(DisplayStudentFrame, text=detail[14]).grid(row=20, column=7, stick=E)
    total_label2 = Label(DisplayStudentFrame, text=detail[3] + detail[4] + detail[5] + detail[6] + detail[7] +
                                                   detail[8] + detail[9] + detail[10] + detail[11] + detail[12] +
                                                   detail[13] + detail[14], width=25).grid(row=21, column=7, stick=E)
    DisplayStudentFrame.pack(side=TOP, fill="both", expand=True, padx=300)


mycursor = mydb.cursor()
mycursor.execute("select PRN_Number from attendance")
prn_numbers = mycursor.fetchall()
prn_variable = IntVar()


def getprn():
    prnnumber = prn_variable.get()
    return prnnumber


def search_details():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM attendance WHERE PRN_Number='%s'"
    key = (getprn(),)
    mycursor.execute(sql, key)
    details = mycursor.fetchall()
    print(details)
    print(len(details))
    displaystudent(details)


def studentcall():
    MainFrame.destroy()
    fontchange = Font(family="Courier", size=12)
    label = Label(StudentFrame, text="Enter your PRN Number :-", font=fontchange)
    label.place(x=200, y=50)
    prn_dropdown = Combobox(StudentFrame, values=prn_numbers, textvariable=prn_variable)
    prn_dropdown.place(x=450, y=50)
    submit_button = Button(StudentFrame, text="Search", padx=10, pady=2, relief=RAISED, fg="BLACK",
                           activebackground="GREEN", activeforeground="WHITE", command=search_details)
    submit_button.place(x=400, y=100)
    StudentFrame.pack(side=TOP, fill="both", expand=True)


def menubar():
    main_menu = Menu()
    root.config(menu=main_menu)
    file_menu = Menu(main_menu, tearoff=False)
    edit_menu = Menu(main_menu, tearoff=False)
    main_menu.add_cascade(label="File", menu=file_menu)
    main_menu.add_cascade(label="Edit", menu=edit_menu)
    file_menu.add_command(label="Open")
    file_menu.add_command(label="Save")
    file_menu.add_command(label="Save as")
    file_menu.add_separator()
    file_menu.add_command(label="Print")
    file_menu.add_command(label="Exit", command=root.quit)
    edit_menu.add_command(label="Copy")
    edit_menu.add_command(label="Cut")
    edit_menu.add_command(label="Paste")


def start():
    menubar()
    fontchange = Font(family="Courier", size=16)
    label = Label(MainFrame, text="Choose your role", font=fontchange)
    label.place(relx=0.40, rely=0.25)

    StudentRoleButton = Button(MainFrame, font=fontchange, text="Student", relief=RAISED, padx=10, pady=3, bg="YELLOW",
                               fg="RED", bd=2, activebackground="BLUE", activeforeground="WHITE", height=1,
                               command=studentcall)
    TeacherRoleButton = Button(MainFrame, font=fontchange, text="Teacher", relief=RAISED, padx=10, pady=3, bg="YELLOW",
                               fg="RED", bd=2, activebackground="BLUE", activeforeground="WHITE", height=1,
                               command=teachercall)
    StudentRoleButton.place(relx=0.35, rely=0.4)
    TeacherRoleButton.place(relx=0.55, rely=0.4)
    MainFrame.pack(side=TOP, fill="both", expand=True)


start()
root.geometry("960x600+35+22")
root.mainloop()
