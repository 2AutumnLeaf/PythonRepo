class Programmer:
    company = "Micorsoft"
    def __init__(self,name,salary,pin):
        self.name = name 
        self.salary = salary 
        self.pin = pin 
    
    def getInfo(self):
        print(f"Comapny : {self.company}\nName : {self.name}\nSalary : {self.salary}\nPIN : {self.pin}")

        return " "

p = Programmer("Manmeet",999999999999999999999,357499)
print(p.getInfo())