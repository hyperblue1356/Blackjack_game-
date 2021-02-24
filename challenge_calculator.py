try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

from tkinter import *

import os

mainWindow = tkinter.Tk()

mainWindow.title("Grid Demo")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = 8

label = tkinter.Label(mainWindow, text="Calculator")
label.grid(row=0, column=0, columnspan=3)

mainWindow.columnconfigure(0, weight=100)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1000)
mainWindow.columnconfigure(3, weight=600)
mainWindow.columnconfigure(4, weight=1000)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

# frame for the radio buttons
optionFrame = tkinter.LabelFrame(mainWindow, text="File Details")
optionFrame.grid(row=1, column=2, sticky='ne')

rbValue = tkinter.IntVar()
rbValue.set(2)

radio1 = tkinter.Radiobutton(optionFrame, text="1", value=1, variable=rbValue, bd=0)
radio2 = tkinter.Radiobutton(optionFrame, text="2", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text="3", value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=0, column=1, sticky='w')
radio3.grid(row=0, column=3, sticky='w')

# Widget to display result
resultLabel = tkinter.Label(mainWindow)
resultLabel.grid(row=0, column=0, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='sw')
mainWindow['padx'] = 8

mainWindow.mainloop()

