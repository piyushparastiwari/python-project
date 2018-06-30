# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 10:16:18 2018

@author: KrRish
"""

import os

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")
os.chdir("E:\python")


f=open("file.txt","r")
print(f.readline(5))
print(f.read())
print(f.readlines())

#**********************************************
f=open("file.txt","r")
with open("file.txt",'r') as f:
    d=f.readlines()
    for var in d:
        print(var)
        
#***********************************************
f=open("file.txt","r+")
