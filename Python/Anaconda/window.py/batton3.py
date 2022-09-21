from tkinter import *

window = Tk()
window.title("Visual Studio Code")
window.geometry("400x300+500+250")

def ex(event):
    quit()

#Кнопка 1   
bat1 = Button(window)
bat1['text'] = 'EXIT IN WINDOW'
bat1.bind('<Button-1>', ex)
bat1.pack(padx=100, pady=30)

#Кнопка 2
bat2 = Button(window)
bat2['text'] = 'FULL SCREEN'
bat2.bind('<Button-2>', )
bat2.pack(padx=120, pady=30)

#Кнопка 3
bat3 = Button(window)
bat3['text'] = 'Нажми на меня!!!'
bat3.config(command=lambda: print("Как пердят мужчины:"))
bat3.pack(padx=150, pady=30)

window.mainloop()


