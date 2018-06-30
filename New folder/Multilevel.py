class One:
    def __init__(self):
        super().__init__()
        print("This is init method of class One")
        self.i=5

class Two(One):
    def __init__(self):
        super().__init__()
        print("This is init method of class Two")
        self.j=10

class Three(Two):
    def __init__(self):
        super().__init__()
        print("This is init method of class Three")
        self.k=15

class Final(Three):
    def __init__(self):
        super().__init__()
        print("This is init method of class Final")
        
