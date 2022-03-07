from tkinter import *
from tkinter import ttk
import tkinter as tk


root = tk.Tk()

Tk()

root.title('Color changer')
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='tab1')
ttk.Label(tab1, text = "Text")