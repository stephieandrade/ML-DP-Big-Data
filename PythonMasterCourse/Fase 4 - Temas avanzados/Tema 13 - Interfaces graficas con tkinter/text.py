from tkinter import *

root = Tk()

text = Text(root)
text.pack()
text.config(width=30, height=30, font=("Consolas", 12), padx=15,
            pady=15, selectbackground="red")  # cantidad de caracteres

root.mainloop()
