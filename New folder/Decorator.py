def check(fun):
    def checksub(x,y):
        if x<y:
            print("x is less than y.. answer can be negative...")
        fun(x,y)
    return checksub

@check
def sub(a,b):
    z=a-b
    print("answer: ",z)
    
