#1
a = lambda x: x*x
print(a(6))

#2
b = ["a","v","d","c"]
final = "-".join(b)
print(final)

#3
c ="{} dsdsdsdsd {}".format("12121212","323223232")
print(c)

#4
d ="{1} dsdsdsdsd {0}".format("12121212","323223232")
print(d)

#5
e = [1, 2, 3 ,4]
square = lambda x:x*x

sqlist = map(square,e)
print(list(sqlist))

#6
list1 = filter(lambda x:x%2 == 0,e)
print(list(list1))

#7
from functools import reduce
def sum(a,b):
    return a+b

print(reduce(sum,e))