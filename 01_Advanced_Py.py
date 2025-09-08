# 1
#using walrus operator
# if (n := len([1, 2, 3 ,4 ]))> 3:
#     print(f"Length of the list of list is too long ({n} elements expected greater)")
    # Output : Length of the list of list is too long (4 elements expected greater)

# 2

# 2a
# Assigning types
# n : int = 5

# 2b
#Assinging Types in Function
# def sum(a : int , b : int)-> int :
    # return a+b
                            #Helps the reader to figure out function type and attribute

# 3
# from typing import List  , Union , Tuple, Dict

#list of integers
# numbers : List[int] = [1, 2, 3 ,4]

#Tuple with int and string
# numbers1 : Tuple[str,int] = ("Lockheed Martin", 99)

#Dictionary with key and value pair
# numbers2: Dict[str,int] = {"A": 10, "B" : 1}

#Union type can hold multiple types of values
# Identifier : Union[str,int] = "10123"
# Identifier = 12345 #Also Valid

# 4
# Match Case
# def https_status(status):
    # match status:
        # case 200:
            # return "OK"
        # case 404:
            # return "Nor found"
        # case 500:
            # return "Internal Server Error"
        # case _:
            # return "Unknown Status"
# 
# print(https_status(200))


# 5
# Merged Dictionary
# a = {"z" : 1}
# b = {"b" : 10}
# merged = a|b
# print(merged)
