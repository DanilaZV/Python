from tkinter import *
 
class App:
    def __init__(self,master):
       master.title('Python Canvas Testing')
       master.minsize(width=550, height=450)
 
       settingscanvas = Canvas(master,bg="yellow")
       settingscanvas.grid(row=0, column=1)
 
       datacanvas = Canvas(master,bg="green")
       datacanvas.grid(row=1, column=1)
 
       master.grid_rowconfigure(2,weight=1)
       master.grid_columnconfigure(2, weight=1)
 
       datacanvas2 = Canvas(master,bg="black")
       datacanvas2.grid(row=1, column=0)
 
window = Tk()
 
app = App(window)
 
mainloop()