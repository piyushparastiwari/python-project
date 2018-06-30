class Add:
    def __init__(self):
        super ().__init__()
        a=20
        b=10
        sum=a+b
        print("Sum is: ",sum)

class Sub(Add):
    def __init__(self):
        super ().__init__()
        a=20
        b=10
        sub=a-b
        print("Sub is: ",sub)

class Mul(Sub):
    def __init__(self):
        super ().__init__()
        a=20
        b=10
        mul=a*b
        print("Mul is: ",mul)

class Div(Mul):
    def __init__(self):
        super ().__init__()
        a=20
        b=10
        div=a/b
        print("Div is: ",div)

class Maths(Div):
    def __init__(self):
        super ().__init__()
        print("Maths class executed")
        
