message = input("Enter you message : \n")
a1 = "Make a lot of money"
a2 = "buy now"
a3 = "subscribe this"
a4 = "click this"

if ((a1 in message) or (a2 in message) or (a3 in message) or (a3 in message)):
    print("SPAM ALERT!")
else:
    print("Nothing to worry about")