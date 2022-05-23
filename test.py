from tkinter import *
root = Tk()
root.bind("<Key>", lambda e: Label(root, text='hi').pack())
root.mainloop()