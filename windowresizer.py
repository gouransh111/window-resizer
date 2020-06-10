from tkinter import *
root = Tk()
def resize():
    root.geometry(f"{canvaw.get()}x{canvah.get()}")
canvaw=StringVar()
canvah=StringVar()
root.geometry("300x300")
Label(text="Enter new window width here").grid(row=0,column=0)
Label(text="Enter new window height here").grid(row=1,column=0)
Entry(root,textvariable=canvaw).grid(row=0,column=1)
Entry(root,textvariable=canvah).grid(row=1,column=1)
Button(root,text="submit",command=resize).grid(row=3,column=0)
root.mainloop()