Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> l=[[1,4,5,6],"hello"]
>>> l[0][1]
4
>>> l1=[4,6,5,6]
>>> l2=[5,45,65]
>>> l3=l1+l2
>>> l3
[4, 6, 5, 6, 5, 45, 65]
>>> l3.sort()
>>> l3
[4, 5, 5, 6, 6, 45, 65]
>>> t1=()
>>> t1=(1,2,3,4)
>>> t1
(1, 2, 3, 4)
>>> t1[2]
3
>>> t1[2]=10
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    t1[2]=10
TypeError: 'tuple' object does not support item assignment
>>> 
