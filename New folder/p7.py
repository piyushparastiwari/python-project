Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> num=5
>>> while(num>1)
SyntaxError: invalid syntax
>>> if num>1
SyntaxError: invalid syntax
>>> if num>1:
	for i in range(2,num):
		if(num%i==0):
			print("Not prime")
		else:
			print("Prime")

			
Prime
Prime
Prime
>>> if num>1:
	for i in range(2,num):
		if(num%2==0):
			print("Not prime")
		else:
			print("Prime")

			
Prime
Prime
Prime
>>> num=4
>>> if num>1:
	for i in range(2,num):
		if(num%i==0):
			print("Not prime")
		else:
			print("Prime")

			
Not prime
Prime
>>> if num>1:
	for i in range(2,num):
		if(num%2==0):
			print("Not prime")
		else:
			print("Prime")

			
Not prime
Not prime
>>> if num>1:
	for i in range(2,num):
		if(num%i==0):
			print("Not prime")
			break;
		else:
			print("Prime")

			
Not prime
>>> 
