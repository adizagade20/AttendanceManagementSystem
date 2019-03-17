from tkinter import *
from tkinter.font import *
from tkinter.ttk import Combobox
from tkinter.ttk import Separator
import mysql.connector
root = Tk()

TeacherFrame=Frame(root)
MarkAttendanceFrame = Frame(root)
canvas=Canvas(root)

vars = []
columnnames=[]
column_variable=StringVar()
mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
mycursor = mydb.cursor()
mycursor.execute("SELECT Roll_No, PRN_Number, Name FROM attendance")
list = mycursor.fetchall()


def getmarkattendance():
    sub=column_variable.get()
    print(sub)
    print(columnnames)
    mycursor.execute("SELECT Roll_No FROM attendance")
    roll=mycursor.fetchall()

    sqlquery="SELECT * FROM attendance"
    key=("sub,")
    mycursor.execute(sqlquery, key)
    data=mycursor.fetchall()
    print("Data:-",data)

    for i in range(len(columnnames)):
        if(columnnames[i]==sub):
            print(i)
            break
    for j in range(len(list)):
        attend=0
        attend=vars[j].get()
        print(attend)
        """if (attend==1):
            newdata = data[j][1] + 1
            sql="UPDATE attendance SET %s=newdata WHERE Roll_No=data[j][0]"
            key=(sub,)
            mycursor.execute(sql, sub)"""







def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))


def markattendance2():
    canvas.pack(side=LEFT, fill="both", expand=True, padx=10, pady=10)
    scrollbary = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    canvas.configure(yscrollcommand=scrollbary.set)
    canvas.bind('<Configure>', on_configure)
    MarkAttendanceFrame2=Frame(canvas)
    canvas.create_window((0, 0), window=MarkAttendanceFrame2, anchor='nw')
    print(list)
    for i in range( len(list) ):
        var=IntVar()
        vars.append(var)
        Label(MarkAttendanceFrame2, text=list[i][0], width=6).grid(row=i, column=0)
        Label(MarkAttendanceFrame2, text=list[i][1], width=12).grid(row=i, column=1)
        Label(MarkAttendanceFrame2, text=list[i][2], width=30).grid(row=i, column=2, stick=W)
        Checkbutton(MarkAttendanceFrame2, text="Tick if Present", variable=vars[i],
                    offvalue=0, onvalue=1).grid(row=i, column=7)
    Button(MarkAttendanceFrame2, text="Save Attendance", bg="ORANGE", fg="YELLOW",
           command=getmarkattendance).grid(row=i+1, column=2, padx=10, pady=20)
    MarkAttendanceFrame2.pack(side=TOP)


def markattendance():
    TeacherFrame.destroy()
    mydb=mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
    mycursor=mydb.cursor()
    mycursor.execute("DESCRIBE attendance")
    AllColumnNames=mycursor.fetchall()
    for i in range(len(AllColumnNames)):
        if i in range(3):
            continue
        else:
            columnnames.append(AllColumnNames[i][0])
    classlabel=Label(MarkAttendanceFrame, text="Choose Class to Mark Attendance :").pack()
    class_dropdown=Combobox(MarkAttendanceFrame, values=columnnames, textvariable=column_variable)
    class_dropdown.current(0)
    class_dropdown.pack()
    Button(MarkAttendanceFrame, text="Sumbit", padx=10, pady=2, relief=RAISED, fg="BLACK",
                           activebackground="GREEN", activeforeground="WHITE", command=markattendance2).pack()
    MarkAttendanceFrame.pack()


def teachercall():
    fontchange = Font(family="Courier", size=12)
    marknewattendace = Button(TeacherFrame, font=fontchange, text="Mark Attendance", relief=RAISED,
                              padx=10, pady=3, bg="YELLOW", fg="RED", bd=2, activebackground="BLUE",
                              activeforeground="WHITE", height=1, command=markattendance).pack()
    TeacherFrame.pack(side=TOP, fill="both", expand=True)


teachercall()


root.geometry("960x600+35+22")
root.mainloop()