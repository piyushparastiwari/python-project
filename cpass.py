class stu():
    def __init__(self,name="",roll_no=0,pasw=123):
        print("non parmeterized  init is called")
        self.name=input('enter the name')
        self.roll_no=int(input('enter the roll no'))
        self.pasw=input('enter the password')
    def hello(self):
        print("hello", self.name)
        print("your roll no is: ",self.roll_no)
        print("your passw: ",self.pasw)
        
    
