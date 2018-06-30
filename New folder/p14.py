Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/Monika/AppData/Local/Programs/Python/Python36-32/Programs/Multilevel.py 
>>> ob=Final()
This is init method of class Final
>>> 
 RESTART: C:/Users/Monika/AppData/Local/Programs/Python/Python36-32/Programs/Multilevel.py 
>>> ob=Final()
This is init method of class One
This is init method of class Two
This is init method of class Three
This is init method of class Final
>>> ob.i
5
>>> ob.j
10
>>> ob.k
15
>>> 
 RESTART: C:/Users/Monika/AppData/Local/Programs/Python/Python36-32/Programs/Multilevel.py 
>>> ob=Final()
This is init method of class One
This is init method of class Two
This is init method of class Three
This is init method of class Final
>>> Final.__mro__
(<class '__main__.Final'>, <class '__main__.Three'>, <class '__main__.Two'>, <class '__main__.One'>, <class 'object'>)
>>> 
 RESTART: C:/Users/Monika/AppData/Local/Programs/Python/Python36-32/Programs/Multiple.py 
>>> ob=Final()
This is init method of class Three
This is init method of class Two
This is init method of class One
This is init method of class Final
>>> Final.__mro__
(<class '__main__.Final'>, <class '__main__.One'>, <class '__main__.Two'>, <class '__main__.Three'>, <class 'object'>)
>>> 
 RESTART: C:/Users/Monika/AppData/Local/Programs/Python/Python36-32/Programs/Multiple1.py 
>>> ob1=Maths()
Div is:  2.0
Mul is:  200
Sub is:  10
Sum is:  30
Maths class executed
>>> 
 RESTART: C:/Users/Monika/AppData/Local/Programs/Python/Python36-32/Programs/Multilevel1.py 
>>> ob2=Maths()
Sum is:  30
Sub is:  10
Mul is:  200
Div is:  2.0
Maths class executed
>>> 
 RESTART: C:/Users/Monika/AppData/Local/Programs/Python/Python36-32/Programs/Multilevel1.py 
>>> ob2=Maths()
Sum is:  30
Sub is:  10
Mul is:  200
Div is:  2.0
Maths class executed
>>> Maths.__mro__
(<class '__main__.Maths'>, <class '__main__.Div'>, <class '__main__.Mul'>, <class '__main__.Sub'>, <class '__main__.Add'>, <class 'object'>)
>>> 
 RESTART: C:/Users/Monika/AppData/Local/Programs/Python/Python36-32/Programs/Multiple1.py 
>>> ob1=Maths()
Div is:  2.0
Mul is:  200
Sub is:  10
Sum is:  30
Maths class executed
>>> Maths.__mro__
(<class '__main__.Maths'>, <class '__main__.Add'>, <class '__main__.Sub'>, <class '__main__.Mul'>, <class '__main__.Div'>, <class 'object'>)
>>> 
