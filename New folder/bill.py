from tkinter import *
import time
import random

root=Tk()
root.geometry("1600x800")
root.title("Burger King")

text_input=StringVar()
op=""

f1=Frame(root,height=200,width=1600,bg="blue")
f1.pack(side=TOP)

f2=Frame(root,height=1000,width=1000,bg="powder blue")
f2.pack(side=RIGHT)

f3=Frame(root,height=600,width=600,bg="powder blue")
f3.pack(side=LEFT)

localtime=time.asctime(time.localtime(time.time()))

lb1=Label(f1,font=("ALGERIAN",40),bg="blue",fg="yellow",bd=10,text="BILL BANWA LO")
lb1.grid()
lb2=Label(f1,font=("ALGERIAN",20),bg="blue",fg="yellow",bd=10,text=localtime)
lb2.grid(row=1,column=0)

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

def btntot():
    global op1
    ans1=str(eval(op1))
    text_input.set(ans1)
    op1=""
'''def btnreset():
def btnexit():'''

e1=Entry(f2,font=("arial",20),bd=20,bg="sky blue",justify="right",textvariable=text_input)
e1.grid(columnspan=4)

lb3=Label(f3,font=("arial",10),bg="powder blue",fg="black",bd=10,text="Large Fries")
lb3.grid(row=0,column=0)
e2=Entry(f3,font=("arial",10),bd=10,bg="sky blue",justify="right",textvariable=text_input)
e2.grid(row=0,column=1)
lb4=Label(f3,font=("arial",10),bg="powder blue",fg="black",bd=10,text="Lage Burger")
lb4.grid(row=1,column=0)
e3=Entry(f3,font=("arial",10),bd=10,bg="sky blue",justify="right",textvariable=text_input)
e3.grid(row=1,column=1)
lb5=Label(f3,font=("arial",10),bg="powder blue",fg="black",bd=10,text="Cold Drink")
lb5.grid(row=2,column=0)
e4=Entry(f3,font=("arial",10),bd=10,bg="sky blue",justify="right",textvariable=text_input)
e4.grid(row=2,column=1)
lb6=Label(f3,font=("arial",10),bg="powder blue",fg="black",bd=10,text="Meal")
lb6.grid(row=3,column=0)
e5=Entry(f3,font=("arial",10),bd=10,bg="sky blue",justify="right",textvariable=text_input)
e5.grid(row=3,column=1)
lb7=Label(f3,font=("arial",10),bg="powder blue",fg="black",bd=10,text="Whopper")
lb7.grid(row=4,column=0)
e6=Entry(f3,font=("arial",10),bd=10,bg="sky blue",justify="right",textvariable=text_input)
e6.grid(row=4,column=1)
lb8=Label(f3,font=("arial",10),bg="powder blue",fg="black",bd=10,text="Invoice Number")
lb8.grid(row=0,column=2)
e7=Entry(f3,font=("arial",10),bd=10,bg="sky blue",justify="right",textvariable=text_input)
e7.grid(row=0,column=3)
lb9=Label(f3,font=("arial",10),bg="powder blue",fg="black",bd=10,text="Service Charge")
lb9.grid(row=1,column=2)
e8=Entry(f3,font=("arial",10),bd=10,bg="sky blue",justify="right",textvariable=text_input)
e8.grid(row=1,column=3)
lb10=Label(f3,font=("arial",10),bg="powder blue",fg="black",bd=10,text="CGST + SGST")
lb10.grid(row=2,column=2)
e9=Entry(f3,font=("arial",10),bd=10,bg="sky blue",justify="right",textvariable=text_input)
e9.grid(row=2,column=3)
lb11=Label(f3,font=("arial",10),bg="powder blue",fg="black",bd=10,text="Sub Total")
lb11.grid(row=3,column=2)
e10=Entry(f3,font=("arial",10),bd=10,bg="sky blue",justify="right",textvariable=text_input)
e10.grid(row=3,column=3)
lb12=Label(f3,font=("arial",10),bg="powder blue",fg="black",bd=10,text="Total")
lb12.grid(row=4,column=2)
e11=Entry(f3,font=("arial",10),bd=10,bg="sky blue",justify="right",textvariable=text_input)
e11.grid(row=4,column=3)
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

bdiv=Button(f3,padx=25,pady=15,bd=8,fg="black",command=lambda:btntot(),font=("arial",10),text="Total",bg="light green").grid(row=5,column=1)
beq=Button(f3,padx=25,pady=15,bd=8,fg="black",command=lambda:btnreset(),font=("arial",10),text="Reset",bg="light green").grid(row=5,column=2)
bclr=Button(f3,padx=25,pady=15,bd=8,fg="black",command=lambda:btnexit(),font=("arial",10),text="Exit",bg="light green").grid(row=5,column=3)

root.mainloop()
