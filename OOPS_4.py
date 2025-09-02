from random import randint

class Train:

    def __init__(self,traininfo):
        self.traininfo = traininfo

    def book(self ,fro , to):
        print(f"The train {self.traininfo} is riding from {fro} to {to}")
        return ""
        

    def getStatus(self):
        print(f"The train {self.traininfo} is running on time")
        return ""

    def getFare(self,fro ,to):
        print(f"The fare of train {self.traininfo} running from {fro} to {to} is {randint(222,5555)}")
        return ""

a = Train(122211)
print(a.book("Kathmandu","Kolkata"))
print(a.getStatus())
print(a.getFare("Kathmandu","Kolkata"))