from abc import*
from ab1 import*
class india(tax):
    def caltax(self):
        self.gross()
        self.expense()
        self.net()
    if(self.ni<250000):
        print("no tax")
    elif(self.ni>250000 and self.ni<=500000):
        self.ni=self.ni-2500000
        print("tax ammount",self.ni*5/1000)

    elif(self.ni>500000 and self.ni<=1000000):
        self.ni=self.ni-5000000
        print("tax ammount",self.ni*20/1000)
    else:
        self.ni=self.ni-5000000
        
        print("tax ammount",self.ni*30/1000)



    
        
