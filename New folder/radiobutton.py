from tkinter import *

root=Tk()
root.geometry("1600x800")

r1=Radiobutton(root,text="yes",value=0)
r2=Radiobutton(root,text="no",value=1)
r1.pack(side=LEFT)
r2.pack(side=LEFT)

root.mainloop()
