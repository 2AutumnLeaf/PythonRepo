#Add a @staticmethod in OOPS_2.py

class Calculator: #This class finds square , cube and square root of number
    def __init__(self,Num):
        self.Num = Num

    @staticmethod
    def hello():
        print("Hello!")
        return ""
    
    def square(self):
        print (f"Square =  {(self.Num)*(self.Num)}")
        print (f"Cuber = {(self.Num)*(self.Num)*(self.Num)}")
        print (f"Square Root = {float((self.Num)**((12)))}")

        return "Done"
    


p = Calculator(64)
print(p.hello())
print(p.square())
