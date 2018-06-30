class first:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.z=0
    def add(self):
        self.z=self.x+self.y
        print("Addition is: ",self.z)
    def sub(self):
        self.z=self.x-self.y
        print("Substraction is: ",self.z)
