from tkinter import *

root = Tk()
root.title("Счётчик кликов")
root.geometry("950x500")
root.resizable(width=False, height=False)

count = 0

def spam():
    global count
    count +=1
    Click.configure(text=count)

Click = Label(root, text='0', font='Arial 35')
Click.pack()

btn = Button(root, text='Нажмешь, негр', padx='20', pady='20', command=spam)
btn.pack()
