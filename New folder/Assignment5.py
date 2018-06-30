Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=3
>>> if a<4:
	a=a/(a-3)
	print(a)

	
Traceback (most recent call last):
  File "<pyshell#4>", line 2, in <module>
    a=a/(a-3)
ZeroDivisionError: division by zero
>>> a=3
>>> try:
	if a<4:
		a=a/(a-3)
		print(a)
except(ZeroDivisionError):
	print("Division by zero is not possible")

	
Division by zero is not possible
>>> l=[1,2,3]
>>> print(l[3])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(l[3])
IndexError: list index out of range
>>> l=[1,2,3]
>>> try:
	print(l[3])
except(IndexError):
	print("This index is not present in list")

	
This index is not present in list
>>> try:
	raise NameError("Hi there")
except NameError:
	print "An exception"
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("An exception")?
>>> try:
	raise NameError("Hi there")
except NameError:
	print ("An exception")
	raise

An exception
Traceback (most recent call last):
  File "<pyshell#27>", line 2, in <module>
    raise NameError("Hi there")
NameError: Hi there
>>> def AbyB(a,b):
	try:
		c=((a+b)/(a-b))
	except ZeroDivisionError:
		print("a/b result in o")
	else:
		print(c)

		
>>> AbyB(2,4)
-3.0
>>> 
>>> AbyB(4,2)
3.0
>>> AbyB(2.0,3.0)
-5.0
>>> 
