try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

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

# Widget to display result
resultLabel = tkinter.Label(mainWindow)
resultLabel.grid(row=0, column=0, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='sw')
mainWindow['padx'] = 8

mainWindow.mainloop()

