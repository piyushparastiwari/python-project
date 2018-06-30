class add:
    def __init__(self):
        super().__init__()
        print("this is init method of class one")
        self.z=self.x+self.y
        print("add: ",self.z)

class sub:
    def __init__(self):
        super().__init__()
        print("this is init method of class two")
        self.z=self.x-self.y
        print("sub: ",self.z)
        
class mul:
    def __init__(self):
        super().__init__()
        print("this is init method of class three")
        self.z=self.x*self.y
        print("mul: ",self.z)
        
class div():
    def __init__(self):
        super().__init__()
        print("this is init method of class final")
        self.z=self.x/self.y
        print("div: ",self.z)

class result(add,sub,mul,div):
    def __init__(self):
        self.x=10
        self.y=30
        super().__init__()
        print("this is init method of class final")
        
        
        
        

