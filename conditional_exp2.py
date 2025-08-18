a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))
c = int(input("Enter number 3 : "))
d = int(input("Enter number 4 : "))

if (a>b and a>b and a>d):
    print(f"{a} is the greatest number")
elif (b>a and b>c and d>d):
    print(f"{b} is the greatest number")
elif (c>b and c>a and c>d):
    print(f"{c} is the greatest number")
else:
    print(f"{d} is the greatest number")