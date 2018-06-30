from  abc import *
from Abstract import *
class India(Tax):
    def calTax(self):
        self.gross()
        self.expense()
        self.net()

        if self.ni<=250000:
            print("Your tax amount is zero")
        elif self.ni>250000 and self.ni<=500000:
            self.ni=self.ni-250000
            print("Your tax amount is: ",self.ni*5/100)
        elif self.ni>500000 and self.ni<=1000000:
            self.ni=self.ni-250000
            print("Your tax amount is: ",self.ni*20/100)
        else:
            self.ni=self.ni-250000
            print("Your tax amount is: ",self.ni*30/100)
            

        
