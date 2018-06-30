from tkinter import *

def hello():
    print("Hello")

root=Tk()
root.geometry("1600x800")
ch1=Checkbutton(root,text="tick",command=hello())
ch1.pack(side=LEFT)


root.mainloop()
