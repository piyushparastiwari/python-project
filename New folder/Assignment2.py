Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> l1=['Infosys','TCS']
>>> l1
['Infosys', 'TCS']
>>> l1.append('Google','Apple')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    l1.append('Google','Apple')
TypeError: append() takes exactly one argument (2 given)
>>> l1
['Infosys', 'TCS']
>>> l1.append('Google')
>>> l1
['Infosys', 'TCS', 'Google']
>>> l1.append('Apple')
>>> l1.append('Facebook')
>>> l1.append('Microsoft')
>>> l1.append('Tesla')
>>> l1
['Infosys', 'TCS', 'Google', 'Apple', 'Facebook', 'Microsoft', 'Tesla']
>>> l2=[1,2,3,4,5]
>>> l2
[1, 2, 3, 4, 5]
>>> 
