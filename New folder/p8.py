Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=20
>>> b=3
>>> b=30
>>> def addition(a,b):
	addition=a+b
	print("Answer is: ",addition)
	return addition

>>> addition(a,b)
Answer is:  50
50
>>> def addition(a,b):
	addition=a+b
	print("Answer is: ",addition)

	
>>> addition(20,30)
Answer is:  50
>>> def addition(a,b):
	addition=a+b
	print("Answer is: ",addition)

	
>>> addition(a,b)
Answer is:  50
>>> a=int(input("enter a: "))
enter a: 40
>>> b=int(input("enter b: "))
enter b: 30
>>> addition(a,b)
Answer is:  70
>>> a=50
>>> l=[50,60,70]
>>> def check(l):
	l.append([11,12,13])
	print("Values are: ",l)
	return

>>> check(l)
Values are:  [50, 60, 70, [11, 12, 13]]
>>> def chk():
	name=input("Enter your name: ")
	age=int(input("Enter age: "))
	print("name: ",name)
	print("age: ",age)
input()
SyntaxError: invalid syntax
>>> def chk():
	name=input("Enter your name: ")
	age=int(input("Enter age: "))
	print("name: ",name)
	print("age: ",age)
	input()
	chk()

	
>>> chk()
Enter your name: Monika
Enter age: 23
name:  Monika
age:  23

Enter your name: sdsds
Enter age: 43
name:  sdsds
age:  43

Enter your name: 
