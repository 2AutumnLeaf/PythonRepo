def rem(l,word):
    n =[]
    for i in l:
        if(i != word):
            n.append(i.strip(word))
    return n

a = ["Harry","Rohan","Shubham","an"]
print(rem(a, "an"))