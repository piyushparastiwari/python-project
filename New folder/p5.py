Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> d={'Name':'Monika','class':10}
>>> type(d)
<class 'dict'>
>>> d
{'Name': 'Monika', 'class': 10}
>>> print("name: ",d['name'])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print("name: ",d['name'])
KeyError: 'name'
>>> print("Name: ",d['Name'])
Name:  Monika
>>> print("Class: ",d['class'])
Class:  10
>>> 
>>> d
{'Name': 'Monika', 'class': 10}
>>> d['Name']='Monika Singh'
>>> d
{'Name': 'Monika Singh', 'class': 10}
>>> del d['Name']
>>> d
{'class': 10}
>>> d.clear()
>>> d
{}
>>> del d
>>> d
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d
NameError: name 'd' is not defined
>>> d={('name','class')}
>>> d
{('name', 'class')}
>>> d={('name','class'):('Monika',10}
       
SyntaxError: invalid syntax
>>> d={('name','class'):('Monika',10)}
       
>>> d
       
{('name', 'class'): ('Monika', 10)}
>>> d={['name','class']:['Monika',10]}
       
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    d={['name','class']:['Monika',10]}
TypeError: unhashable type: 'list'
>>> d
       
{('name', 'class'): ('Monika', 10)}
>>> x=10
       
>>> if x>5:
       print("Hello")

       
Hello
>>> if x>5
       
SyntaxError: invalid syntax
>>> if x>5:
       print("x is greater than 5")
       else:
       
SyntaxError: invalid syntax
>>> if c>5:


       else
       
SyntaxError: invalid syntax
>>> if x>5:
       print("x is greater than 5")
else:
       print("x is less than 5")

       
x is greater than 5
>>> x=25
       
>>> if x>10:
       if x>20:
       print('no. is greater than 10 and 20 both')
       
SyntaxError: expected an indented block
>>> if x>10:
       if x>20:
       print('abc')
       
SyntaxError: expected an indented block
>>> if x>10:
       if x>20:
       print("Number is greater than 10 and 20")
       
SyntaxError: expected an indented block
>>> 
