def check(fun):
    def checksub(x,y):
        if x<y:
            print(" x is less than y  ans is negative.....")
        fun(x,y)
        return checksub

@check
def sub(a,b):
    a=int(input(" enter the value of a:   "))
    b=int(input("enter the value of b:  "))
    z=a-b
    print("ans:  ",z)
