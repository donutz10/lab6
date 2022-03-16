from tkinter import *
from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.geometry("150x150")
r = IntVar()
root.title('Color changer')
Radiobutton(root, text="Red", variable = r, value = 1,command=lambda: color(r.get())).pack()
Radiobutton(root, text="Blue", variable = r, value = 2, command= lambda: color(r.get())).pack()
Radiobutton(root, text="green", variable = r, value = 3, command=lambda: color(r.get())).pack()
myLabel = Label(root, text="No selection provided", bg='purple')
myLabel.pack()
def color(value):
    if value == 1:
        global myLabel
        myLabel.destroy()
        myLabel = Label(root, text="You have selected Red", bg="red", fg="white")
        myLabel.pack()
    elif value == 2:
        myLabel.destroy()
        myLabel = Label(root, text="You have selected Blue", bg="Blue", fg="white")
        myLabel.pack()
    elif value == 3:
        myLabel.destroy()
        myLabel = Label(root, text="You have selected Green", bg="green", fg="black")
        myLabel.pack()
        








mainloop()