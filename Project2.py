from tkinter import *
root = Tk()
root['bg'] = 'White'
root.geometry('350x450')
root.title('Калькулятор')
root.resizable(width=False, height=False)
#Поле вывода
btnConc = Entry(root, bg='LightGray')
btnConc.place(x=75,y=65, width=350, height=49)
#Поле для ввода
task = Entry(root, bg='LightGray')
task.place(x=0, y=0, width = 350, height=66)
#(Кнопка деления
def numDiv():
    task.insert(END, '/')
btnDiv = Button(root, text='/', bg = 'LightGrey', command=numDiv)
btnDiv.place(x=276, y=385, height=70, width=75)
#(Кнопка умножения
def numMult():
    task.insert(END, '*')
btnMult = Button(root, text='×', bg='LightGrey', command=numMult)
btnMult.place(x=276, y=315, height=70, width=75)
#(Кнопка суммы
def numSun():
    task.insert(END, '+')
btnSum = Button(root, text='+', bg='LightGrey', command=numSun)
btnSum.place(x=276, y=247, height=70, width=75)
#Кнопка -
def numSub():
    task.insert(END, '-')
btnSub = Button(root, text='-', bg='LightGrey', command=numSub)
btnSub.place(x=276, y=178, height=70, width=75)
#Кнопка х²
def numSq():
    task.insert(END, '**2')
btnSq = Button(root, text='х²', bg='LightGrey', command=numSq)
btnSq.place(x=276, y=110, height=70, width=75)
#Кнопка =
def numRav():
    '²' == '*'
    a=task.get()
    n = eval(a)
    btnConc.insert(0, n)
btnRav = Button(root, text='=', bg='Gainsboro', command=numRav)
btnRav.place(x=0,y=65, height=50, width=75)
#Кнопка -x
def num_X():
    task.insert(END, '-')
btn_X = Button(root, text='-x', bg='LightGrey', command=num_X)
btn_X.place(x=0, y=382, height=70, width=92)
#Кнопка 0
def num0():
    task.insert(END, '0')
btn0 = Button(root, text='0', bg='DarkGray', command=num0)
btn0.place(x=90, y=382, height=70, width=92)
#Кнопка (
def numBrack1():
    task.insert(END, '(')
btnBrack1 = Button(root, text='(', bg='LightGrey', command=numBrack1)
btnBrack1.place(x=180, y=382, height=70, width=48)
#Кнопка )
def numBrack2():
    task.insert(END, ')')
btnBrack2 = Button(root, text=')', bg='LightGrey', command=numBrack2)
btnBrack2.place(x=228, y=382, height=70, width=48)
#Кнопка 9
def num9():
    task.insert(END, '9')
btn9 = Button(root, text='9', bg='DarkGray', command=num9)
btn9.place(x=180, y=313, height=70, width=96)
#Кнопка 8
def num8():
    task.insert(END,'8')
btn8 = Button(root, text='8', bg='DarkGray', command=num8)
btn8.place(x=89, y=313, height=70, width=92)
#Кнопка 7
def num7():
    task.insert(END, '7')
btn7 = Button(root, text='7', bg='DarkGray', command=num7)
btn7.place(x=0, y=313, height=70, width=92)
#Кнопка 6
def num6():
    task.insert(END, '6')
btn6 = Button(root, text='6', bg='DarkGray', command=num6)
btn6.place(x=180, y=243, height=70, width=96)
#Кнопка 5
def num5():
    task.insert(END, '5')
btn5 = Button(root, text='5', bg='DarkGray', command=num5)
btn5.place(x=89, y=243, height=70, width=92)
#Кнопка 4
def num4():
    task.insert(END, '4')
btn4 = Button(root, text='4', bg='DarkGray', command=num4)
btn4.place(x=0, y=243, height=70, width=92)
#Кнопка 3
def num3():
    task.insert(END, '3')
btn3 = Button(root, text='3', bg='DarkGray', command=num3)
btn3.place(x=180, y=173, height=70, width=96)
#Кнопка 2
def num2():
    task.insert(END, '2')
btn2 = Button(root, text='2', bg='DarkGray', command=num2)
btn2.place(x=89, y=173, height=70, width=92)
#Кнопка 1
def num1():
    task.insert(END, '1')
btn1 = Button(root, text='1', bg='DarkGray', command=num1)
btn1.place(x=0, y=173, height=70, width=92)
#Кнопка clear
def clear():
    task.delete(0, END)
    btnConc.delete(0, END)
btnClear = Button(root, text='CLEAR', bg='DarkGray', command=clear)
btnClear.place(x=0,y=114, height=60, width=276)





















