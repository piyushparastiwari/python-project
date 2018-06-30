Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> try:
	x=int(input())
except Exception as Ex:
	print(Ex.__class__.__name__,Ex)

	
a
ValueError invalid literal for int() with base 10: 'a'
>>> try:
	raise ZeroDivisionError
except Exception as Ex:
	print(Ex.__class__.__name__)

	
ZeroDivisionError
>>> try:
	raise ZeroDivisionError
except Exception as Ex:
	print(Ex.__class__.__name__,Ex)

	
ZeroDivisionError 
>>> try:
	raise ZeroDivisionError("arguments")
except Exception as Ex:
	print(Ex.__class__.__name__,Ex.args)

	
ZeroDivisionError ('arguments',)
>>> class Gen(Exception):
	def __init__(self,message):
		self.message=message
		print("Creating generic exception ",message)
	def iferror(self):
		print("iferror: ",self.message)

		
>>> try:
	x=30
	if x>40:
		raise Gen("Condition not satisfied")
except Gen as g:
	print("Exception here caught by Gen: ",g)

	
>>> try:
	x=30
	if x>40:
		raise Gen("Condition not satisfied")
except Gen as g:
	print("Exception here caught by Gen: ",g)
	g.iferror()

	
>>> try:
	x=30
	if x<40:
		raise Gen("Condition not satisfied")
except Gen as g:
	print("Exception here caught by Gen: ",g)
	g.iferror()

	
Creating generic exception  Condition not satisfied
Exception here caught by Gen:  Condition not satisfied
iferror:  Condition not satisfied
>>> try:
	x=30
	if x<40:
		raise Gen("Condition satisfied")
except Gen as g:
	print("Exception here caught by Gen: ",g)
	g.iferror()

	
Creating generic exception  Condition satisfied
Exception here caught by Gen:  Condition satisfied
iferror:  Condition satisfied
>>> class Gen(Exception):
	def __init__(self,message):
		self.message=message
		print("Creating generic exception ",message)
	def iferror(self):
		print("iferror: ",self.message)
try:
	
SyntaxError: invalid syntax
>>> class Gen(Exception):
	def __init__(self,message):
		self.message=message
		print("Creating generic exception ",message)
	def iferror(self):
		print("iferror: ",self.message)try:
			
SyntaxError: invalid syntax
>>> class Gen(Exception):
	def __init__(self,message):
		self.message=message
		print("Creating generic exception ",message)
	def iferror(self):
		print("iferror: ",self.message)
	tr:
		
SyntaxError: invalid syntax
>>> class Gen(Exception):
	def __init__(self,message):
		self.message=message
		print("Creating generic exception ",message)
	def iferror(self):
		print("iferror: ",self.message)
	try:
		x=30
		if x<40:
			raise Gen("Condition satisfied")
	except Gen as g:
		print("Exception here caught by Gen: ",g)
		g.iferror()

		
Creating generic exception  Condition satisfied
Exception here caught by Gen:  Condition satisfied
iferror:  Condition satisfied
>>> 
 RESTART: C:/Users/Monika/AppData/Local/Programs/Python/Python36-32/Programs/student.py 
>>> monika=Student()
Enter your name : Monika
Enter your roll no. : 1
>>> monika.hello()
Hello this is:  Monika
Your roll no. is:  1
>>> 
 RESTART: C:/Users/Monika/AppData/Local/Programs/Python/Python36-32/Programs/student1.py 
>>> monika=Student()
>>> monika.hello()
Hello this is Monika
Your roll no. is: 1
>>> 
 RESTART: C:/Users/Monika/AppData/Local/Programs/Python/Python36-32/Programs/student2.py 
>>> monika=Student("Monika",1)
para init called
>>> monika.hello()
Hello this is:  Monika
Your roll no. is:  1
>>> 
 RESTART: C:/Users/Monika/AppData/Local/Programs/Python/Python36-32/Programs/student3.py 
>>> monika=Student("Monika",3)
para init called
>>> monika.hello()
Hello this is:  Monika
Your roll no. is:  3
>>> monika=Student("Monika")
para init called
>>> monika.hello()
Hello this is:  Monika
Your roll no. is:  2
>>> 
 RESTART: C:/Users/Monika/AppData/Local/Programs/Python/Python36-32/Programs/private.py 
>>> monika=Student()
Enter your name : Monika
Enter your roll no. : 1
Enter your password : "abcd"
>>> monika.hello()
Hello this is:  Monika
Your roll no. is:  1
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    monika.hello()
  File "C:/Users/Monika/AppData/Local/Programs/Python/Python36-32/Programs/private.py", line 9, in hello
    print("Your roll no. is: ",self.pasw)
AttributeError: 'Student' object has no attribute 'pasw'
>>> 
 RESTART: C:/Users/Monika/AppData/Local/Programs/Python/Python36-32/Programs/private.py 
>>> monika=Student()
Enter your name : Monika
Enter your roll no. : 1
Enter your password : monikasingh
>>> monika.hello()
Hello this is:  Monika
Your roll no. is:  1
Your roll no. is:  monikasingh
>>> monika.name="Monika Singh"
>>> monika.hello()
Hello this is:  Monika Singh
Your roll no. is:  1
Your roll no. is:  monikasingh
>>> monika.__pasw="password"
>>> monika.hello()
Hello this is:  Monika Singh
Your roll no. is:  1
Your roll no. is:  monikasingh
>>> 
 RESTART: C:/Users/Monika/AppData/Local/Programs/Python/Python36-32/Programs/private.py 
>>> monika=Student()
Enter your name : ABC
Enter your roll no. : 4
Enter your password : abcde123
>>> monika.hello()
Hello this is:  ABC
Your roll no. is:  4
Your password is:  abcde123
>>> monika.__pasw="password"
>>> monika.hello()
Hello this is:  ABC
Your roll no. is:  4
Your password is:  abcde123
>>> 
 RESTART: C:/Users/Monika/AppData/Local/Programs/Python/Python36-32/Programs/student4.py 
>>> cal=Student1()
>>> cal.hello()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    cal.hello()
AttributeError: 'Student1' object has no attribute 'hello'
>>> cal=Student1()
>>> cal.result()
Sum is:  30
Sub is:  -10
>>> 
 RESTART: C:/Users/Monika/AppData/Local/Programs/Python/Python36-32/Programs/student5.py 
>>> stud=Student()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    stud=Student()
NameError: name 'Student' is not defined
>>> stud=first()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    stud=first()
TypeError: __init__() missing 2 required positional arguments: 'x' and 'y'
>>> stud=first(6,3)
>>> stud.add()
Addition is:  9
>>> stud.sub()
Substraction is:  3
>>> 
 RESTART: C:/Users/Monika/AppData/Local/Programs/Python/Python36-32/Programs/Inheritance.py 
Traceback (most recent call last):
  File "C:/Users/Monika/AppData/Local/Programs/Python/Python36-32/Programs/Inheritance.py", line 1, in <module>
    from first import *
ModuleNotFoundError: No module named 'first'
>>> 
 RESTART: C:/Users/Monika/AppData/Local/Programs/Python/Python36-32/Programs/Inheritance.py 
>>> monika=Second(5,4)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    monika=Second(5,4)
TypeError: object() takes no parameters
>>> 
