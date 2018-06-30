Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def chk():
	name=input("Enter your name: ")
	age=int(input("Enter age: "))
	print("name: ",name)
	print("age: ",age)
	input()

	
>>> chk()
Enter your name: Monika
Enter age: 23
name:  Monika
age:  23

>>> chk('Monika',23)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    chk('Monika',23)
TypeError: chk() takes 0 positional arguments but 2 were given
>>> chk(56,'ABC')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    chk(56,'ABC')
TypeError: chk() takes 0 positional arguments but 2 were given
>>> def chk():
	name=input("Enter your name: ")
	age=int(input("Enter age: "))
	print("name: ",name)
	print("age: ",age)
	input()

	
>>> chk(56,'ABC')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    chk(56,'ABC')
TypeError: chk() takes 0 positional arguments but 2 were given
>>> def chk(name='ABC',age=10):
	name=input("Enter your name: ")
	age=int(input("Enter age: "))
	print("name: ",name)
	print("age: ",age)
	input()

	
>>> chk()
Enter your name: as
Enter age: 23
name:  as
age:  23

>>> chk(name='ABC',age=10)
Enter your name: sas
Enter age: 32
name:  sas
age:  32
