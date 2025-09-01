class Calculator: #This class finds square , cube and square root of number
    def __init__(self,Num):
        self.Num = Num
    
    def square(self):
        print (f"Square =  {(self.Num)*(self.Num)}")
        print (f"Cuber = {(self.Num)*(self.Num)*(self.Num)}")
        print (f"Square Root = {float((self.Num)**((12)))}")


p = Calculator(64)
print(p.square())