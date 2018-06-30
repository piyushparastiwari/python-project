Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> f=open("fil.txt","r")
>>> print(f.read())
Hello world
!!!!!!!!!!!
>>> f=open("fil.txt","r")
>>> print(f.readline())
Hello world

>>> f=open("fil.txt","r")
>>> print(f.readlines())
['Hello world\n', '!!!!!!!!!!!']
>>> 
f=open("fil.txt","r")
>>> with open("fil.txt","r")
SyntaxError: invalid syntax
>>> f=open("fil.txt","r")
>>> with open("fil.txt","r") as f:
	d=f.readlines()
	for var in d:
		print(var)

		
Hello world

!!!!!!!!!!!
>>> f=open("fil.txt","w")
>>> f.write(input)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    f.write(input)
TypeError: write() argument must be str, not builtin_function_or_method
>>> f=open("fil.txt","w")
>>> f.write(input("Enter your text: "))
Enter your text: "I am changing my data"
23
>>> f=open("fil.txt","r")
>>> print(f.readlines())
['"I am changing my data"']
>>> f=open("fil.txt","r")
>>> print(f.read())
"I am changing my data"
>>> f=open("fil.txt","a")
>>> f.write(input("Enter your text: "))
Enter your text: "Adding data in append mode"
28
>>> f=open("fil.txt","r")
>>> print(f.read())
"I am changing my data""Adding data in append mode"
>>> 
f=open("fil.txt","r")
>>> print(f.read())
"I am changing my data""Adding data in append mode"
>>> f.write(input())
"adding in read mode"
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    f.write(input())
io.UnsupportedOperation: not writable
>>> f=open("fil.txt","r+")
>>> f.write(input())
"adding in r mode"
SyntaxError: multiple statements found while compiling a single statement
>>> f=open("fil.txt","r+")
>>> f.write(input())"adding in r mode"
SyntaxError: invalid syntax
>>> f=open("fil.txt","r+")
>>> f.write(input())
f.write(input())
"adding in r mode"
16
>>> f=open("fil.txt","r+")
>>> f.write(input())
18
>>> print(f.read())
data""Adding data in append mode"
>>> f=open("fil.txt","w")
>>> f.write(input("Enter your text: "))
Enter your text: I am changing my data
21
>>> print(f.read())
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print(f.read())
io.UnsupportedOperation: not readable
>>> f=open("fil.txt","r")
>>> print(f.read())
I am changing my data
>>> f=open("fil.txt","r+")
>>> f.write(input())
"adding data in r+ mode"
24
>>> f.close()
>>> f=open("fil.txt","r+")
>>> print(f.read())
"adding data in r+ mode"
>>> f=open("fil.txt","r+")
>>> f.write(input())
"adding other data in r+ mode"
SyntaxError: multiple statements found while compiling a single statement
>>> f=open("fil.txt","r+")
>>> f.write(input())
"adding other data in r+ mode"
30
>>> print(f.read())

>>> print(f.read())

>>> f=open("fil.txt","r")
>>> print(f.read())
"adding other data in r+ mode"
>>> print(f.read())

>>> f.seek(0,0)
0
>>> print(f.read())
"adding other data in r+ mode"
>>> f.seek(5,0)
5
>>> print(f.read())
ng other data in r+ mode"
>>> print(f.read())

>>> f.seek(0,0)
0
>>> print(f.read())
"adding other data in r+ mode"
>>> f.close()
>>> 
