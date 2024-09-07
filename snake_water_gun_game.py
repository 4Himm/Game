import random

'''
1 for Snake 
-1 for Water 
0 for Gun 
'''

values = [-1,1,0]
# Select a random value
computer =  random.choice(values)

youstr = input("enter your choice : ")
youdict = { "s": 1, "w": -1, "g": 0}
computerdict = {1 : "Snake", -1: "Water", 0: "Gun"}

you = youdict[youstr]

print(f"you chose {computerdict[you]} \nComputer chose {computerdict[computer]}")

if(computer==you):
    print("Game DRAW.")

else:
    if(computer == -1 and you == 1):
        print("You WIN!!")

    elif(computer == -1 and you == 0):
        print("You LOOSE!!")

    elif(computer == 1 and you == -1):
        print("You LOOSE!!")

    elif(computer == 1 and you == 0):
        print("You WIN!!")

    elif(computer == 0 and you == 1):
        print("You LOOSE!!")

    elif(computer == 0 and you == -1):
        print("You WIN!!")

    else:
        print("Something went Wrong!!!!")