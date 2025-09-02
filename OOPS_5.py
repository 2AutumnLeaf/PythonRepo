'''
Nothing changes if we use "slf" instead of "self"
Changing parameters

'''

from random import randint

class Train:

    def __init__(slf,traininfo):
        slf.traininfo = traininfo

    def book(slf ,fro , to):
        print(f"The train {slf.traininfo} is riding from {fro} to {to}")
        return ""
        

    def getStatus(slf):
        print(f"The train {slf.traininfo} is running on time")
        return ""

    def getFare(slf,fro ,to):
        print(f"The fare of train {slf.traininfo} running from {fro} to {to} is {randint(222,5555)}")
        return ""

a = Train(122211)
print(a.book("Kathmandu","Kolkata"))
print(a.getStatus())
print(a.getFare("Kathmandu","Kolkatalf"))