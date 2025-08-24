import random 

computer = random.choice([1 , 0 , -1])
n = int(input("Enter your number : "))
your_choice = [1 , 0 , -1]
values = {
    "R" : 1,
    "P" : 0,
    "S" : -1
}

if (computer == n):
    print(f"You chose {your_choice[n]}")
    print(f"The computer chose {your_choice[computer]}")
    print("The game is a draw")
elif((n) == 1 and (computer) == 0):
    print(f"You chose {your_choice[n]}")
    print(f"The computer chose {your_choice[computer]}")
    print("You lose")
elif((n) == -1 and (computer) == 0):
    print(f"You chose {your_choice[n]}")
    print(f"The computer chose {your_choice[computer]}")
    print("You Win")
elif((n) == 0 and (computer) == 1):
    print(f"You chose {your_choice[n]}")
    print(f"The computer chose {your_choice[computer]}")
    print("You Win")
elif((n) == 0 and (computer) == -1):
    print(f"You chose {your_choice[n]}")
    print(f"The computer chose {your_choice[computer]}")
    print("You lose")
elif((n) == -1 and (computer) == 1):
    print(f"You chose {your_choice[n]}")
    print(f"The computer chose {your_choice[computer]}")
    print("You Win")
elif((n) == 1 and (computer) == -1):
    print(f"You chose {your_choice[n]}")
    print(f"The computer chose {your_choice[computer]}")
    print("You Win")
