Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import math
>>> x=4.5
>>> math.ceil(x)
5
>>> math.floor(x)
4
>>> math.cos(x)
-0.2107957994307797
>>> math.sin(x)
-0.977530117665097
>>> math.tan(x)
4.637332054551185
>>> 
>>> math.degrees(x)
257.8310078088705
>>> math.radians(x)
0.07853981633974483
>>> x=5
>>> math.factorial(x)
120
>>> math.gcd(50,70)
10
>>> math.pow(3,4)
81.0
>>> print(math.pi)
3.141592653589793
>>> import os
>>> os.name
'nt'
>>> os.path.abspath('.')
'C:\\Users\\Monika\\AppData\\Local\\Programs\\Python\\Python36-32'
>>> os.listdir('.')
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'Programs', 'python.exe', 'python3.dll', 'python36.dll', 'pythonw.exe', 'Scripts', 'tcl', 'Tools', 'vcruntime140.dll']
>>> import datetime
>>> datetime.today()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    datetime.today()
AttributeError: module 'datetime' has no attribute 'today'
>>> dir(datetime)
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']
>>> datetime.time()
datetime.time(0, 0)
>>> datetime.date(2000,12,1)
datetime.date(2000, 12, 1)
>>> import time
>>> time.time()
1528782608.6723456
>>> time.time()
1528782620.1257682
>>> time.sleep(1)

>>> time.sleep(5)
>>> time.clock()
2.5659250288025083e-06
>>> time.localtime(time.time)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    time.localtime(time.time)
TypeError: an integer is required (got type builtin_function_or_method)
>>> time.localtime(time.time())
time.struct_time(tm_year=2018, tm_mon=6, tm_mday=12, tm_hour=11, tm_min=23, tm_sec=27, tm_wday=1, tm_yday=163, tm_isdst=0)
>>> time.strftime("%H:%M:%S")
'11:27:21'
>>> 
