'''
n = 3

***     3
**      2
*       1
'''

def starpatt(n):
    if n == 1:
        return "*"
    print("*"*n)
    return starpatt(n-1)

n = int(input("Enter your number: "))
print(starpatt(n))