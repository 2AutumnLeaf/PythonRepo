word = ["Donkey", "Bad","Nice"]

with open("File4.txt","r") as f:
    content = f.read()

for words in word:
    content = content.replace(words, "#" * len(words))

with open("File4.txt","w") as f:
    f.write(content)