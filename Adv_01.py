try:
    with open("110file.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("11file.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("12file.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)


print("Please open an already existing file. Thank You!")