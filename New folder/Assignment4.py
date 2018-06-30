Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x=6
>>> if x%2==0:
	print("Even no.")
else:
	print("Odd no.")

	
Even no.
>>> age=30
>>> gender='Male'
>>> sal=60000
>>> if age>30:
elif gender=='Male':
	
SyntaxError: expected an indented block
>>> if age>30:
	if gender=='Male':
		if sal>50000:
			print("Person is eligible for policy")
else:
	print("Not eligible")

	
Not eligible
>>> marks=80
>>> if marks>=90:
	print("A+")
elif marks>=80:
	print("A")
elif marks>=70:
	print("B")
elif marks>=60:
	print("C")
elif marks>=50:
	print("D")
elif marks>=40:
	print("E")
else:
	print("F")

	
A
>>> year=2016
>>> if year%4==0:
	if year%100==0:
		print("Leap year")
else:
	print("Not leap year")

	
>>> year
2016
>>> if year%4==0:
	print("Leap year")
else:
	print("Not leap year")

	
Leap year
>>> l=10
>>> b=5
>>> if age>25:
	if gender=='Male':
		if sal>50000:
			print("Person is eligible for policy")
else:
	print("Not eligible")

	
Person is eligible for policy
>>> l=10
>>> b=5
>>> if l==b
SyntaxError: invalid syntax
>>> if l==b:
	print("It is a square")
else:
	print("It is a rectangle")

	
It is a rectangle
>>> age1=20
>>> age2=10
>>> age3=30
>>> if age1>age2:
	if age1>age3:
		print("age1 is oldest")
	else:
		print("age1 is youngest")
if age2>age1:
	
SyntaxError: invalid syntax
>>> if age1>age2:
	if age1>age3:
		print("age1 is oldest")
	else:
		print("age1 is youngest")
	if age2>age1:
		if age2>age3:
			print("age2 is oldest")
		else:
			print("age2 is younger")
		if age3>age1:
			print("age3 is oldest")
		else:
			print("age3 is youngest")

			
age1 is youngest
>>> if age1>age2 && age1>age3:
	
SyntaxError: invalid syntax
>>> if age1>age2 and age1>age3:
	print("age1 is oldest")
	else:
		
SyntaxError: invalid syntax
>>> if age1>age2 and age1>age3:
	print("age1 is oldest")
else:
	print("age1 is youngest")
	if age2>age1 and age2>age3:
			print("age2 is oldest")
		else:
			print("age2 is younger")
		if age3>age1 and age3>age2
			print("age3 is oldest")
		else:
			print("age3 is youngest")
			
SyntaxError: unindent does not match any outer indentation level
>>> if age1>age2 and age1>age3:
	print("age1 is oldest")
else:
	print("age1 is youngest")
	if age2>age1 and age2>age3:
			print("age2 is oldest")
	else:
			print("age2 is younger")
		if age3>age1 and age3>age2
			print("age3 is oldest")
		else:
			print("age3 is youngest")
			
SyntaxError: unindent does not match any outer indentation level
>>> if age1>age2 and age1>age3:
	print("age1 is oldest")
else:
	print("age1 is youngest")
	if age2>age1 and age2>age3:
			print("age2 is oldest")
	else:
			print("age2 is younger")
		if age3>age1 and age3>age2:
			print("age3 is oldest")
		else:
			print("age3 is youngest")
			
SyntaxError: unindent does not match any outer indentation level
>>> if age1>age2 and age1>age3:
	print("age1 is oldest")
else:
	print("age1 is youngest")
	if age2>age1 and age2>age3:
		print("age2 is oldest")
	else:
		print("age2 is younger")
			if age3>age1 and age3>age2:
				print("age3 is oldest")
			else:
				print("age3 is youngest")
				
SyntaxError: unexpected indent
>>> if age1>age2 and age1>age3:
	print("age1 is oldest")
else:
	print("age1 is youngest")
	if age2>age1 and age2>age3:
		print("age2 is oldest")
	else:
		print("age2 is younger")
		if age3>age1 and age3>age2:
			print("age3 is oldest")
		else:
			print("age3 is youngest")

			
age1 is youngest
age2 is younger
age3 is oldest
>>> 
