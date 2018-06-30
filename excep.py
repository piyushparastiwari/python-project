try:
    a=3
    if a<4:
        b=a/(a-3)
        print(b)
except(ZeroDivisionError):
    print("dividing num by 0: " )
