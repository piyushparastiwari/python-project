import re

st="hello \\doggy"
print(st)

r=re.search(r'\\doggy',st)
print(r)
print(type(r))
