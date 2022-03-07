from tkinter import *
from tkinter import ttk
import tkinter as tk


root = tk.Tk()
root.geometry("300x300")
root.title('Color changer')




g1 = IntVar()
r1 = IntVar()
b1 = IntVar()

g = Checkbutton(root, text ="Green", variable=g1)
g.grid(row=1,stick=W)

r = Checkbutton(root, text ="Red", variable=r1)
r.grid(row=2,sticky=W)


b = Checkbutton(root, text ="Blue", variable=b1)


b.grid(row=3,sticky=W)


def one_Choice():
    anyChecked = b1.get() | r1.get() | g1.get()
    if anyChecked:
        root.destroy()
    else:
        print("error")
Label(root, text='green',bg="green", font="Tahoma").grid(row=6, column=15, pady = 50, padx = 50)


root.mainloop()


