import re

st="amit and amita belongs to same family"
for val in re.finditer("amit",st):
    print(val)
    lis=val.span()
    print(lis)
    print(type(lis))
