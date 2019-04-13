from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from tkinter.ttk import Combobox
import mysql.connector


class StudentRoot:
    def __init__(self, root):
        self.master = root
        self.StudentFrame = Frame(self.master, background='gray53')
        self.DisplayStudentFrame = Frame(self.master, background='gray53')
        self.prn_variable = IntVar()
        self.database = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
        self.mycursor = self.database.cursor()


    def studentcall(self):
        self.destroy1()
        self.__init__(self.master)
        change_font = Font(family="Courier", size=12)
        Label(self.StudentFrame, text="Choose your PRN Number :- ", font=change_font, bg='gray53', fg='white').place(x=240, y=30)
        self.mycursor.execute("select PRN_Number, IsDeleted from attendance ORDER BY PRN_Number ASC")
        self.prn_numbers = self.mycursor.fetchall()
        prn = []
        for i in range(len(self.prn_numbers)):
            if self.prn_numbers[i][1] == 0:
                prn.append(self.prn_numbers[i][0])
        combobox = Combobox(self.StudentFrame, values=prn, textvariable=self.prn_variable)
        combobox.current(0)
        combobox.state(['readonly'])
        combobox.bind("<FocusIn>", self.defocus)
        combobox.place(x=540, y=30)
        Button(self.StudentFrame, text="Search", padx=5, pady=2, relief=RAISED, activebackground="BLUE", activeforeground="WHITE", font=Font(size=12), command=self.search_details).place(x=570, y=80)
        self.StudentFrame.pack(side=TOP, fill="both", expand=True)


    def defocus(self, event):
        event.widget.master.focus_set()


    def search_details(self):
        try:
            self.sql = "SELECT * FROM attendance WHERE PRN_Number='%s'"
            self.key = (self.prn_variable.get(),)
            self.mycursor.execute(self.sql, self.key)
            self.details = self.mycursor.fetchall()
            self.columns = (
            "Roll_No", "PRN_Number", "Name", "AM4", "AM4_Tut", "AOA", "AOA_Lab", "CG", "CG_Lab", "OS", "OS_Lab", "COA",
            "COA_Lab", "OSTL_Th", "OSTL")
            for i in range(len(self.columns) - 1):
                Label(self.DisplayStudentFrame, text=self.columns[i], bg='gray53', fg='white').grid(row=i + 6, column=6, stick=W, pady=2)
                Label(self.DisplayStudentFrame, text=self.details[0][i], bg='gray53', fg='white').grid(row=i + 6, column=7, stick=E)
            self.DisplayStudentFrame.pack(side=TOP, fill="both", expand=True, padx=400)
        except:
            messagebox.showerror("Not found", "Entered PRN can't be found, please Recheck!")
            self.destroy1()
            self.__init__(self.master)
            self.studentcall()


    def destroy1(self):
        self.StudentFrame.destroy()
        self.DisplayStudentFrame.destroy()





if __name__=='__main__':
	root=Tk()
	root.geometry("1000x600+180+30")
	root.resizable(0,0)
	root.configure(background='gray53')
	a=StudentRoot(root)
	a.studentcall()
	root.mainloop()