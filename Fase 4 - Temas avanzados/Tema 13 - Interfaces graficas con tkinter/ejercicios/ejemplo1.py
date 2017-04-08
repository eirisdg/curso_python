from tkinter import *

root = Tk()

root.title("Hola mundo")
root.resizable(0,0)
root.iconbitmap("@hola.xbm")

frame = Frame(root, width=480, height=320)
frame.pack()
frame.config(bg="lightblue")

root.mainloop()