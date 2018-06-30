from tkinter import *
import time
import random

root=Tk()
root.geometry("1600x800")
root.title("CALCULATOR")

text_input=StringVar()
op=""

f1=Frame(root,height=200,width=1600,bg="blue")
f1.pack(side=TOP)
f2=Frame(root,height=800,width=1600,bg="green")
f2.pack(side=LEFT)

lb1=Label(f1,font=("ALGERIAN",40),bg="blue",fg="yellow",bd=10,text="CALCULATOR")
lb1.grid()


def btnclick(num):
    global op
    op=op+str(num)
    text_input.set(op)
    
def btnclr():
    global op
    op=""
    text_input.set(op)

def btneq():
    global op
    ans=str(eval(op))
    text_input.set(ans)
    op=""


e1=Entry(f2,font=("arial",20),bd=20,bg="sky blue",justify="right",textvariable=text_input)
e1.grid(columnspan=4)
b1=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:btnclick(1),font=("arial",10),text="1",bg="light green").grid(row=1,column=0)
b2=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:btnclick(2),font=("arial",10),text="2",bg="light green").grid(row=1,column=1)
b3=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:btnclick(3),font=("arial",10),text="3",bg="light green").grid(row=1,column=2)
b4=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:btnclick(4),font=("arial",10),text="4",bg="light green").grid(row=2,column=0)
b5=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:btnclick(5),font=("arial",10),text="5",bg="light green").grid(row=2,column=1)
b6=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:btnclick(6),font=("arial",10),text="6",bg="light green").grid(row=2,column=2)
b7=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:btnclick(7),font=("arial",10),text="7",bg="light green").grid(row=3,column=0)
b8=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:btnclick(8),font=("arial",10),text="8",bg="light green").grid(row=3,column=1)
b9=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:btnclick(9),font=("arial",10),text="9",bg="light green").grid(row=3,column=2)
b0=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:btnclick(0),font=("arial",10),text="0",bg="light green").grid(row=4,column=0)
bp=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:btnclick('+'),font=("arial",10),text="+",bg="light green").grid(row=1,column=3)
bs=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:btnclick('-'),font=("arial",10),text="-",bg="light green").grid(row=2,column=3)
bm=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:btnclick('*'),font=("arial",10),text="*",bg="light green").grid(row=3,column=3)
bdiv=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:btnclick('/'),font=("arial",10),text="/",bg="light green").grid(row=4,column=3)
beq=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:btneq(),font=("arial",10),text="=",bg="light green").grid(row=4,column=1)
bclr=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:btnclr(),font=("arial",10),text="clr",bg="light green").grid(row=4,column=2)

root.mainloop()
