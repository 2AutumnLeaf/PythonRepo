l = [0 , 1 , 2 , 3 , 4 , 5, 6 , 7 ]

indices = [3,5,7]
for index,item in enumerate(l):
    if index in indices :
        print(f"The item number {index} is {item}")

