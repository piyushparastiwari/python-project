try:
    x=int(input("Enter your first num: "))
    y=int(input("Enter your second num: "))
    z=x/y
    print("Answer: ",z)
    try:
        a=x*y
        print("a: ",a)
    finally:
        print("All the statements has been printed")
except(ZeroDivisionError):
    print("You are dividing any no. with 0")
except(ValueError,NameError):
    print("Take care of your errors")
    
