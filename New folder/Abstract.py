from abc import *
class Tax(ABC):
    def __init__(self):
        self.gi=0
        self.ge=0
        self.ni=0
    def gross(self):
        self.gi=float(input("Enter your gross income: "))
    def expense(self):
        self.ge=float(input("Enter your gross expense: "))
    def net(self):
        self.ne=self.gi-self.ge
        print("Your net income is: ",self.ni)

    @abstractmethod
    def calTax(self):
        pass
