import re

st="sat ,mat,bat,cat,hat"
a=re.findall("[m-s]at",st)
print(a)
for val in a:
    print(val)
