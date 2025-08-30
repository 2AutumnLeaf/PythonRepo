with open("File3.txt", "r") as f:
    content = f.read()

# Replace all occurrences of "Donkey" with "#####"
content = content.replace("Donkey", "#####")
    
with open("File3.txt", "w") as f:
    f.write(content)
