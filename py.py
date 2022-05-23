from tkinter import *
from Tutorial import PythonTitle
 
 
root = Tk()
 
# specify size of window.
root.geometry("250x170")
 
# Create text widget and specify size.
T = Text(root, height = 250, width = 170)
T.config(bg='black', fg='white', insertbackground='blue')
T.pack()
# Insert The Fact.
T.insert(END, PythonTitle)
 
root.mainloop()