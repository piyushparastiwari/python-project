Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> t1=("Hello",1,2.3)
>>> t1
('Hello', 1, 2.3)
>>> print(len(t1))
3
>>> t2=(1,2,3,4,5)
>>> t2
(1, 2, 3, 4, 5)
>>> print(max(t2))
5
>>> print(min(t2))
1
>>> print(t2[0]*t2[1]*t2[2]*t2[3]*t2[4])
120
>>> s1={1,2,3}
>>> s1
{1, 2, 3}
>>> s2={3,4,5}
>>> s2
{3, 4, 5}
>>> print(s1-s2)
{1, 2}
>>> print(s1&s2)
{3}
>>> print(s1==s2)
False
