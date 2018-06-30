from tkinter import *

root=Tk()
root.geometry("1600x800")
def hello():
    print("hello")

menu=Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New",command=hello)
filemenu.add_command(label="Open")
editmenu=Menu(menu)
menu.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")





root.mainloop()
