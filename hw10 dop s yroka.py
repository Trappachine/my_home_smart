from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=600, height=600)
tk.title("Image")
canvas.pack()

def bg_green():
    canvas.configure(bg="green")
    id_btn.configure(bg="green", activebackground="green")
    label.configure(bg="green", activebackground="green")
def bg_orange():
    canvas.configure(bg="orange")
    id_btn.configure(bg="orange", activebackgroung="orange")
    label.configure(bg="orange", activebackgroung="orange")

btn = PhotoImage(file="button.png")
id_img = canvas.create_image(220, 100, anchor="nw", image=btn)
id_btn = Button(tk, image=btn, command=bg_green)
id_btn.place(x=200, y=100)

label=Label(tk, image=btn)
label.place(x=200, y=200)
label.bind("Button-1", bg_orange)
label.bind("Enter", lambda event: label.place(x=302, y=102))
label.bind("Leave", lambda event: label.place(x=300, y=100))






tk.mainloop()
