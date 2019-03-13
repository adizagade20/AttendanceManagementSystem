from tkinter import *
from tkinter.font import Font
import time
root = Tk()

def get_prn():
    prn = prn_var.get()
    print(prn)
    return prn

frame = Frame(root, width=700, height=500)
fontchange = Font(family="Courier", size=12)
entry = Label(root, text="Enter your Name :-", font=fontchange)
entry.place(x=50, y=40)
prn_var = IntVar()
enter_name = Entry(root, textvariable=prn_var, width=30)
enter_name.place(x=250, y=45)
submit_button = Button(root, text = "Search", padx = 10, pady = 2, relief = RAISED, fg = "BLACK", activebackground = "GREEN", activeforeground = "WHITE")
submit_button.place(x=250, y=100)
frame.pack()



root.mainloop()

x = get_prn()
print(x)
