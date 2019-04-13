from tkinter import *
from tkinter.ttk import Combobox

def defocus(event):
    event.widget.master.focus_set()

root = Tk()

comboBox = Combobox(root, state="readonly", values=("a", "b", "c"))
comboBox.grid()
comboBox.set("a")
#comboBox.bind("<FocusIn>", defocus)

mainloop()



"""
from tkinter import *
import tkinter
import tkinter.messagebox
from PIL import Image
from PIL import ImageTk

master = Tk()

def callback():
    print("click!")

width = 50
height = 50
img = Image.open("student.png")
img = img.resize((width,height), Image.ANTIALIAS)
photoImg =  ImageTk.PhotoImage(img)
b = Button(master,image=photoImg, command=callback, width=50)
b.pack()
master.geometry("400x400+100+100")
mainloop()
"""
"""
from tkinter import *
root = Tk()
frame = Frame(root, width=10, height=10)
try:
    photo = PhotoImage(file = "1.jpg")
except:
    photo = PhotoImage(file = "student.png")
photo = photo.zoom(25)
photo = photo.subsample(32)
Label(frame, image=photo).pack()
frame.pack()
root.geometry("800x400+100+100")
root.mainloop()
"""