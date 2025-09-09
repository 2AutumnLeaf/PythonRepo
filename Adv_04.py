
try: 
    a : int = 5
    b : int = 0
    print(a/b)
except ZeroDivisionError as v:
    print("Infinite")

print("PLease type a number other than 0.Thank you!")
