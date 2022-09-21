from tkinter import *
import tkinter
import time
root = Tk()

c = Canvas(root, width=600, height=600, bg='white')
c.pack()
#Крест
for i in range(360):

    c.create_line(300, 300, 300, 150)
    c.create_line(300, 300, 300, 450)
    c.create_line(300, 300, 450, 300)
    c.create_line(300, 300, 150, 300)
    #Боковухи
    c.create_line(300, 150, 450, 150)
    c.create_line(450, 300, 450, 450)
    c.create_line(300, 450, 150, 450)
    c.create_line(150, 300, 150, 150)
#c.create_line(300, 300, 300, 150)
#c.create_line(300, 300, 300, 150)
root.mainloop()