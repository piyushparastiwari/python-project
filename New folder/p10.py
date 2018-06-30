Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x='abc'
>>> x=x+'ehj'
>>> x
'abcehj'
>>> x='abc'
>>> id(x)
28933376
>>> x=x+'efg'
>>> x
'abcefg'
>>> id(x)
29047616
>>> a=[1,2,3]
>>> b=a
>>> b
[1, 2, 3]
>>> b[1]=6
>>> b
[1, 6, 3]
>>> a
[1, 6, 3]
>>> c=a.copy
>>> c
<built-in method copy of list object at 0x043B38A0>
>>> c=a.copy()
>>> c
[1, 6, 3]
>>> c[2]=8
>>> c
[1, 6, 8]
>>> a
[1, 6, 3]
>>> b
[1, 6, 3]
>>> a=['a','b','c']
>>> b=[1,2,3]
>>> for i in range(len(a)):
	for j in range(len(b)):
		print("\t"+a[i],b[j])

		
	a 1
	a 2
	a 3
	b 1
	b 2
	b 3
	c 1
	c 2
	c 3
>>> a
['a', 'b', 'c']
>>> b
[1, 2, 3]
>>> a=['a','b','c']
>>> b=[1,2,3]
SyntaxError: multiple statements found while compiling a single statement
>>> a=['a','b','c']
>>> b=[1,2,3]
>>> [[i,j]for i in a for j in b]
[['a', 1], ['a', 2], ['a', 3], ['b', 1], ['b', 2], ['b', 3], ['c', 1], ['c', 2], ['c', 3]]
>>> l=['Ram','Shyam','Mohan','Sohan','Ram','Seema','Seema']
>>> l
['Ram', 'Shyam', 'Mohan', 'Sohan', 'Ram', 'Seema', 'Seema']
>>> count(l)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    count(l)
NameError: name 'count' is not defined
>>> count(l[0])
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    count(l[0])
NameError: name 'count' is not defined
>>> l.count('Ram')
2
>>> print("Ram: "+l.count('Ram'))
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print("Ram: "+l.count('Ram'))
TypeError: must be str, not int
>>> l1=l.count('Ram')
>>> print("Ram: "+l1)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print("Ram: "+l1)
TypeError: must be str, not int
>>> print("Ram: ",l.count('Ram'))
Ram:  2
>>> print("Shyam: ",l.count('Shyam'))
Shyam:  1
>>> print("Mohan: ",l.count('Mohan'))
Mohan:  1
>>> print("Sohan: ",l.count('Sohan'))
Sohan:  1
>>> print("Seema: ",l.count('Seema'))
Seema:  2
>>> l.count('Ram','Shyam')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    l.count('Ram','Shyam')
TypeError: count() takes exactly one argument (2 given)
>>> 
>>> l.count('Ram'+'Shyam')
0
>>> for i in range(len(a))
SyntaxError: invalid syntax
>>> for i in range(len(a))
SyntaxError: invalid syntax
>>> 
>>> for i in range(len(a)):
	for j in range(l.count(i))
	
SyntaxError: invalid syntax
>>> for i in range(len(a)):
	for j in range(l.count(i)):
		print(j)

		
>>> or i in range(len(a)):
	for j in range(l.count(i)):
		print(i+j)
		
SyntaxError: invalid syntax
>>> for i in range(len(a)):
	for j in range(l.count(i)):
		print(i+j)

		
>>> for i in range(len(l)):
	for j in range(l.count(i)):
		print(i+j)

		
>>> for i in range(len(l)):
	for j in range(len(l.count(i))):
		print(j)

		
Traceback (most recent call last):
  File "<pyshell#65>", line 2, in <module>
    for j in range(len(l.count(i))):
TypeError: object of type 'int' has no len()
>>> d1={('Name','Age'):(input("Enter name: "),(input("Enter age: ")}
			
SyntaxError: invalid syntax
>>> d1={('Name','Age'):(input("Enter name: "),(input("Enter age: "))}
	
SyntaxError: invalid syntax
>>> 
	
>>> d1={('Name','Age'):(input("Enter name: "),input("Enter age: ")}
	
SyntaxError: invalid syntax
>>> 
