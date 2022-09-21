from tkinter import *
window = Tk()
window.title("Visual Studio Code")
window.geometry("400x300+500+250")
def ex(event):
    quit()
bat1 = Button(window)
bat1['text'] = 'Окей'
bat1.bind('<Button-1>', ex)
bat1.pack()
window. mainloop()