from tkinter import *

root = Tk()
"""
frame = Frame(root, width=480, height=320)
frame.pack()

label = Label(frame, text='Hola mundo')
label.place(x=0, y=0)

"""

imagen=PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack(side='left')
root.mainloop()