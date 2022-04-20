from tkinter import *

root = Tk() #raiz
root.resizable(1,0)
root.iconbitmap('hola.ico')

frame = Frame(root, width=480, height=320)
frame.pack(fill='both', expand=1) #empaquetamos frame, que se distribuya en si mismo
frame.config( cursor='pirate') #establecemos dimensiones
frame.config(bg='lightblue', bd=25, relief='sunken')

root.config(cursor='arrow', bg='blue', bd=15, relief='ridge')
root.mainloop()
