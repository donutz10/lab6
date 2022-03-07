from tkinter import *
from tkinter import ttk
import tkinter as tk

def is_checked():
    if g1.get() == 1:
        r.deselect()
        b.deselect()
        text1 = Label(root, bg="green", text='Select Button to change the color \nsimply deselect to choose another color', font="Tahoma")
        text1.grid(row=6, column=15, pady = 50, padx = 50)
    elif r1.get() == 1:
        g.deselect()
        b.deselect()
        text1 = Label(root, bg="red", text='Select Button to change the color \nsimply deselect to choose another color', font="Tahoma")
        text1.grid(row=6, column=15, pady = 50, padx = 50)
    elif b1.get() == 1:
        g.deselect()
        r.deselect()
        text1 = Label(root, bg="blue", text='Select Button to change the color \nsimply deselect to choose another color', font="Tahoma")
        text1.grid(row=6, column=15, pady = 50, padx = 50)
    else:
        r.deselect()
        b.deselect()
        g.deselect()


root = tk.Tk()
root.geometry("450x450")
root.title('Color changer')



i = IntVar()
g1 = IntVar()
r1 = IntVar()
b1 = IntVar()

g = Checkbutton(root, text ="Green", variable=g1 , bg="green", command=is_checked)
g.grid(row=1,stick=W)

r = Checkbutton(root, text ="Red", variable=r1, bg="red", command=is_checked)
r.grid(row=2,sticky=W)


b = Checkbutton(root, text ="Blue", variable=b1, bg="blue", command=is_checked)
b.grid(row=3,sticky=W)


#### fix this and add only one choice


# add thing to change the text if selection is done
text1 = Label(root, text='Select Button to change the color \nsimply deselect to choose another color', font="Tahoma", bg="Purple")
text1.grid(row=6, column=15, pady = 50, padx = 50)


root.mainloop()


