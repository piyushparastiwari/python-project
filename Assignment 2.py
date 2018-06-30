# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 11:23:48 2018

@author: KrRish
"""
#create a list with user defined input
li=list(map(int,input().split()))
li1=['google','apple','facebook','microsoft','tesla','tesla']
li=li+li1
li
for i in li:
    print(i,li.count(i))
    
liNum=[5,9,8,4,1,23,56,4,84]
liNum.sort()
liNum


tu= (1,23.0,"krrish")
type(tu)
len(tu)

sa={"as"}
type(sa)

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
etype(dict)