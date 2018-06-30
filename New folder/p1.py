Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("Hello World")
Hello World
>>> print(4)
4
>>> print("\n\tMonika")

	Monika
>>> print("\tMonika"*5)
	Monika	Monika	Monika	Monika	Monika
>>> print("'Monika'")
'Monika'
>>> print("I dont want to go outside")
I dont want to go outside
>>> print("My name is "Monika"")
SyntaxError: invalid syntax
>>> print("My name is \Monika\")
	  
SyntaxError: EOL while scanning string literal
>>> print("My name is \Monika\ ")
	  
My name is \Monika\ 
>>> print("My name is \"Monika\"")
	  
My name is "Monika"
>>> print("My name is \\Monika\\")
	  
My name is \Monika\
>>> print("My name is \Smonika\ ")
	  
My name is \Smonika\ 
>>> print("my name is \tx\ ")
	  
my name is 	x\ 
>>> print("my name is \Monkia")
	  
my name is \Monkia
>>> print("my Name is \"X ")
	  
my Name is "X 
>>> print('"Monika"')
	  
"Monika"
>>> print("My name is \"Monika\"")
	  
My name is "Monika"
>>> print("Monika",sep=',')
	  
Monika
>>> print("Monika"*5,sep=',')
	  
MonikaMonikaMonikaMonikaMonika
>>> print("Monika",end="!!")
	  
Monika!!
>>> print("My name is Monika***")
	  
My name is Monika***
>>> print("My name is Monika ***")
	  
My name is Monika ***
>>> print("My name is Monika",end="***")
	  
My name is Monika***
>>> print(1,2,3)
	  
1 2 3
>>> print(111,222,333,sep='%')
	  
111%222%333
>>> print(1,2,3,sep=',',end='!!')
	  
1,2,3!!
>>> input("Monika")
	  
Monika
''
>>> input("enter any number: ")
	  
enter any number: 6
'6'
>>> x=input("Enter any number: ")
	  
Enter any number: 5
>>> print(x)
	  
5
>>> type(x)
	  
<class 'str'>
>>> y=input("enter another number: ")
	  
enter another number: 3
>>> z=x+y
	  
>>> print(z)
	  
53
>>> type(z)
	  
<class 'str'>
>>> x=input("enter any number: ")
	  
enter any number: 56
>>> y=int(input("Enter your number: "))
	  
Enter your number: 45
>>> type(x)
	  
<class 'str'>
>>> type(y)
	  
<class 'int'>
>>> z=int(input("Enter scnd no: "))
	  
Enter scnd no: 33
>>> y+z
	  
78
>>> type(z)
	  
<class 'int'>
>>> x=2
	  
>>> x=3
	  
>>> print(x)
	  
3
>>> 
