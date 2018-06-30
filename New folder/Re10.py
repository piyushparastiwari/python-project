import re

st="sat ,mat,bat,cat,hat"
a=re.findall("[abz]at",st)
print(a)
for val in a:
    print(val)
