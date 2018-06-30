Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> r=input("enter radius: ")
enter radius: 2
>>> p=3.14
>>> type(r)
<class 'str'>
>>> r=int(input("Enter radius: "))
Enter radius: 2
>>> type(p)
<class 'float'>
>>> a=p*r*r
>>> print(a)
12.56
>>> x="meaning"
>>> x
'meaning'
>>> y="word"
>>> x
'meaning'
>>> x+y
'meaningword'
>>> z=56
>>> x
'meaning'
>>> x+y+z
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x+y+z
TypeError: must be str, not int
>>> x+y+str(z)
'meaningword56'
>>> x[2]
'a'
>>> x[2]='A'
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    x[2]='A'
TypeError: 'str' object does not support item assignment
>>> len(x)
7
>>> x
'meaning'
>>> x.upper()
'MEANING'
>>> x
'meaning'
>>> x.lower()
'meaning'
>>> x.isalpha()
True
>>> x="abc2"
>>> x.isalpha()
False
>>> x="abc@"
>>> x.isalpha()
False
>>> x.isnumeric()
False
>>> x="abc3"
>>> x.isnumeric
<built-in method isnumeric of str object at 0x03C315E0>
>>> x.isnumeric()
False
>>> x.isalnum()
True
>>> x=" "
>>> x.isspace
<built-in method isspace of str object at 0x03239A80>
>>> x.isspace()
True
>>> name="Monika"
>>> name="My name is Monika"
>>> name
'My name is Monika'
>>> age="My age is 23"
>>> x=name+age
>>> x
'My name is MonikaMy age is 23'
>>> name="My name is Monika and "
>>> x=name+age
>>> x
'My name is Monika and My age is 23'
>>> x="companies"
>>> x.startswith('c)
		 
SyntaxError: EOL while scanning string literal
>>> x.startwith('c')
		 
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    x.startwith('c')
AttributeError: 'str' object has no attribute 'startwith'
>>> x
		 
'companies'
>>> x.startswith('c')
		 
True
>>> x.endswith('e')
		 
False
>>> x.replace('m','M')
		 
'coMpanies'
>>> x="compamies"
		 
>>> x.replace('m','M')
		 
'coMpaMies'
>>> x="My name is Monika"
		 
>>> x.split(',')
		 
['My name is Monika']
>>> x.split(' ')
		 
['My', 'name', 'is', 'Monika']
>>> x
		 
'My name is Monika'
>>> x.split(' ')
		 
['My', 'name', 'is', 'Monika']
>>> x="companies"
		 
>>> x[o;]
		 
SyntaxError: invalid syntax
>>> x[0:]
		 
'companies'
>>> x[2:]
		 
'mpanies'
>>> x[2:6]
		 
'mpan'
>>> x[:6]
		 
'compan'
>>> x[::1]
		 
'companies'
>>> x[::2]
		 
'cmais'
>>> x[-1:]
		 
's'
>>> x[-6:]
		 
'panies'
>>> x[-9:]
		 
'companies'
>>> x[:-9]
		 
''
>>> x[::-1]
		 
'seinapmoc'
>>> x[:0]
		 
''
>>> x[:9]
		 
'companies'
>>> x[:-1]
		 
'companie'
>>> x[::-1]
		 
'seinapmoc'
>>> x[:1]
		 
'c'
>>> x[:9::1]
		 
SyntaxError: invalid syntax
>>> x[:9:1]
		 
'companies'
>>> x="My name is Monika"
		 
>>> x.find('n')
		 
3
>>> x="Monika"
		 
>>> x.find('n')
		 
2
>>> l1=[1,2,3,4,5]
		 
>>> l1
		 
[1, 2, 3, 4, 5]
>>> l2=[3,4,5]
		 
>>> type(l1)
		 
<class 'list'>
>>> type(l1==l2)
		 
<class 'bool'>
>>> print(l1==l2)
		 
False
>>> l1=[]
		 
>>> type(l1)
		 
<class 'list'>
>>> l2=list()
		 
>>> type(l2)
		 
<class 'list'>
>>> print(l1==l2)
		 
True
>>> f=['mango','apple','grapes']
		 
>>> f
		 
['mango', 'apple', 'grapes']
>>> type(f)
		 
<class 'list'>
>>> l1=['S1','S2','S3']
		 
>>> l1
		 
['S1', 'S2', 'S3']
>>> l1['S1','S2','S3','S4','S5']
		 
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    l1['S1','S2','S3','S4','S5']
TypeError: list indices must be integers or slices, not tuple
>>> l1=['S1','S2','S3','S4','S5']
		 
>>> l1
		 
['S1', 'S2', 'S3', 'S4', 'S5']
>>> x=[32,23,33,43]
		 
>>> x[2]
		 
33
>>> x[2]=45
		 
>>> x
		 
[32, 23, 45, 43]
>>> print(map(int,input().split()))
		 
print(map(int,input().split()))
<map object at 0x03C31B50>
>>> l1[2]='S6'
		 
>>> l1
		 
['S1', 'S2', 'S6', 'S4', 'S5']
>>> l3=list(map(int,input().split()))
		 
45,54,55,43,45
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    l3=list(map(int,input().split()))
ValueError: invalid literal for int() with base 10: '45,54,55,43,45'
>>> l3=list(map(int,input().split()))
		 
45 54 55 43 45
>>> l3
		 
[45, 54, 55, 43, 45]
>>> l4=ist(map(float,input().split()))
		 
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    l4=ist(map(float,input().split()))
NameError: name 'ist' is not defined
>>> l4=list(map(float,input().split()))
		 
55 67 77 65 55
>>> l4
		 
[55.0, 67.0, 77.0, 65.0, 55.0]
>>> f.append('banana')
		 
>>> f
		 
['mango', 'apple', 'grapes', 'banana']
>>> f.index('apple')
		 
1
>>> f.append('grapes')
		 
>>> f
		 
['mango', 'apple', 'grapes', 'banana', 'grapes']
>>> f.index('grapes')
		 
2
>>> f.index('grapes',2)
		 
2
>>> f.pop()
		 
'grapes'
>>> f
		 
['mango', 'apple', 'grapes', 'banana']
>>> 
