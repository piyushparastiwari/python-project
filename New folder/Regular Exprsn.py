import re

name='''
                Rahul is 25 and Sohan is 27
                Mohan is 29 and Seema is 29
           '''
age=re.findall(r'\d{1,3}',name)
names=re.findall(r'[A-Z][a-z]*',name)

Dict={}
x=0
for val in names:
    Dict[val]=age[x]
    x+=1
print(Dict)
    
