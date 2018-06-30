from tkinter import *

root=Tk()
root.geometry("1600x800")


sb=Scrollbar(root)
sb.pack(side=RIGHT)
lis=Listbox(root,yscrollcommand=sb.set)
for line in range(100):
    lis.insert(END,"my values: "+str(line))
lis.pack(side=RIGHT)
sb.config(command=lis.yview)


root.mainloop()
