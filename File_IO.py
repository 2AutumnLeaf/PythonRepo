# f = open("File.txt")
# data = f.read()
# print(data)
# f.close()

# st = "1AutumnLeaf"
# f = open("File.txt","w")
# f.write()
# f.close()

# f = open("File.txt")
# lines = f.readlines()             #Returns a list
# print(lines,type(lines))
# f.close()

# f= open("File.txt")
# line1 = f.readline()
# print(line1, type(line1))
# line2 = f.readline()
# print(line2, type(line2))
# f.close()

f = open("File.txt")
while not(line == ""):
    print(line)
    line = f.readline()


f.close()