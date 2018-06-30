# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:02:03 2018

@author: KrRish
"""

print("hello")
35

print(1,2,3*5,sep="/")


print("\'krrish\'")

print(" my name is \"krrish\"")
print(" my name is \\krrish\\" ,end="***")

mylist = [1, 2, 3,15,20]
for i in mylist:
    print(i)

#90 angle triangle    
for i in range(0,5):
    for y in range(0,i+1):
        print("* ",end="")
    print("\r")
    
#180' flip trinagle
k=5*2-2
for i in range(0,5):
    for j in range(0,k):
        print(end=" ")
    k=k-2
    for j in range(0,i+1):
        print("* ",end="")
    print("\r")
    

#proper triangle
k=5*2-2
for i in range(0,5):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("* ",end="")
    print("\r")
    
#opposite triangle
for i in range(1,5):
    for j in range(5,i,-1):
        print("* ",end="")
    print()
    
#abcde triangle
a=65
for i in range(6):
    for j in range(i+1):
        print(chr(a+j),end="")
    print()

    
#abcde opposite triangle
a=65
for i in range(6):
   for j in range(6,i,-1):
       print(chr(a+j),end="")
   print()
 
#abcde with space triangle
a=65
for i in range(6):
    sum1=0
    for j in range(6,i,-1):
        print(chr(a+sum1),end="")
        sum1+=1
    print()
    

a=65
for i in range(6):
    num=i
    for j in range(6,i,-1):
        print(" ",end ="") 
    for m in range(i+1):
        print(chr(a+(num-m)),end="")
    print()


#alphabet triangle
a=65
for i in range(6):
    num=i
    for j in range(6,i,-1):
        print(" ",end ="") 
    for m in range(i+1):
        print(chr(a+(num-m)),end="")
    for m in range(1,i+1):
        print(chr(a+m),end="")
    print()    


#calculate area
r=float(input("Enter a radius: "))
area=3.14 * r *r
area

tu=("krrish",)*5
type(tu)


#leap year
year=int(input())
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not a leap year")


#dictionary

a={'a':1,'b':2}
b={'a':11,'c':13}
for i in a.keys() & b.keys():
    print(i)
    

a=['a','b','c']
b=[1,2,3]
for i in a:
    for j in b:
        print(i,j)
        


li=tuple([[i,j] for i in a for j in b])
print(''.join(li))


l=['Ram','Abhishek','Seema','seeta','Seema','Ram','Seema']
d={}
for i in range(len(l)):
    con=l.count(l[i])
    d[l[i]]=con
print(''.join(d[i]))


d={}
for _ in range(int(input())):
    name = input()
    score = float(input())
    d[str(name)]=score


#*****************************************************************************
import os
os.name
os.listdir('.')

import time

def ti(a1):
    a=time.strftime("%H:%M:%S")
    if(a!=a1):
        return(a)
        
a=time.strftime("%H:%M:%S")
for i in range(30):
    a=ti(a)
    print(a)
    
import os
import time
x=1
while(x>0):
    print(time.strftime("%H:%M:%S"))
    time.sleep(1)
    os.system('cls')

#**************************************************************


a=tuple(map(int,input().split()))
a   