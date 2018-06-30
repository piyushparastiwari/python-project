class Student:
    def __init__(self):
        self.name=input("Enter your name : ")
        self.roll_no=int(input("Enter your roll no. : "))
        self.__pasw=input("Enter your password : ")
    def hello(self):
        print("Hello this is: ",self.name)
        print("Your roll no. is: ",self.roll_no)
        print("Your password is: ",self.__pasw)
