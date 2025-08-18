a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))
c = int(input("Enter number 3 : "))
d = int(input("Enter number 4 : "))

if(a>b):
    if(a>c):
        if (a > d):
            print(a)
        else:
            print(d)
    elif(c>d):
        print(c)
    else:
        print(d)
elif(b>c):
    if (b>d):
        print(b)
    else:
        print(d)
elif(c>d):
    print(c)
else:
    print(d)
