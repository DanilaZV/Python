import tkinter
import tkinter.messagebox
import random
#import tkinter as tk
 
root =tkinter.Tk()
#app = tk.Tk()
root.geometry('280x100')
root.title('Игра')
 
number=random.randint(1,100)
#Проверка числа
def check_num():
    guess=text_guess.get()
    #guess=int(guess)
    if guess == str():
        tkinter.messagebox.showinfo("Ответ","Нужно ввести ЗНАЧЕНИЕ!!!") 
    if int(guess)>number:
        tkinter.messagebox.showinfo("Ответ","Ваше число слишком большое")
    if int(guess) < number:
        tkinter.messagebox.showinfo("Ответ","Ваше число слишком маленькое")       
    if int(guess) == number:
        tkinter.messagebox.showinfo("Ответ","Вы угадали!")
        #Закрытие игры
        exit()
    #Самоотчистка строки ввода
    text_guess.delete(0, 'end')


def check_num1(event):
    guess=text_guess.get()
    #guess=int(guess)
    if guess == str():
        tkinter.messagebox.showinfo("Ответ","Нужно ввести ЗНАЧЕНИЕ!!!") 
    if int(guess)>number:
        tkinter.messagebox.showinfo("Ответ","Ваше число слишком большое")
    if int(guess) < number:
        tkinter.messagebox.showinfo("Ответ","Ваше число слишком маленькое")       
    if int(guess) == number:
        tkinter.messagebox.showinfo("Ответ","Вы угадали!")
        #Закрытие игры
        exit()
    #Самоотчистка строки ввода
    text_guess.delete(0, 'end')

    

#Перед вводом значения 
label_guess=tkinter.Label(root,text='Введите значение:')
label_guess.place(x=10,y=50)
#Ввод значения
text_guess=tkinter.Entry(root,width=10)
text_guess.place(x=115,y=50)
#Кнопка
btnCheck=tkinter.Button(root,text='Угадать',command=check_num)
btnCheck.place(x=200,y=45,width=50,height=30)

root.bind('<Return>', check_num1)
root.mainloop()