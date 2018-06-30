#Wap to replace any particular word with the word present in string.


import re

st="sat ,mat,bat,cat,hat"
a=re.findall("[smbch]",st)

print(a)
for val in a:
    print(val)
