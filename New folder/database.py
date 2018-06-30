Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import MySQLdb
>>> #1. Connection creatio
>>> #1. Connection creation
>>> db=MYSQLdb.connect("localhost","monika","rootroot","lpu")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    db=MYSQLdb.connect("localhost","monika","rootroot","lpu")
NameError: name 'MYSQLdb' is not defined
>>> db=MySQLdb.connect("localhost","monika","rootroot","lpu")
>>> cursor=db.cursor()
>>> cursor.execute("create table mytable(name varchar(30),age int,salary int)")
0
>>> cursor.execute("insert into mytable values('one,45,60000)")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    cursor.execute("insert into mytable values('one,45,60000)")
  File "C:\Python36\lib\site-packages\MySQLdb\cursors.py", line 250, in execute
    self.errorhandler(self, exc, value)
  File "C:\Python36\lib\site-packages\MySQLdb\connections.py", line 50, in defaulterrorhandler
    raise errorvalue
  File "C:\Python36\lib\site-packages\MySQLdb\cursors.py", line 247, in execute
    res = self._query(query)
  File "C:\Python36\lib\site-packages\MySQLdb\cursors.py", line 411, in _query
    rowcount = self._do_query(q)
  File "C:\Python36\lib\site-packages\MySQLdb\cursors.py", line 374, in _do_query
    db.query(q)
  File "C:\Python36\lib\site-packages\MySQLdb\connections.py", line 277, in query
    _mysql.connection.query(self, query)
_mysql_exceptions.ProgrammingError: (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''one,45,60000)' at line 1")
>>> cursor.execute("insert into mytable values('one',45,60000)")
1
>>> db.commit()
>>> cursor.execute("insert into mytable(name,salary,age) values('one',45,60000)")
1
>>> cursor.execute("insert into mytable(name,salary,age) values('one',60000,45)")
1
>>> db.commit()
>>> cursor.execute("select * from mytable")
3
>>> for rows in cursor:
	print("name: ",row[0],"age: ",rows[1], "salary: ",rows[2])

	
Traceback (most recent call last):
  File "<pyshell#16>", line 2, in <module>
    print("name: ",row[0],"age: ",rows[1], "salary: ",rows[2])
NameError: name 'row' is not defined
>>> for rows in cursor:
	print("name: ",rows[0],"age: ",rows[1], "salary: ",rows[2])

	
name:  one age:  45 salary:  60000
name:  one age:  60000 salary:  45
name:  one age:  45 salary:  60000
>>> cursor.execute("select * from mytable")
3
>>> db.close()
>>> import MySQLdb
>>> db=MYSQLdb.connect("localhost","monika","rootroot","lpu")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    db=MYSQLdb.connect("localhost","monika","rootroot","lpu")
NameError: name 'MYSQLdb' is not defined
>>> db=MySQLdb.connect("localhost","monika","rootroot","lpu")
>>> cursor=db.cursor()
>>> cursor.execute("select * from mytable")
3
>>> for rows in cursor:
	print("name: ",rows[0],"age: ",rows[1], "salary: ",rows[2])

	
name:  one age:  45 salary:  60000
name:  one age:  60000 salary:  45
name:  one age:  45 salary:  60000
>>> cursor.execute("select * from mytable where salary<25000")
1
>>> for rows in cursor:
	print("name: ",rows[0],"age: ",rows[1], "salary: ",rows[2])

	
name:  one age:  60000 salary:  45
>>> cursor.execute("insert into mytable values('three',20,30000)")
1
>>> db.commit()
>>> cursor.execute("select * from mytable where salary<25000")
1
>>> for rows in cursor:
	print("name: ",rows[0],"age: ",rows[1], "salary: ",rows[2])

	
name:  one age:  60000 salary:  45
>>> cursor.execute("insert into mytable values('three',20,30000)")
1
>>> db.commit()
>>> cursor.execute("select * from mytable")
5
>>> db.commit()
>>> cursor.execute("select * from mytable where salary<25000")
1
>>> for rows in cursor:
	print("name: ",rows[0],"age: ",rows[1], "salary: ",rows[2])

	
name:  one age:  60000 salary:  45
>>> cursor.execute("select * from mytable where salary<45000")
3
>>> for rows in cursor:
	print("name: ",rows[0],"age: ",rows[1], "salary: ",rows[2])

	
name:  one age:  60000 salary:  45
name:  three age:  20 salary:  30000
name:  three age:  20 salary:  30000
>>> cursor.execute("drop table mytable")
0
>>> cursor.execute("select * from mytable")
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    cursor.execute("select * from mytable")
  File "C:\Python36\lib\site-packages\MySQLdb\cursors.py", line 250, in execute
    self.errorhandler(self, exc, value)
  File "C:\Python36\lib\site-packages\MySQLdb\connections.py", line 50, in defaulterrorhandler
    raise errorvalue
  File "C:\Python36\lib\site-packages\MySQLdb\cursors.py", line 247, in execute
    res = self._query(query)
  File "C:\Python36\lib\site-packages\MySQLdb\cursors.py", line 411, in _query
    rowcount = self._do_query(q)
  File "C:\Python36\lib\site-packages\MySQLdb\cursors.py", line 374, in _do_query
    db.query(q)
  File "C:\Python36\lib\site-packages\MySQLdb\connections.py", line 277, in query
    _mysql.connection.query(self, query)
_mysql_exceptions.ProgrammingError: (1146, "Table 'lpu.mytable' doesn't exist")
>>> delete from mytable where salary>60000
SyntaxError: invalid syntax
>>> 
