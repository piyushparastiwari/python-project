class Student:
    def __init__(self,name="",roll=2):
        print("para init called")
        self.name=name
        self.roll_no=roll
    def hello(self):
        print("Hello this is: ",self.name)
        print("Your roll no. is: ",self.roll_no)
    
