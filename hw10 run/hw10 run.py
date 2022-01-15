from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=2000, height=1500)
canvas.pack()
bot = PhotoImage(file="sunshine.png")
id_bober = canvas.create_image(50, 50, anchor=NW, image=bot)
print(id_bober)
import time

for i in range(1, 100):
    canvas.move(id_bober,2,0)
    tk.update()
    time.sleep(0.02)
