class Student:
    def __init__(self,name,roll):
        print("para init called")
        self.name=name
        self.roll=roll
    def hello(self):
        print("Hello this is: ",self.name)
        print("Your roll no. is: ",self.roll)
    
