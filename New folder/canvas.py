from tkinter import *

root=Tk()
root.geometry("1600x800")
c=Canvas(root,bg='green',height=40,width=100)
c.pack(side=LEFT)
h=20
w=300
y=h
c.create_line(0,y,w,y)




root.mainloop()
