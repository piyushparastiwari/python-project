# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 09:52:26 2018

@author: KrRish
"""

#***********************************************************
a=3
try:
    if a<4:
        b=a/(a-3)
        print(b)
except ZeroDivisionError:
    print("denominator can't be zero")
#***********************************************************
l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print("list index out of bound")
 
#***********************************************************
try:
    raise NameError("Hi there")
except NameError:
        print("An exception")
       

#***********************************************************
try:
    a=(-10)
    if(a<0):
        raise NameError()
except NameError:
        print("value can't be negative")
     
        
#***********************************************************
def AbyB(a,b):
    try:
        c((a+b)/(a-b))
    except ZeroDivisionError:
        print("a/b result in zero")
    else:
        print(c)
        
AbyB(2,3)       
#***********************************************************
number = 10

while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError
       elif i_num > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This value is too small, try again!")
       print()
   except ValueTooLargeError:
       print("This value is too large, try again!")
       print()

print("Congratulations! You guessed it correctly.")