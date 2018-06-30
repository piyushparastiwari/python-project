from tkinter import *

root=Tk()
root.geometry("1600x800")
ls=Listbox(root,bg="green",height=20,width=20)
l=["Delhi","Noida","Gurgaon","Malviya Nagar"]
i=0
for val in l:
    ls.insert(i,val)
    i+=1
    ls.pack(side=LEFT)

root.mainloop()


