from tkinter import *
from tkinter import ttk
import tkinter as tk


root = tk.Tk()
root.geometry("300x300")
root.title('Color changer')

green = IntVar()
Checkbutton(text ="Green", variable = green).grid(row=1,stick=W)
red = IntVar()
Checkbutton(text ="Red", variable = red).grid(row=2,sticky=W)
blue = IntVar()
Checkbutton(text ="Blue", variable = blue).grid(row=3,sticky=W)



Label(root, text='green',bg="green", font="Tahoma").grid(row=6, column=15, pady = 50, padx = 50)


root.mainloop()


