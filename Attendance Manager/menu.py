from tkinter import *
root = Tk()
class menubar:
    def __init__(self, master):
        self.master = master
        master.title("Attendance Management System")
        self.main_menu = Menu()
        self.master.config(menu = self.main_menu)

        self.file_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label = "File", menu = self.file_menu)
        self.file_menu.add_cascade(label = "Open")




window = menubar(root)
root.geometry("700x500+300+100")
root.mainloop()