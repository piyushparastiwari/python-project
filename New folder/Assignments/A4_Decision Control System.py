Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> year=2016
>>> if year%4==0 and year%100!=0:
	if year%400==0:
		print("It is a leap year")
	else:
		print("It is not a leap year")

		
It is not a leap year
>>> if year%4==0 and year%100!=0:
	if year%400!=0:
		print("It is a leap year")
	else:
		print("It is not a leap year")

		
It is a leap year
>>> l=int(input("Enter length: "))
Enter length: 2
>>> b=int(input("Enter breadth: "))
Enter breadth: 4
>>> if(l==b):
	print("It is a square")
else:
	print("It is a rectangle")

	
It is a rectangle
>>> a=20
>>> b=30
>>> c=10
>>> if a>b and a>c:
	print("a is oldest")
elif:
	
SyntaxError: invalid syntax
>>> if a>b and a>c:
	print("a is oldest")
elif a<b and a<c:
	print("a is youngest")
elif b>a and b>c:
	print("b is oldest")
elif b<a and b<c:
	print("b is youngest")
elif c>a and c>b:
	print("c is oldest")
	else:
		
SyntaxError: invalid syntax
>>> if a>b and a>c:
	print("a is oldest")
elif a<b and a<c:
	print("a is youngest")
elif b>a and b>c:
	print("b is oldest")
elif b<a and b<c:
	print("b is youngest")
elif c>a and c>b:
	print("c is oldest")
else:
	print("c is youngest")

	
b is oldest
>>> 
