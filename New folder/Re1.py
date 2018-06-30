import re

st='''
        Hello Everyone
        How are you?
        bye
    '''

print(st)

s=re.compile("\n")
st=s.sub(" ",st)
print(st)
