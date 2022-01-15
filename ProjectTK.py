import random
from tkinter import *
from time import sleep
#
root = Tk()
root['bg'] = 'Gray'
root.geometry('700x360')
root.title('2Games')
root.resizable(width=False, height=False)
#
def randdnum():
    global num345
    num345 = random.randint(1, 100)
def rand_num():
    print('Ваше число: ', og)
    if og != num345:
        if og < num345:
            print("Ваше число меньше")
        elif og > num345:
            print("Ваше число больше")
        elif og == num345:
            print("Вы угадали")
    elif og == num345:
        print('Вы угадали')
def paper():
    rand = random.choice(["Ножницы", "Камень", "Бумага"])
    print("Дайте мне время выбрать")
    sleep(1)
    print("Думаю...")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    if rand == "Ножницы":
        if choice2 == '1':
            print("Вы выбрали ножницы, я выбрал ножницы, ничья")
        elif choice2 == '2':
            print("Вы выбрали камень, я выбрал ножницы, вы выиграли.")
        elif choice2 == '3':
            print("Вы выбрали бумагу, я выбрал ножницы, вы проиграли.")
        else:
            print('Такого ответа нет, вы проиграли')
    elif rand == "Камень":
        if choice2 == '1':
            print("Вы выбрали ножницы, я выбрал камень, вы проиграли.")
        elif choice2 == '2':
            print("Вы выбрали камень, я выбрал камень, ничья.")
        elif choice2 == '3':
            print("Вы выбрали бумагу, я выбрал камень, вы выиграли")
        else:
            print('Такого ответа нет, вы проиграли')

    elif rand == "Бумага":
        if choice2 == '1':
            print("Вы выбрали ножницы, я выбрал бумагу, вы выиграли")
        elif choice2 == '2':
            print("Вы выбрали камень, я выбрал бумагу, вы проиграли")
        elif choice2 == '3':
            print("Вы выбрали бумагу, я выбрал бумагу, ничья")
        else:
            print('Такого ответа нет, вы проиграли')
def cho():
    global choice2
    choice2 = vvod.get()
def num333():
    global og
    og = int(rest.get())
b2 = Button(root, text='Играть в "Камень-ножницы-бумага"', bg = 'DarkGrey', command=paper)
b2.place(x=0, y=45, width=250, height=80)
b1 = Button(root, text='Испытать удачу', bg = 'DarkGrey', command=rand_num)
b1.place(x=0, y=170, width=160, height=93)
vvod = Entry(root, bg = 'LightGray')
vvod.place(x=0, y=20, width=650, height=24)
but = Button(root, text='Выбрать', bg = 'DarkGrey', command=cho)
but.place(x=645, y=20)
poleText = Canvas(root, width = 700, height = 20, bg='Gray')
poleText.create_text(130, 10, text='Выберите: 1-ножницы, 2-камень, 3-бумага', fill='white')
poleText.pack()
rest = Entry(root, bg = 'LightGray')
rest.place(x=0, y=160, width=650, height=24)
num23 = Canvas(root, width = 700, height = 20, bg='Gray')
num23.place(x=0, y = 140)
num23.create_text(100, 10, text='Введите число от 1 до 100', fill='white')
ggnum = Button(root, text = "Ввод", bg = 'DarkGrey', command=num333)
ggnum.place(x=650, y = 162, height=25, width = 55)
numran = Button(root, text='Загадать число', bg = 'DarkGrey', command=randdnum)
numran.place(x=160, y=183, width=150, height=80)
finText = Canvas(root, width = 700, height = 90, bg='Gray')
finText.place(x=0, y=263)
finText.create_text(35, 8, text='Правила', fill='white')
finText.create_text(45, 20, text='1.Ввести число', fill='white')
finText.create_text(180, 32, text='2.Нажать кнопку "Ввод", после нажать кнопку "Загадать число"', fill='white')
finText.create_text(100, 44, text='3.Нажать кнопку "Испытать удачу"', fill='white')




#все ок !
