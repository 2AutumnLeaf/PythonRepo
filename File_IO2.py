import random

def game():
    print("You are playing a game ")
    score = random.randint(1,62)
    with open("HiScore.txt","r") as f:
        HiScore = f.read()
        if(HiScore != ""):
            HiScore = int(HiScore)
        else:
            HiScore = 0
    print(f"High Score {str(HiScore)}")
    print(f"Your Score {score}")
    if(score>HiScore):
        with open("HiScore.txt","w") as f:
            f.write(str(score))
    
    return score

print(game())