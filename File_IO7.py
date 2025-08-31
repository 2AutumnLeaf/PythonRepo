
with open("File5.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if ("Python" in line):
        print(f"Python is present in line no: {lineno}")
        break
    lineno += 1

else:
    print(f"Python is not present")

