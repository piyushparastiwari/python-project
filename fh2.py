Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
f=open("qqq.txt","r")
>>> print(f.read)
<built-in method read of _io.TextIOWrapper object at 0x000000643F56B1F8>
>>> print(f.read())
this is python class
>>> f=open("qqq.txt","r")
>>> f=open("qqq.txt","w")
>>> f.write(input(" adding data in append mode"))
 adding data in append modef=open("qqq.txt","r")
21
>>> f=open("qqq.txt","r")print(f.read())
SyntaxError: invalid syntax
>>> print(f.read)
<built-in method read of _io.TextIOWrapper object at 0x000000643F56B1F8>
>>> print(f.read())
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(f.read())
io.UnsupportedOperation: not readable
>>> f=open("qqq.txt","r")
>>> print(f.read())
f=open("qqq.txt","r")
>>> print(f.read())

>>> 
>>> f=open("qqq.txt","w")
>>> f.write(input(" adding data in append mode"))
 adding data in append mode
0
>>> f=open("qqq.txt","r")
>>> print(f.read())

>>> 
>>> f=open("qqq.txt","a")
>>> f.write(input(" adding data in append mode"))
 adding data in append mode
0
>>> f=open("qqq.txt","r")
>>> print(f.read())

>>> 
