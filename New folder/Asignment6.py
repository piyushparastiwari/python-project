Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> f.open("file1.txt","r")
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    f.open("file1.txt","r")
NameError: name 'f' is not defined
>>> f=open("file1.txt","r")
>>> print(f.read())
My name is Monika Singh.
>>> print(f.readlines())
[]
>>> print(f.readlines())
['\n', 'abcd..']
>>> f=open("file1.txt","r")
>>> print(f.readlines())
['My name is Monika Singh.\n', 'abcd..']
>>> f=open("file1.txt","r")
>>> 
