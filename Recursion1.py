def sum_of_n(n):
    if n==1:
        return 1
    b = n +(sum_of_n(n-1))
    return b

n = int(input("Enter your number: "))
a = sum_of_n(n)
print(f"The sum of natural numbers til {n} is {a}")