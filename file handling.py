Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> f=open("qqq.txt","r")
>>> print(f.read())
hello
my name is mamta

>>> f=open("qqq.txt","r")
>>> print(f.readline())
hello

>>> f=open("qqq.txt","r")
>>> print(f.readlines())
['hello\n', 'my name is mamta\n']
>>> f=open("qqq.txt","r")
>>> with open("qqq.txt","r") as f:
	d=f.readlines()
	for var in d:
		print(var)

		
hello

my name is mamta

>>> 
