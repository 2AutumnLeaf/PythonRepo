# 6
# Opening Multiple files 
# with (
    # open('file.txt',"r") as f1
    # open('file1.txt',"r") as f2
# )

# 7
# try | except
# try:
#     a = int(input("Enter a number : "))
#     print(a)
# except Exception as e:
#     print(e)
# except ZeroDivisionError as f:
#     print(f)
# except TypeError as b:
#     print(b)
# except :
    

# print("Thank you")

# 8
# Raising Error
# a = int(input("Enter your 1st number : "))
# b = int(input("Enter your 2nd number : "))

# if ((a == 0 or b == 0 ) or (a == 0 and b == 0) ):
#     raise ZeroDivisionError("Hey ,Our program is not meant to handle division by 0 ")
# else :
#     print(f"The division of a/b = {a/b}")



# 9
# try | else
# try :
#     a = int(input("Enter your number : "))
#     print(a)
# except Exception as e:
#     print(e)

# else:
#     print("I am inside else . If try block runs successfully you print else")

# 10
# finally: 
'''
Finally is used to print a statement wether the try block works or not
But this is useful when used in a function
''' 
# def main():
#     try :
#         a = int(input("Enter your number : "))
#         print(a)
#         return
#     except Exception as e:
#         print(e)
#         return
    
#     finally:
#         print("Finally runs Regards if try is run succesfully or not")
    
# main()