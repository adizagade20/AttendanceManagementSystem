from tkinter import *

class menubar:
    def __init__(self, master):
        self.master = master
        self.main_menu = Menu()
        self.master.config(menu = self.main_menu)

        self.file_menu = Menu(self.main_menu, tearoff = False)
        self.edit_menu = Menu(self.main_menu, tearoff = False)
        self.main_menu.add_cascade(label = "File", menu = self.file_menu)
        self.main_menu.add_cascade(label = "Edit", menu = self.edit_menu)

        self.file_menu.add_command(label = "Open")
        self.file_menu.add_command(label = "Save")
        self.file_menu.add_command(label = "Save as")
        self.file_menu.add_separator()
        self.file_menu.add_command(label = "Print")

        self.edit_menu.add_command(label = "Copy")
        self.edit_menu.add_command(label = "Cut")
        self.edit_menu.add_command(label = "Paste")