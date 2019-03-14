import tkinter as tk
class ClassList(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, FirstPage, SecondPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page")
        label.pack()
        button = tk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(FirstPage))
        button.pack()
        button1 = tk.Button(self, text="Visit Page 2", command=lambda: controller.show_frame(SecondPage))
        button1.pack()

class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="First Page")
        label.pack()
        button = tk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(FirstPage))
        button.pack()
        button1 = tk.Button(self, text="Visit Page 2", command=lambda: controller.show_frame(SecondPage))
        button1.pack()


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Second Page")
        label.pack()
        button = tk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(FirstPage))
        button.pack()
        button1 = tk.Button(self, text="Visit Page 2", command=lambda: controller.show_frame(SecondPage))
        button1.pack()

app =  ClassList()
app.mainloop()